# import pandas as pd
# from Load_data import Load_data

# df = Load_data.loaddata()

# print(df.info())








# Fun little stupid graph. will remove later.

# # Get all rows where a player managed to score a medal
# olympic_data_with_medals = olympic_data[olympic_data['Medal'].notna()]

# sports = ['Basketball', 'Football', 'Ice Hockey']

# f = {}

# for sport in sports:

#     olympic_data_sport_with_medals = olympic_data_with_medals.drop(olympic_data_with_medals[olympic_data_with_medals['Sport'] != sport].index)

#     medals_across_countries_sport = olympic_data_sport_with_medals.groupby('NOC')['Medal'].value_counts()

#     #Group each game and sum the medal types (e.g bronze, silver & gold) for each given game 
#     medals_per_country_sport = medals_across_countries_sport.groupby('NOC').sum()

#     #Sort index, so we can display the games in order of year
#     medals_per_country_sport = medals_per_country_sport.sort_values(ascending=False)
    
#     f[sport] = medals_per_country_sport  # new key, so add

# f


# g = pd.DataFrame(f)
# g = g.sort_values('Basketball')


# barfig = px.bar(
#     x=g.index,
#     y=[g['Basketball'], g['Football'], g['Ice Hockey']],
#     barmode='group',
#     title="Medal distribution across countries in basketball",
#     labels={
#         'x': '',
#         'y': 'Medals'
#     }
# )

# barfig.show()