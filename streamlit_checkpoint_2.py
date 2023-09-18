# -*- coding: utf-8 -*-
"""streamlit_checkPoint_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MXi0guqVxV1vyPZlI-RJEdsZqZiktwrp
"""


"""#**1. Install necessary package**"""
import subprocess

for package in ['pandas', 'numpy', 'scikit-learn', 'pydrive', 'google', 'oauth2client', 'streamlit']:
    try:
        import pandas_profiling as pp
    except:
        result = subprocess.run(["pip", "install", package], tdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

import pandas as pd
import numpy as np
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *

from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive

from google.colab import auth

from oauth2client.client import GoogleCredentials

auth.authenticate_user()

gauth = GoogleAuth()

gauth.credentials = GoogleCredentials.get_application_default()

drive = GoogleDrive(gauth)

file_download = drive.CreateFile({'id':'1FrFTfUln67599LTm2uMTSqM8DjqpAaKL'})

file_download.GetContentFile('Financial_inclusion_dataset.csv')

"""#**2. Import the data and perform the basic data exploration**"""

df = pd.read_csv('Financial_inclusion_dataset.csv')

"""###**⏺ Display general information about dataset**"""

df

df.info()

"""###**⏺ Create pandas profiling report**"""

report = pp.ProfileReport(df)
report.to_notebook_iframe()

"""###**⏺ Handle missing value and corrupted**"""

'''
  There is no missing value
'''

"""###**⏺ Remove duplicate value**"""

'''
  There is no duplicate value
'''

"""###**⏺ Handle outliers**"""

'''
  There is no outliers
'''

"""###**⏺ Encode categorical features**"""

categ_feat = [i for i in df.columns if df[i].dtype==object]
num_feat = [i for i in df.columns if df[i].dtype!=object]

encode = LabelEncoder()
for i in categ_feat:
  df[i] = encode.fit_transform(df[i])

df

"""#**3. Train and test machine learning classify**"""

features = [i for i in df.columns if i not in ['bank_account']]
target = 'bank_account'

x_train, x_test, y_train, y_test = train_test_split(df[features], df[target], train_size=0.7, random_state=39)

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
score = accuracy_score(y_pred, y_test)
f'accuracy score = {score}'

"""#**4. Create streamlit application and add inputs field**"""

st.title("Financial Inclusion in Africa")

input_features = st.text_input("input the features. eg: feat1,feat2,feat3 : ")
if st.button('valid'):
  val_features = input_features.title()
  list_features = val_features.split(',')
  st.success('validation success')

"""#**6. Import the model into streamlit and make prediction**"""

x_train, x_test, y_train, y_test = train_test_split(df[list_features], df[features], train_size=0.7, random_state=39)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
score = accuracy_score(y_pred, y_test)
st.write("the y prediction is ",y_pred)
st.write('the accuracy score is ', score)

"""#**6. Deploy the model on streamlit share**"""
