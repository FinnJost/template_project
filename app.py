# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px
# import plotly.graph_objects as go
# from urllib.request import urlopen
# import json
# from copy import deepcopy

# # First some MPG Data Exploration
# mpg_df = pd.read_csv("./data/raw/mpg.csv")

# # Add title and header
# st.title("Introduction to Streamlit")
# st.header("MPG Data Exploration")

# # We can write stuff
# url = "https://archive.ics.uci.edu/ml/datasets/auto+mpg"
# st.write("data source:", url)
# # "This works too:", url

# @st.cache_data #decorator
# def load_data(path):
#     df = pd.read_csv(path)
#     return df

# mpg_df_raw = load_data(path="./data/raw/mpg.csv") #for speed
# mpg_df = deepcopy(mpg_df_raw) #for security

# #st.table(data=mpg_df)
# if st.sidebar.checkbox("Show Dataframe"):
#     st.subheader("This is my dataset:")
#     st.dataframe(data=mpg_df)

# left_column, right_column=st.columns(2)

# show_means = right_column.radio(
#     label='Show Class Means', options=['Yes', 'No'])

# years = ["All"]+sorted(pd.unique(mpg_df['year']))
# year=left_column.selectbox("Choose a year", years,index=0) ### index says at what option to start

# if year == "All":
#     reduced_df = mpg_df
# else:
#     reduced_df = mpg_df[mpg_df["year"] == year]

# means = reduced_df.groupby('class').mean(numeric_only=True)

# plot_types = ["Matplotlib", "Plotly"]
# plot_type = right_column.radio("Choose Plot Type", plot_types)

# #matplotlib
# m_fig, ax = plt.subplots(figsize=(10, 8))
# if show_means == "Yes":
#     ax.scatter(means['displ'], means['hwy'], alpha=0.7,
#                color="red", label="Class Means")
# ax.scatter(reduced_df['displ'], reduced_df['hwy'], alpha=0.7)
# ax.set_title("Engine Size vs. Highway Fuel Mileage")
# ax.set_xlabel('Displacement (Liters)')
# ax.set_ylabel('MPG')

# # st.pyplot(m_fig)

# # In Plotly
# p_fig = px.scatter(reduced_df, x='displ', y='hwy', opacity=0.5,
#                    range_x=[1, 8], range_y=[10, 50],
#                    width=750, height=600,
#                    labels={"displ": "Displacement (Liters)",
#                            "hwy": "MPG"},
#                    title="Engine Size vs. Highway Fuel Mileage")

# if show_means == "Yes":
#     p_fig.add_trace(go.Scatter(x=means['displ'], y=means['hwy'],
#                                mode="markers",
#                                marker=dict(color="red")))  # ✅ Correct placement of color

#     p_fig.update_layout(showlegend=False)

# p_fig.update_layout(title_font_size=22)

# #st.plotly_chart(p_fig)

# if plot_type == "Matplotlib":
#     st.pyplot(m_fig)
# else:
#     st.plotly_chart(p_fig)

# # Sample Streamlit Map
# st.subheader("Streamlit Map")
# ds_geo = px.data.carshare()

# ds_geo['lat'] = ds_geo['centroid_lat']
# ds_geo['lon'] = ds_geo['centroid_lon']

# st.map(ds_geo)


#### Putting the exercise of 25-02-25 on this app

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
from plotly.subplots import make_subplots
from urllib.request import urlopen
import json
import plotly.express as px
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# data to do the world-map plot 
with open("data/raw/countries.geojson") as f:
    countries = json.load(f)
# data of internet usage
df = pd.read_csv("data/raw/share-of-individuals-using-the-internet.csv")
# data of population
data = px.data.gapminder()


int_pop = 'Individuals using the Internet (% of population)'

countries_list = ['Afghanistan', 'Albania', 'Algeria',
       'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda',
       'Argentina', 'Armenia', 'Aruba', 'Australia',
       'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
       'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
       'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria',
       'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
       'Cape Verde', 'Cayman Islands', 'Central African Republic',
       'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 
       'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao',
       'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark',
       'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Eswatini', 'Ethiopia', 'Faeroe Islands', 'Fiji', 'Finland', 'France',
       'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany',
       'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam',
       'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Honduras', 'Hong Kong', 'Hungary',
       'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
       'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
       'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos',
       'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 
       'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia',
       'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
       'Mauritius', 'Mexico', 'Micronesia (country)',
       'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
       'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
       'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
       'Niger', 'Nigeria', 'North America', 'North Korea',
       'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman',
       'Pakistan', 'Palau', 'Palestine',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
       'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania',
       'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
       'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
       'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania',
       'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago',
       'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
       'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'United Kingdom', 'United States', 'United States Virgin Islands',
       'Uruguay', 'Uzbekistan', 'Vanuatu',
       'Venezuela', 'Vietnam', 'World', 'Yemen', 'Zambia', 'Zimbabwe']

# Add title and header
st.title("Developement of Internet Usage Worldwide")
st.header("Internet Usage in Percent of the Population:")


# Add plot showing the internet usage as the color of the country on the map
#   with a selector putting the year, for which internet usage is displayed
years = sorted(df['Year'].unique())
year=st.selectbox("Choose a year", years,index=0) ### index says at what option to start

fig = go.Figure(
    go.Choroplethmapbox(
        geojson=countries, 
        locations=df[df['Year'] == year]['Code'], 
        z=df[df['Year'] == year][int_pop],
        featureidkey='properties.ISO_A3',
        colorscale="Viridis", zmin=0, zmax=100,
        marker_opacity=0.5, marker_line_width=0
                    )
                )
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_center = {"lat": 17.0902, "lon": 0}
                  )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)


# Add plot that shows the developement of the internet usage for a selected country
if st.checkbox("Developement for specific country"):
#     st.subheader("This is my dataset:")
#     st.dataframe(data=mpg_df)
    countries = countries_list
    st.subheader(f"Developement of Internet Usage for")
    country = st.selectbox("Choose a country", countries,index=0)
    country_code = df[df['Entity'] == country]['Code'].unique()[0]
    # st.subheader(f'{country_code}')
    st.markdown(f'**Comparing the Internet Usage in {country} to that in the USA**')
    fig = go.Figure()
    fig.add_scatter(x = df[df['Code'] == 'USA']['Year'], y = df[df['Code'] == 'USA'][int_pop], mode='lines+markers', name='USA')
    fig.add_scatter(x = df[df['Code'] == country_code]['Year'], y = df[df['Code'] == country_code][int_pop], mode='lines+markers', name=country)
    fig.update_layout(yaxis = {'title':{'text': 'Internet Usage in Proportion of Population'}}, 
                      xaxis = {'title':{'text': 'Years'}})
    
    st.plotly_chart(fig)



### Make a plot comparing the internet usage to the GDP perCapita
#       also include info about life expectancy in color of markers
#       and total population in size of markers
st.subheader(f"Internet usage vs GDP per Capita")
st.markdown('Comparing the **internet usage** in the world with the **GDP per capita** in the respective countries, one realizes a clear trend. It is commonly accepted to use the GDP per capita as a indicator for the development of a country. Therefore, it should not come as a surprize that the trend in the plots, that is higher GDP per capita suggests larger proportion of people having access (and using) the internet. ')
st.markdown('This trend is evident from 1992, when internet is used in a significant amount of countries and data is available, to more recent years. Inspecting the temporal component, the GDP per capita is, furthermore, a good indicator about the **timeframe** in which internet usage rises. Comparing a low developed country like Afganistan, where the internet usage only recently rose over 1%, to the US where the usage rose already in the 90s and reached roughly 60% already in 2002. ')
st.markdown('Similar trends on a varying level can be found for most countries, highlighting here also developent of eastern Asian countries with large **populations** (indicated by size of markers) like India and China, which is qick compared to that of other Asian countries such as Afganistan or subsahel African countries such as Burundi. It should be noted that from this analysis a clear trend of internet usage with population cannot be deducted. More obvious is the dependence **life expectancy**, indicating lower with green and higher with blue colors, on both GDP per capita and internet usage. This suggests that both life expectancyand internet usage profit from a development of the societies. ')
st.markdown('Finally, it can be noted that the population of the countries is up to a certain point influenced by the **life expectancy** of their inhabitants. However, this effect is only evident in the data for countries with comparatively low GDP per capita and ceases in the upper two quartiles. ')

left_column, right_column=st.columns(2)

# placeholder1 = st.empty()
# placeholder1 = st.empty()

q_log = 0
# log_option = placeholder1.checkbox("Logarithic Axes Scaling")
# if log_option:
#     q_log = 1
if left_column.checkbox("Logarithic Axes Scaling"):
    q_log = 1

bin_sizes = sorted(range(2, 11, 2))
binning =right_column.selectbox("Choose bin size for binning of life expectancy: ", bin_sizes,index=0)

### merge dataframes
df_merged = pd.merge(left = df, right = data, left_on=['Code', 'Year'], right_on= ['iso_alpha', 'year'])
df_merged = df_merged[['country', 'Code', 'year', int_pop, 'lifeExp', 'pop', 'gdpPercap', 'continent']]
# binning = 2
df_merged['lifeExp_bin'] = df_merged['lifeExp'].apply(lambda x: (x//binning)*binning)

fig4 = make_subplots(rows = 1, cols = 4)
continents = df_merged['continent'].unique()
life_exp_bins = np.arange(40, 90, 2)
colors = plt.cm.winter_r(range(256))
colors = [mpl.colors.rgb2hex(c) for c in colors]

for k, year in enumerate(sorted(df_merged['year'].unique())):

    for i, lf_exp in enumerate(life_exp_bins):
        ds_aux = df_merged[(df_merged['lifeExp_bin'] == lf_exp) & (df_merged['year'] == year)]
        #print(ds_aux['pop'])

        fig4.add_trace(
            go.Scatter(
                x = ds_aux['gdpPercap'], y = ds_aux[int_pop],
                mode = "markers",
                name = str(lf_exp), 
                marker = {'color': colors[7*i], 'size': ds_aux['pop'].apply(lambda x: np.sqrt(x)), 'sizeref': 100, 'sizemode': 'area'},
                #marker={"size": ds_aux['pop'], "sizeref": 2*max(ds['pop'])/5000, "sizemode": "area"},
                text=ds_aux[['country', 'lifeExp', 'pop']],
                hovertemplate="<b>%{text[0]}:</b><br><br>" +
                    # "Internet usage: %{y:$,.0f}<br>" +
                    # "GDP per Capita: %{x:$,.0f}<br>" +
                    "Internet usage: %{y:,.0f}%<br>" +
                    "GDP per Capita: $%{x}<br>" +
                    "Life Expectation: %{text[1]}<br>" +
                    "Population: %{text[2]}" +
                    "<extra></extra>"
            ), row=1, col=k+1
        )

# Remove tick labels from the second, third, and fourth plots
for i in range(2, 5):  # Columns 2, 3, and 4
    # fig4.update_xaxes(showticklabels=False, row=1, col=i)
    fig4.update_yaxes(showticklabels=False, row=1, col=i)
# q_log = 1
if q_log == 1:
    fig4.update_yaxes(type="log", range=[-4.5, 2.2])
    fig4.update_xaxes(type="log", range=[2.2, 5])
else:
    fig4.update_yaxes(range=[-10, 100])
    fig4.update_xaxes(range=[-5000, 55000])
    None

fig4.update_layout(
    #title={"text": "Internet usage vs GDP per Capita", "font": {"size": 24}},
    yaxis1={"title": {"text": "Internet usage (per cent)", "font": {"size": 16}}},
    # yaxis2={showticklabels=False}, 
    # yaxis3={"ticktext": [], "tickangle": 0}, 
    # yaxis4={#"tickvals": [], 
    #     "ticktext": [], "tickangle": 0}, 
    xaxis1={"title": {"text": "1992", "font": {"size": 16}}},
    xaxis2={"title": {"text": "1997", "font": {"size": 16}}},
    xaxis3={"title": {"text": "2002", "font": {"size": 16}}},
    xaxis4={"title": {"text": "2007", "font": {"size": 16}}},
)



st.plotly_chart(fig4)





