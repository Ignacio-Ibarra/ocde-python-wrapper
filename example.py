from oecd_wrapper import QueryBuilder
import json


# Ejemplo...
# Defino los parámetros para hacer la búsqueda

# dataset_id = "PRICES_CPI"
# location = ["ARG"] 
# subject=["CPALTT01","CP030000"] # CPALTT01 es All Items, CP030000 es Clothing and footwear
# measure=["IXNB"] # IXNB es National Index
# frequency="M" # Mensual
# agency_name="all" # No tengo idea
# startTime="2000" # El año desde donde comienza
# endTime= "2023" # El año donde termina
# layout = "ts" # para que me lo traiga como serie de tiempo. 

# builder = QueryBuilder(dataset_identifier=dataset_id,
#                        location=location,
#                        subject=subject,
#                        measure=measure,
#                        frequency=frequency,
#                        agency_name=agency_name,
#                        startTime=startTime,
#                        endTime=endTime,
#                        layout=layout)


url = "https://stats.oecd.org/SDMX-JSON/data/PRICES_CPI/ARG+USA+CHL.CPALTT01.IXOB.M/all?startTime=1914-01&endTime=2023-05"

builder = QueryBuilder(url)

data = builder.get_dataframe()

data.to_excel("example.xlsx")

# print(json.dumps(data, indent=4))




