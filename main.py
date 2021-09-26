import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommander System')
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
selected_movie = st.selectbox('Enter Movie Name',movies['title'].values)
def fecth_poster(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a63d8464949c3121299179baf66ea283'.format(id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_poster=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id
        recommended_poster.append(fecth_poster(movies_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_poster
if st.button('Recommend'):
    recommendation_movies,recommendation_poster=recommend(selected_movie)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendation_movies[0])
        st.image(recommendation_poster[0])
    with col2:
        st.text(recommendation_movies[1])
        st.image(recommendation_poster[1])
    with col3:
        st.text(recommendation_movies[2])
        st.image(recommendation_poster[2])
    with col4:
        st.text(recommendation_movies[3])
        st.image(recommendation_poster[3])
    with col5:
        st.text(recommendation_movies[4])
        st.image(recommendation_poster[4])