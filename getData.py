import pandas as pd 

PATH_TO_DATA = r'sensorlogs-2019-12-09.csv'

pandas_data = pd.read_csv(PATH_TO_DATA, sep=';')
pandas_data_date_as_index = pandas_data.set_index('date',drop=True)
print(pandas_data_date_as_index)

print(type(pandas_data_date_as_index.at['2019-12-09 00:00:01','x']))

# list_of_indexes=dataFrame.index
# list_of_indexes=list_of_indexes.tolist()