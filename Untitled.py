#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


df_2013 = pd.read_csv ("ESCOLAS_2013.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["ID_QUADRA_ESPORTES_COBERTA"])
df_2014 = pd.read_csv ("ESCOLAS_2014.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["ID_QUADRA_ESPORTES_COBERTA"])
df_2015 = pd.read_csv ("ESCOLAS_2015.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_COBERTA"])
df_2016 = pd.read_csv ("ESCOLAS_2016.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_COBERTA"])
df_2017 = pd.read_csv ("ESCOLAS_2017.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_COBERTA"])


# In[7]:


coberta_2013 = (df_2013.query("ID_QUADRA_ESPORTES_COBERTA == 1")["ID_QUADRA_ESPORTES_COBERTA"].count())
coberta_2014 = (df_2014.query("ID_QUADRA_ESPORTES_COBERTA == 1")["ID_QUADRA_ESPORTES_COBERTA"].count())
coberta_2015 = (df_2015.query("IN_QUADRA_ESPORTES_COBERTA == 1")["IN_QUADRA_ESPORTES_COBERTA"].count())
coberta_2016 = (df_2016.query("IN_QUADRA_ESPORTES_COBERTA == 1")["IN_QUADRA_ESPORTES_COBERTA"].count())
coberta_2017 = (df_2017.query("IN_QUADRA_ESPORTES_COBERTA == 1")["IN_QUADRA_ESPORTES_COBERTA"].count())


# In[8]:


df_2013d = pd.read_csv ("ESCOLAS_2013.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["ID_QUADRA_ESPORTES_DESCOBERTA"])
df_2014d = pd.read_csv ("ESCOLAS_2014.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["ID_QUADRA_ESPORTES_DESCOBERTA"])
df_2015d = pd.read_csv ("ESCOLAS_2015.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_DESCOBERTA"])
df_2016d = pd.read_csv ("ESCOLAS_2016.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_DESCOBERTA"])
df_2017d = pd.read_csv ("ESCOLAS_2017.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_QUADRA_ESPORTES_DESCOBERTA"])


# In[9]:


descoberta_2013 = (df_2013d.query("ID_QUADRA_ESPORTES_DESCOBERTA == 1")["ID_QUADRA_ESPORTES_DESCOBERTA"].count())
descoberta_2014 = (df_2014d.query("ID_QUADRA_ESPORTES_DESCOBERTA == 1")["ID_QUADRA_ESPORTES_DESCOBERTA"].count())
descoberta_2015 = (df_2015d.query("IN_QUADRA_ESPORTES_DESCOBERTA == 1")["IN_QUADRA_ESPORTES_DESCOBERTA"].count())
descoberta_2016 = (df_2016d.query("IN_QUADRA_ESPORTES_DESCOBERTA == 1")["IN_QUADRA_ESPORTES_DESCOBERTA"].count())
descoberta_2017 = (df_2017d.query("IN_QUADRA_ESPORTES_DESCOBERTA == 1")["IN_QUADRA_ESPORTES_DESCOBERTA"].count())


# In[10]:


print(f'Em 2013 {coberta_2013} estavam cobertas e {descoberta_2013} descobertas.')
print(f'Em 2014 {coberta_2014} estavam cobertas e {descoberta_2014} descobertas.')
print(f'Em 2015 {coberta_2015} estavam cobertas e {descoberta_2015} descobertas.')
print(f'Em 2016 {coberta_2016} estavam cobertas e {descoberta_2016} descobertas.')
print(f'Em 2017 {coberta_2017} estavam cobertas e {descoberta_2017} descobertas.')


# In[58]:


x = [2013, 2014, 2015, 2016, 2017]
y = [(coberta_2013), (coberta_2014), (coberta_2015), (coberta_2016), (coberta_2017)]

plt.title('Quadras cobertas Ensino Básico Público')
plt.xlabel('Ano')
plt.ylabel('Escolas')
plt.bar(x, y)
plt.show()


# In[14]:


x = [2013, 2014, 2015, 2016, 2017]
y = [(descoberta_2013), (descoberta_2014), (descoberta_2015), (descoberta_2016), (descoberta_2017)]

plt.title('Quadras descobertas Ensino Básico Público')
plt.xlabel('Ano')
plt.ylabel('Escolas')
plt.bar(x, y)
plt.show()


# In[141]:


x = [2013, 2014, 2015, 2016, 2017]
y = [(coberta_2013), (coberta_2014), (coberta_2015), (coberta_2016), (coberta_2017)]
b = [(descoberta_2013), (descoberta_2014), (descoberta_2015), (descoberta_2016), (descoberta_2017)]
fig = plt.figure()
ax1 = fig.add_subplot()

plt.title('Quadras cobertas e descobertas Ensino Básico Público')
plt.xlabel('Ano')
plt.ylabel('Escolas')
ax1.axhline(44000, linestyle = ':')
ax1.axvline(2017.0, linestyle = ':')
ax1.axhline(42000, linestyle = ':')
ax1.axvline(2016.5, linestyle = ':')
ax1.axhline(40000, linestyle = ':')
ax1.axvline(2016.0, linestyle = ':')
ax1.axhline(38000, linestyle = ':')
ax1.axvline(2015.5, linestyle = ':')
ax1.axhline(36000, linestyle = ':')
ax1.axvline(2015.0, linestyle = ':')
ax1.axhline(34000, linestyle = ':')
ax1.axvline(2014.5, linestyle = ':')
ax1.axhline(32000, linestyle = ':')
ax1.axvline(2014.0, linestyle = ':')
ax1.axhline(30000, linestyle = ':')
ax1.axvline(2013.5, linestyle = ':')
ax1.axvline(2013.0, linestyle = ':')
plt.plot(x, y,  color ='y', label = 'Cobertas')
plt.scatter(x, y, color = 'r', marker = '*', s=100)
plt.plot(x, b,color = 'g', label = 'Descobertas')
plt.scatter(x, b, color = 'm', marker = '*', s=100)
for f, g in enumerate(y):
    g = round(g, 2)
    plt.text(x[f] - 0.2, g - 2000, str(g))
for f, g in enumerate(b):
    g = round(g, 2)
    plt.text(x[f] - 0.2, g + 1000, str(g))
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




