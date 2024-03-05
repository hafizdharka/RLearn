import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy
import streamlit as st

st.title('Proyek Akhir Analisis Data')
st.write('Muhammad Hafizd Harkaputra -  M001D4KY1680')

st.header('GATHERING DATA')
st.write('Data yang dipilih adalah Bike Sharing Dataset Day.csv. Data terdiri dari 731 amatan hari dan 16 kolom peubah. ')
mentah_df = pd.read_csv('https://raw.githubusercontent.com/hafizdharka/RLearn/main/day.csv')
mentah_df

mentah_df.info()

st.header('ASSESSING DATA')
st.write('Pada proses assesing data, dilakukan pengecekan')
st.write("1. Missing Value")
st.write('2. Duplicate Data')

code = """mentah_df.isna().sum()
mentah_df.duplicated().sum()"""
st.code(code, language='python')

mentah_df.isna().sum()
mentah_df.duplicated().sum()

st.write('Berdasarkan hasil pengecekan, tidak terdapat Missing Value dan Duplicated Data pada dataset yang digunakan.')

mentah_df.describe()

st.header('CONVERTING DATA')
st.write('Beberapa kolom pada dataset masih bertipe data numerik, jadi perlu adanya convert tipe data untuk penyesuaian pada nilai yang terdapat pada kolom amatan, sehingga peubah season, yr, mnth, holiday, weekday, weathersit, workingday diconvert menjadi data kategorik. Sementara, peubah datetime diubah ke tipe data datetime.')

mentah_df['season'] = mentah_df['season'].astype('category')
mentah_df['yr'] = mentah_df['yr'].astype('category')
mentah_df['mnth'] = mentah_df['mnth'].astype('category')
mentah_df['holiday'] = mentah_df['holiday'].astype('category')
mentah_df['weekday'] = mentah_df['weekday'].astype('category')
mentah_df['weathersit'] = mentah_df['weathersit'].astype('category')
mentah_df['season'] = mentah_df['season'].astype('category')
mentah_df['workingday'] = mentah_df['workingday'].astype('category')

code = """mentah_df['season'] = mentah_df['season'].astype('category')
mentah_df['yr'] = mentah_df['yr'].astype('category')
mentah_df['mnth'] = mentah_df['mnth'].astype('category')
mentah_df['holiday'] = mentah_df['holiday'].astype('category')
mentah_df['weekday'] = mentah_df['weekday'].astype('category')
mentah_df['weathersit'] = mentah_df['weathersit'].astype('category')
mentah_df['season'] = mentah_df['season'].astype('category')
mentah_df['workingday'] = mentah_df['workingday'].astype('category')"""
st.code(code, language='python')

datetime_columns = ["dteday"]

for column in datetime_columns:
  mentah_df[column] = pd.to_datetime(mentah_df[column])

mentah_df.info()

st.header('MAPPING DATA')
st.write('Agar lebih mudah diinterpretasikan, nilai-nilai pada peubah kategorik akan diganti dengan nilai yang lebih spesifik. Berdasarkan keterangan pada readme.txt, panduan keterangan setiap nilai sebagai berikut.')

code = """mentah_df['season'] = mentah_df['season'].cat.rename_categories({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'})
mentah_df['yr'] = mentah_df['yr'].cat.rename_categories({0: '2011', 1: '2012'})
mentah_df['mnth'] = mentah_df['mnth'].cat.rename_categories({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Des'})"""
st.code(code, language='python')

st.header('EXPLORATORY DATA ANALYSIS (EDA)')
st.write('Berdasarkan hasil cleaning data dan definisi setiap kolom pada readme.txt pada data Bike Sharing Dataset, terdapat beberapa pertanyaan yang ingin diuji. Diantara lain;')
st.write('1. Bagaimana hubungan antara peubah numerik?')
st.write('2. Peubah numerik apa yang paling memengaruhi peubah cnt (Jumlah Pengendara Sepeda Harian).')
st.write('3. Apakah ada perbedaan Jumlah Pengendara Sepeda Harian setiap musim?')
st.write('4. Apakah ada perbedaan Jumlah Pengendara Sepeda Harian peubah?')


st.subheader('Plot Korelasi Peubah Numerik')
st.write('Pada plot korelasi peubah numerik, dapat dilihat ada tiga peubah yang memiliki pengaruh signifikan terhadap peubah cnt (Jumlah Pengendara Harian) (nilai korelas > 0.6), yaitu registered, casual, dan temp')
variable_df = mentah_df[['season','temp','hum','windspeed','casual','registered','cnt']]
corr_matrix = variable_df.corr(numeric_only=True, method='spearman')
heatmap = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
st.pyplot(heatmap.figure)
plt.clf()

st.subheader('Perbandingan Boxplot Jumlah Pengendara Harian berdasarkan casual dan registered Setiap Bulan')
st.write('Perbandingan Boxplot **cnt** (Jumlah Pengendara Harian) berdasarkan casual dan registered setiap bulan. Berdasarkan hasil perbandingan, sebaran jumlah pengendara harian cenderung tinggi pada bulan Juli hingga Oktober.')

df = mentah_df[['mnth','casual','registered']]
melted_df = pd.melt(df,id_vars='mnth', var_name='status',value_name= 'Pengendara Harian')
boxplot = sns.boxplot(melted_df, x='mnth', y= 'Pengendara Harian',hue='status', showfliers=False)
st.pyplot(plt)
plt.clf()

st.subheader('Perbandingan *Boxplot* Jumlah Pengendara Harian berdasarkan *casual* dan *registered* Setiap Musim')
st.write('Perbandingan Boxplot **cnt** (Jumlah Pengendara Harian) berdasarkan casual dan registered setiap bulan. Berdasarkan hasil perbandingan, sebaran jumlah pengendara harian paling tinggi terdapat pada Musim Panas, yaitu sebanyak 1.061.129 orang.')
df = mentah_df[['season','casual','registered']]
melted_df = pd.melt(df,id_vars='season', var_name='status',value_name= 'Pengendara Harian')
boxplot2 = sns.boxplot(data = melted_df, x='season', y= 'Pengendara Harian',hue='status', showfliers=False)
st.pyplot(plt)







