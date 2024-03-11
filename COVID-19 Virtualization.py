#!/usr/bin/env python
# coding: utf-8

# In[1]:


# first cell handles imports, stylings, constants, and initialization of data

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("seaborn-deep")  # graph styling by legends

AGGREGATED_DATA = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"

data = pd.read_csv(AGGREGATED_DATA, parse_dates=["Date"])
data["Total Cases"] = data[["Confirmed", "Recovered", "Deaths"]].sum(axis=1)


# In[2]:


# Second cell handles worldwide aggregation

ww_df = data.groupby(["Date"]).sum()
# ww_df.head()
w = ww_df.plot(figsize=(16,10))
w.set_xlabel("Data")
w.set_ylabel("# of Cases WorldWide")
w.title.set_text("WorldWide Covid Insights")

plt.show()


# In[3]:


# Third Cell, compare worldwide aggregation to localized US/UK/CN

us_df = data[data["Country"] == "US"].groupby(["Date"]).sum()  # filters by US/country.
uk_df = data[data["Country"] == "United Kingdom"].groupby(["Date"]).sum()  # filters by UK
ch_df = data[data["Country"] == "China"].groupby(["Date"]).sum()  # filters by zh-CN

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)  # 1x1 @ 1st subplot

ax.plot(ww_df[["Total Cases"]], label="Worldwide")
ax.plot(us_df[["Total Cases"]], label="United States")
ax.plot(uk_df[["Total Cases"]], label="United Kingdom")
ax.plot(ch_df[["Total Cases"]], label="China")
ax.set_xlabel("Data")
ax.set_ylabel("# of Total Cases")
ax.title.set_text("WorldWide vs. US Total Cases")

plt.legend(loc="upper left")
plt.show()


# In[4]:


# Fourth Cell. Daily Cases for country XYZ and its own Deaths

