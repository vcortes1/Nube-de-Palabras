# -*- coding: utf-8 -*-
"""NubedePalabras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sFuusUU52egcDL_AEyoitRDVh-bk7VV_

#Importamos Base de datos
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials


# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

link = 'https://docs.google.com/spreadsheets/u/4/d/199fJfcuQqKiuHOx0DuwH8zPZhEOhyFh8/edit?usp=drive_web&ouid=113137427337237414865&rtpof=true'

import pandas as pd

# to get the id part of the file
id = link.split("/")[-2]

downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('Proceso Constituyente.xlsx')

df = pd.read_excel('Proceso Constituyente.xlsx')
df.head(10)

muestra =df.sample(20)

muestra.head(10)

"""#Limpieza de cuerpo"""

muestra['cuerpo'] = muestra['cuerpo'].str.lower()
muestra['cuerpo'] =muestra['cuerpo'].str.replace('rt','')

caracteres =['-', ',','´','.','1','2','3','4','5','6','7','8','9','0','120382','chile','#','&','http\S+', 'RT', ':','@', ';', '\\n','_','!', '\\r', '\ ','?','¿' ]

for j in caracteres:#se quitan numeros y otros caracteres indeseados
  muestra['cuerpo']=muestra['cuerpo'].str.replace(j," ")


muestra['cuerpo'].str.strip()


muestra.head(10)

"""Limpieza base completa"""

df['cuerpo'] = df['cuerpo'].str.lower()
df['cuerpo'] =df['cuerpo'].str.replace('rt','')

caracteres =['-', ',','´','.','1','2','3','4','5','6','7','8','9','0','120382','chile','#','&','http\S+', 'RT', ':','@', ';', '\\n','_','!', '\\r', '\ ','?','¿','%']

for j in caracteres:#se quitan numeros y otros caracteres indeseados
  df['cuerpo']=df['cuerpo'].str.replace(j," ")

  df['cuerpo'].str.strip()


df.head(10)

df['cuerpo']=df['cuerpo'].replace('%','')
df['cuerpo']=df['cuerpo'].replace('(','')
df['cuerpo']=df['cuerpo'].replace(')','')

"""Instalamos nube de palabras"""

!pip install wordcloud

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop = stopwords.words('spanish')

nltk.download('punkt')

from nltk.tokenize import word_tokenize

muestra['SIN'] = muestra['cuerpo'].apply(lambda x: ' '.join ([word for word in x.split()  if word not in (stop)]))

df['SIN'] = df['cuerpo'].apply(lambda x: ' '.join ([word for word in x.split()  if word not in (stop)]))

muestra[['cuerpo','SIN']]

df[['cuerpo','SIN']]

"""#Nube de palabras"""

import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = ' '.join(i for i in muestra.SIN)
wordcloud = WordCloud(background_color = 'rgba(255,255,255,0)', width=1800, height=1400).generate(texto)

plt.imshow(wordcloud, interpolation ='bilinear')
plt.axis('off')
plt.show()

texto = ' '.join(i for i in df.SIN)
wordcloud = WordCloud(background_color = 'rgba(255,255,255,0)', width=1800, height=1400).generate(texto)

plt.imshow(wordcloud, interpolation ='bilinear')
plt.axis('off')
plt.show()