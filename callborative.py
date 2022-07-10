import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


overall_stats = pd.read_csv('C:\\Users\\asus\\Downloads\\pydictionary-master\\u.data', header=None)
column_names1 = ['user id','movie id','rating','timestamp']
dataset = pd.read_csv('C:\\Users\\asus\\Downloads\\pydictionary-master\\u.data', sep='\t',header=None,names=column_names1)
print(dataset.head())
print(len(dataset), max(dataset['movie id']),min(dataset['movie id']))
d = 'movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western'
column_names2 = d.split(' | ')
print(column_names2)

items_dataset = pd.read_csv('C:\\Users\\asus\\Downloads\\pydictionary-master\\Movie_Titles.csv', sep='|',header=None,names=column_names2,encoding='latin-1')
print(items_dataset)

movie_dataset = items_dataset[['movie id','movie title']]
print(movie_dataset.head())

print('Split of movies count based on their overall average rating')
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '5 star', '4 to 5 star', '3 to 4 star', '2 to 3 star', '1 to 2 star'
sizes = [10, 163, 871, 492, 128]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


