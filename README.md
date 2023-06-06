# Simple OECD Stats API Python Wrapper

Install via `git clone...`

Example: 

```
from oecd_wrapper import QueryBuilder


# Ejemplo...
# Defino los parámetros para hacer la búsqueda

dataset_id = "PRICES_CPI"
location = ["ARG"] 
subject=["CPALTT01","CP030000"] # CPALTT01 es All Items, CP030000 es Clothing and footwear
measure=["IXNB"] # IXNB es National Index
frequency="M" # Mensual
agency_name="all" # No tengo idea
startTime="2014" # El año desde donde comienza
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
```
Example output

```
Country                 Argentina                                
Subject    CPI: 01-12 - All items CPI: 03 - Clothing and footwear
Measure            National Index                  National Index
Frequency                 Monthly                         Monthly
Time                                                             
2016-12-01               100.0000                        100.0000
2017-01-01               101.5859                         99.0066
2017-02-01               103.6859                         98.8523
2017-03-01               106.1476                        102.2550
2017-04-01               108.9667                        106.8806
...                           ...                             ...
2022-12-01              1134.5880                       1371.3370
2023-01-01              1202.9790                       1402.8450
2023-02-01              1282.7090                       1457.7660
2023-03-01              1381.1600                       1595.0860
2023-04-01              1497.2150                       1768.097
```