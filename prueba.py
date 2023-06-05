import requests
import urllib3
import ssl
import json


class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

# Ejemplo de query
# http://stats.oecd.org/SDMX-JSON/data/<dataset identifier>/<filter expression>/<agency name>[ ?<additional parameters>]


r = get_legacy_session().get('http://stats.oecd.org/sdmx-json/data/QNA/ARG.GDP.VOBARSA.Q/all?startTime=2009-Q2&endTime=2011-Q4')

# status = r.status_code
# print(status)

data = r.json()

print(data)

# class QueryBuilder(): 
#     """
#     Retrieve data from OECD API based on https://data.oecd.org/api/sdmx-json-documentation/.
#     :param dataset_identifier: string, see api docs for details
#     :param location: list 3-code
#     :return: byte-string (needs to be decoded)
#     """
#     def __init__(self, dataset_identifier:str, location:list, subject:list, measure:list, frequency:str, agency_name:str, start_year:str, end_year:str):
#         self.dataset_identifier = dataset_identifier
#         pre_query = f"{'+'.join(location)}.{'+'.join(subject)}.{'+'.join(measure)}.{frequency}"
#         self.filter_expresion = pre_query if pre_query!="..." else "all"
#         self.agency_name = agency_name
#         self.query = f"http://stats.oecd.org/SDMX-JSON/data/{self.dataset_identifier}/{self.filter_expresion}/{self.agency_name}?startTime={start_year}&endTime={end_year}"
#         print(self.query)
    
#     def get_data(self):
#         r = get_legacy_session().get(self.query)
#         return r.json()
    
#     def get_response(self):
#         response = get_legacy_session().get(self.query)
#         return response
    
#     def get_response_text(self):
#         response = get_legacy_session().get(self.query)
#         return response.text
    
# builder = QueryBuilder(dataset_identifier="QNA", 
#                        location=["ARG"],
#                        subject=["GDP"],
#                        measure=[],
#                        frequency="Q",
#                        agency_name="all", 
#                        start_year="2020-Q1", 
#                        end_year= "2022-Q2")

# response = builder.get_response_text()

# # import ast

# # json_data = ast.literal_eval(json.dumps(response))

# print(response)
