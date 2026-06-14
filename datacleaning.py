# Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Import the data
data = pd.read_csv("hospitalreadmissions\diabetic_data.csv")
print(data.head())

# Examine the shape
print(data.shape)

data.replace('?', np.nan, inplace=True)
print(data.dtypes)
# Find missing values
print(data.isnull().sum())

# Inspect column values
for col in data.columns:
    print(data[col].unique())


missing_cols = ["race", "weight", "payer_code", "medical_specialty", "diag_1", "diag_2", "diag_3", "max_glu_serum", "A1Cresult"]
size = data.shape[0]
missing_40 = size * 0.40
drop_cols = ["payer_code"] # Payer code is irrelevant
for col in missing_cols:
    if data[col].isnull().sum() >= missing_40:
        drop_cols.append(col)

cleaning = data.drop(columns=drop_cols)    
print(cleaning.columns)

print("Dropped columns", drop_cols)

cleaning["change"]=cleaning["change"].replace("ch", "yes")
cleaning["age"]=cleaning["age"].replace('[', '(')

# Fill the unknown race and extra diagnoses with an unknown value
cleaning['race'] = cleaning['race'].fillna("Unknown")
cleaning['diag_2'] = cleaning['diag_2'].fillna("N/A")
cleaning['diag_3'] = cleaning['diag_3'].fillna("N/A")

# Remove the 21 rows with no diagnoses
cleaning = cleaning.dropna(subset=['diag_1'])

print(cleaning.isnull().sum())
print(cleaning.head())

cleaning.to_csv("hospitalreadmissions/cleaned_diabetic_data.csv", index=0)