import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import json

pd.set_option('display.max_columns', None)

def fetch_poster(api_key, movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US')
    movie_data = response.json()
    poster_path = f'https://image.tmdb.org/t/p/w185' + movie_data['poster_path']
    return poster_path

def recommender(movie_name):
    movie_df_index = final_data[final_data.title == movie_name].index[0]
    recommended_movies_list = []
    recommended_movies_posters_path_list = []
    for x in sorted(similarity[movie_df_index], reverse=True)[1:6]:
        i = np.where(similarity[movie_df_index] == x)
        recommended_movies_list.append(final_data.iloc[i].title.values[0])
        recommended_movies_posters_path_list.append(fetch_poster(api_key, final_data.iloc[i].movie_id.values[0]))
    return recommended_movies_list, recommended_movies_posters_path_list

# API Key
api_key = 'c0fd2b595b2a29d36f91cf3569988415'

# Read the final dataframe
final_data = pd.read_csv('final_data.csv')

# Read cosine similarity multidimensional array
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

movie_name = st.selectbox(
    'Search for your movie below',
    final_data.title)

if st.button('Recommend'):
    names, posters = recommender(movie_name)
    movie1, movie2, movie3, movie4, movie5 = st.columns(5)
    with movie1:
       st.text(names[0])
       st.image(posters[0])

    with movie2:
        st.text(names[1])
        st.image(posters[1])

    with movie3:
        st.text(names[2])
        st.image(posters[2])

    with movie4:
        st.text(names[3])
        st.image(posters[3])

    with movie5:
        st.text(names[4])
        st.image(posters[4])