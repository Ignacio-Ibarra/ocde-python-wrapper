from oecd_wrapper import QueryBuilder


# Ejemplo...
# Defino los parámetros para hacer la búsqueda

dataset_id = "PRICES_CPI"
location = ["ARG"] 
subject=["CPALTT01","CP030000"] # CPALTT01 es All Items, CP030000 es Clothing and footwear
measure=["IXNB"] # IXNB es National Index
frequency="M" # Mensual
agency_name="all" # No tengo idea
startTime="2000" # El año desde donde comienza
endTime= "2023" # El año donde termina
layout = "ts" # para que me lo traiga como serie de tiempo. 

builder = QueryBuilder(dataset_identifier=dataset_id,
                       location=location,
                       subject=subject,
                       measure=measure,
                       frequency=frequency,
                       agency_name=agency_name,
                       startTime=startTime,
                       endTime=endTime,
                       layout=layout)

df = builder.get_dataframe()

print(df)


