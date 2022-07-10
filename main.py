import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
my_df = pd.read_csv('C:\\Users\\asus\\Downloads\\pydictionary-master\\u.data', sep='\t', names=['user_id','item_id','rating','timestamp'])
print(my_df.head())

movie_titles = pd.read_csv('C:\\Users\\asus\\Downloads\\pydictionary-master\\Movie_Titles.csv', encoding= 'unicode_escape')
my_df = pd.merge(my_df, movie_titles, on='item_id')
print(my_df.head())
print(my_df.describe())

ratings = pd.DataFrame(my_df.groupby('title')['rating'].mean())
print(ratings.head())

ratings['number_of_ratings'] = my_df.groupby('title')['rating'].count()
print(ratings.head())



sns.jointplot(x='rating', y='number_of_ratings', data=ratings, color = "r")
plt.show()

movie_matrix_UII = my_df.pivot_table(index='user_id', columns='title', values='rating')
print(movie_matrix_UII.head())
print(ratings.sort_values('number_of_ratings', ascending=False).head(10))

Fargo_user_rating = movie_matrix_UII['Fargo (1996)']
similar_to_fargo=movie_matrix_UII.corrwith(Fargo_user_rating)
print(similar_to_fargo.head())

corr_fargo = pd.DataFrame(similar_to_fargo, columns=['Correlation'])
corr_fargo.dropna(inplace=True)
print(corr_fargo.head())

corr_fargo = corr_fargo.join(ratings['number_of_ratings'])
print(corr_fargo.head())

print(corr_fargo[corr_fargo['number_of_ratings'] > 30].sort_values(by='Correlation', ascending=False).head(10))

print('Split of movies count based on their overall average rating')
labels = '5 star', '4 to 5 star', '3 to 4 star', '2 to 3 star', '1 to 2 star'
sizes = [10, 163, 871, 492, 128]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()