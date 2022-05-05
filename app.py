import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1007d87a6b0488703f2c63636372dde7&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetching posters from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        # fetching movies from the algorithm
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

st.subheader("Search a movie")
selected_movie_name = st.selectbox("Choose here:",
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    searched_movie = selected_movie_name
    searched_movie_index = movies[movies['title'] == searched_movie].index[0]
    searched_movie_id = movies.iloc[searched_movie_index].movie_id
    searched_movie_poster = fetch_poster(searched_movie_id)
    st.text("")
    st.subheader("Your searched movie is: ")
    st.text(selected_movie_name)
    col_main, col_d, col_e = st.columns(3)
    with col_main:
        st.image(searched_movie_poster)
    with col_d:
        pass
    with col_e:
        pass

    st.text("")
    st.text("")
    st.subheader("Your recommended movies are: ")

    col1, col2, col3= st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    st.write(" ")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col6:
        st.text(names[5])
        st.image(posters[5])