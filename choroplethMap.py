#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.graph_objs as go
df = pd.read_csv("StateCode_Count.csv")
df = df.reset_index()
import plotly.express as px

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['Count_Star'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Count",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()


# In[3]:


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("Fips_Count1.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth(df, geojson=counties, locations='fips code',color="Count_Star",
                           color_continuous_scale="blues",
                           range_color=(0, 120),
                           scope="usa",
                           labels={'Count':'Count'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[ ]:




