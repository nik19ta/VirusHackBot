# -*- coding: utf-8 -*-
"""VirusHack Corona.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10TrYRQ1X_1AitKCYb73MHNINw5ak-b0y
"""

import pandas as pd

data = pd.read_csv('covid19_chisto.csv')

data.hosp_visit_date.fillna(0, inplace=True)

data.rename(columns={'hosp_visit_date': 'hosp_visit'}, inplace=True)

for i in range(data.hosp_visit.shape[0]):
  if not data.hosp_visit[i] == 0:
    data.hosp_visit[i] = 1

data.symptom.unique()

data.symptom.fillna(0, inplace=True)

all_symptoms = []
for i in range(data.symptom.shape[0]):
  if not data.symptom[i] == 0:
    all_symptoms += [i.strip() for i in data.symptom[i].split(',')]

all_symptoms = set(all_symptoms)

all_symptoms.remove('feve\\')

for item in all_symptoms:
  data[item] = 0

data.head()

data.drop({'exposure_end', 'exposure_start'}, axis=1, inplace=True)

data.head()

for i in range(data.symptom.shape[0]):
  if not data.symptom[i] == 0:
    list_ = [i.strip() for i in data.symptom[i].split(',')]
    for item in list_:
      try:
        data[item][i] = 1
      except KeyError:
        print('Не совпадение ключа!')

data.info()

data[data.symptom != 0]

data.gender = data.gender.map({
    'male': 1,
    'female': 0
})

data.gender.fillna(0, inplace=True)

data.to_csv('dataset_for_ML.csv', index=False)

data.drop({'symptom'}, axis=1, inplace=True)

import numpy as np

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

data.hosp_visit = data.hosp_visit.astype('int')

data.death = data.death.replace('2/14/2020', 1).replace('2/26/2020', 1).replace('2/13/2020', 1).replace('2/28/2020', 1).replace('2/27/2020', 1).replace('2/23/2020', 1).replace('2/24/2020', 1).replace('2/22/2020', 1).replace('2/25/2020', 1).replace('02/01/20', 1)

data.death = data.death.replace('2/19/2020', 1).replace('2/21/2020', 1)

data.death = data.death.astype('int')

data.recovered = data.recovered.replace('02/12/20', 1).replace('1/15/2020', 1).replace('12/30/1899', 1).replace('02/08/20', 1).replace('2/14/2020', 1).replace('02/04/20', 1).replace('2/18/2020', 1).replace('02/05/20', 1).replace('2/17/2020', 1).replace('02/09/20', 1).replace('2/15/2020', 1).replace('2/27/2020', 1).replace('2/19/2020', 1).replace('2/20/2020', 1).replace('1/17/2020', 1).replace('02/07/20', 1).replace('2/21/2020', 1).replace('2/23/2020', 1).replace('02/11/20', 1).replace('2/22/2020', 1).replace('2/16/2020', 1).replace('2/24/2020', 1).replace('2/26/2020', 1).replace('2/25/2020', 1).replace('02/06/20', 1).replace('2/28/2020', 1).replace('1/30/2020', 1).replace('2/13/2020', 1).replace('02/02/20', 1).replace('1/31/2020', 1)

data.recovered = data.recovered.astype('int')

clean_dataset(data)

X = data.drop({'death', 'recovered'}, axis=1)
y = data.death

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, y_train)
p = model.predict(X_test)
model.score(X_test, y_test)

"""**Проверка на коронавирус**


---


Проверка модели
"""

test = [[2013, 0, 4.4, 555, 0, 2, 1, 0, 0]]

df_test = pd.DataFrame(test, columns=['год выпуска', 'Пробег', 'Двигатель (объем)', 'Двигатель (мощность)', 'Владельцы', 'Коробка', 'Привод', 'ПТС'])
