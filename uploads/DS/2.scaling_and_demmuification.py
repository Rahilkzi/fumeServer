import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data={
    'Product':['Apple_Juice','Banana_Smoothie','Orange_Jam','Grape_Jelly','Kiwi_Parfait','Mango_Chutney','Pineapple_Sorbet','Strawberry_Yogurt','BlueBerry_pie','Cherry_Salsa'],
    'Category':['Apple','Banana','Orange','Grape','Kiwi','Mango','Pineapple','Strawberry','Blueberry','Cherry'],
    'Sales':[1200,1700,2200,1400,2000,1000,1500,1800,1300,1600],
    'Cost':[600,850,1100,700,1000,500,750,900,650,800],
    'Profit':[600,850,1100,700,1000,500,750,900,650,800]
    }

df=pd.DataFrame(data)

print("Original Dataset:")
print(df)

numeric_columns=['Sales','Cost','Profit']
scaler_standardization=StandardScaler()
scaler_normalization=MinMaxScaler()

df_scaled_standardized=pd.DataFrame(scaler_standardization.fit_transform(df[numeric_columns]),
             columns=numeric_columns)

df_scaled=pd.concat([df_scaled_standardized,df.drop(numeric_columns,axis=1)],axis=1)

print("\nDataset after Feature Scaling:")
print(df_scaled)

categorical_columns=['Product','Category']

preprocessor=ColumnTransformer(
    transformers=[
        ('categorical',OneHotEncoder(),categorical_columns)
    ],
    remainder='passthrough'
)

df_dummified=pd.DataFrame(preprocessor.fit_transform(df))

print("\nDataset after Feature Dummification:")
print(df_dummified)

