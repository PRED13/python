import pandas as pd
serie = pd.Series([1,2,3])
serie
serie.name='nombre'
df = pd.DataFrame({'columna1' : [1,2,3,4], 'columna2': ['a','b','c','d']})
df
df.shape
df = pd.read csv('data/iris.data', header=None)
df.head()
df.tail(2)
nombres = ['logitud sepalo', 'ancho sepalo', 'ancho petalo', 'clase']
df.columns=nombres
df.head()
df.columns
df.index
df.shape
df.describe()
df['clase'].value_counts()
df.memory_usage().sum()/1024
df.T
df.short_values('ancho_sepalo',ascending=False)
df[['longitud_sepalo', 'longitud_petalo']]
