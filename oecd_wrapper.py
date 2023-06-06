import _session
import _parser





class QueryBuilder(): 
    """
    Query Builder to retrieve data from OECD API based on https://data.oecd.org/api/sdmx-json-documentation/.
    
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
    def __init__(self, 
                 dataset_identifier:str, 
                 location:list, 
                 subject:list, 
                 measure:list, 
                 frequency:str, 
                 agency_name:str, 
                 startTime:str, 
                 endTime:str,
                 layout:str):
        self.dataset_identifier = dataset_identifier
        pre_query = f"{'+'.join(location)}.{'+'.join(subject)}.{'+'.join(measure)}.{frequency}"
        self.filter_expresion = pre_query if pre_query!="..." else "all"
        self.agency_name = agency_name
        self.startTime = startTime
        self.endTime = endTime
        if layout == "ts":
            self.layout = ""
        elif layout == "flat":
            self.layout = "&dimensionAtObservation=allDimensions"
        else:
            raise ValueError("Wrong value to layout parameter: 'ts' to get a time series layout or 'flat' to get all dimensions") 
        self.query = f"http://stats.oecd.org/SDMX-JSON/data/{self.dataset_identifier}/{self.filter_expresion}/{self.agency_name}?startTime={self.startTime}&endTime={self.endTime}{self.layout}"
        # print(self.query)
    
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



