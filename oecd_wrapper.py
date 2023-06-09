import _session
import _parser
import numpy as np
import re





class QueryBuilder(): 
    """
    Query Builder to retrieve data from OECD API based on https://data.oecd.org/api/sdmx-json-documentation/.
    :param *args:              string url starting with 'http://stats.oecd.org/SDMX-JSON/data/'
    :param dataset_identifier: string, see api docs for details, e.g. 'PRICE_CPI' refers to Consumer Price Indexes
    :param location:           list 3-code e.g. 'ARG' refers to Argentina
    :param subject:            list of subjects, see api docs for details, e.g. 'CP030000' refers to Clothing and footwear
    :param measure:            list of measures, see api docs for details, e.g. 'IXNB' stands for National Index
    :param frequency:          string, 'A': annual, 'Q' quarterly and 'M' monthly
    :param agency_name:        string, see api docs for details, e.g. 'all' refers to all agencies
    :param startTime:          string, e.g. '2012-Q3' means that query will collect data from 2012 3rd quarter, 
                               '2012' will collect from 1st month, and '2012-05' from 5th month
    :param endTime:            string, e.g. '2022-Q2' means that query will collect until 2022 2nd quarter, 
                               '2022' will collect until 12th month, and '2022-08' until 8th month
    :param layout              string, could be 'ts' to get a time series layout or 'flat' to get all dimensions. 
                      
    """
    
    def __init__(self, *args, **kwargs): 
        self.base_url = "https://stats.oecd.org/SDMX-JSON/data/"
        self.keywords = ['dataset_identifier','location', 'subject', 'measure', 'frequency', 'agency_name', 'startTime', 'endTime', 'layout']
        if args:
            if len(args) == 1:
                if isinstance(args[0], str):
                    url = args[0] 
                    if url.startswith(self.base_url):
                        self.query = url
                    else:
                        raise ValueError(f"The url provided must begain with '{self.base_url}'\n") 
                else:
                    raise ValueError(f"You must provided a valid string as argument")
            else: 
                raise ValueError("Only one string must be passed") 
        
        if kwargs:
            if set(kwargs.keys()) == set(self.keywords):   
                self.dataset_identifier = kwargs['dataset_identifier']
                self.locations = kwargs['location']
                self.subjects = kwargs['subject']
                self.measures = kwargs['measure']
                self.frequency = kwargs['frequency']
                self.agency_name = kwargs['agency_name']
                self.startTime = kwargs['startTime']
                self.endTime = kwargs['endTime']
                layout = kwargs['layout']
                if layout == "ts":
                    self.layout = ""
                elif layout == "flat":
                    self.layout = "&dimensionAtObservation=allDimensions"
                else:
                    raise ValueError("Wrong value to layout parameter: 'ts' to get a time series layout or 'flat' to get all dimensions") 
            else:
                raise ValueError(f"Invalid set of parameters was passed. Available params are: {', '.join(self.keywords)}")
                      
    def get_jdata(self):
        r = _session.get_legacy_session().get(self.query)
        return r.json()
    
    def get_response(self):
        response = _session.get_legacy_session().get(self.query)
        return response
    
    def get_response_text(self):
        response = _session.get_legacy_session().get(self.query)
        return response.text
    
    def get_dataframe(self):
        jdata = self.get_jdata() 
        return _parser.read_jdata(jdata=jdata)



