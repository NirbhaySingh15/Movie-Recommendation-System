import streamlit as st
import pickle
import pandas as pd
import requests


similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d0f741027b5e6d1e9caa4b80ddcc881f&language=en-US'.format(movie_id))
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #runtime=data['runtime']
    return full_path

def fetch_overview(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d0f741027b5e6d1e9caa4b80ddcc881f&language=en-US'.format(movie_id))
    data=response.json()
    overview=data['overview']
    return overview

def fetch_runtime(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d0f741027b5e6d1e9caa4b80ddcc881f&language=en-US'.format(movie_id))
    data=response.json()
    runtime=data['runtime']
    return runtime

def fetch_rating(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d0f741027b5e6d1e9caa4b80ddcc881f&language=en-US'.format(movie_id))
    data=response.json()
    rating=data['vote_average']
    return rating

def fetch_link(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d0f741027b5e6d1e9caa4b80ddcc881f&language=en-US'.format(movie_id))
    data=response.json()
    link=data['homepage']
    return link


def recommend(movie):
    # movie index
    movie_index = movies[movies['title'] == movie].index[0]
    # similer movies distance
    distances = similarity[movie_index]
    # we have to sort the distance to find the nearest vectors
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies=[]
    recommended_movies_poster=[]
    recommended_movies_overview=[]
    recommended_movies_runtime = []
    recommended_movies_rating = []
    recommended_movies_link=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        #movie title
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
        # fetch overview from api
        recommended_movies_overview.append(fetch_overview(movie_id))
        # fetch runtime from api
        recommended_movies_runtime.append(fetch_runtime(movie_id))
        # fetch rating from api
        recommended_movies_rating.append(fetch_rating(movie_id))
        # fetch rating from api
        recommended_movies_link.append(fetch_link(movie_id))
    return recommended_movies, recommended_movies_poster, recommended_movies_overview,recommended_movies_runtime,recommended_movies_rating, recommended_movies_link



#st.title("Movie Recommender System")
st.markdown("<h1 style='text-align: center; color: dark;'>MOVIE RECOMMENDER SYSTEM</h1>", unsafe_allow_html=True)

#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)


#st.title("Movie Recommender System")
selected_movie_name=st.selectbox("SELECT MOVIE FOR MORE RECOMMENDATION",movies['title'].values)

if st.button('SEARCH'):
    names,posters,overview,runtime,rating,url = recommend(selected_movie_name)
    # FIRST COLUMN
    a = [col1, col2, col3, col4, col5] = st.columns(5)
    b = 0
    for i in a:
        with i:
            st.subheader(names[b])
            st.image(posters[b])
            st.write('###### IMDB: ', round(rating[b], 1), 'RUN TIME : ', runtime[b])
            st.write('<t style="font-size:15px; color:red;">OVERVIEW: </t>', overview[b], unsafe_allow_html=True)
        b += 1
    # SECOND COLUMN
    a = [col6, col7, col8, col9, col10] = st.columns(5)
    b = 5
    for i in a:
        with i:
            st.subheader(names[b])
            st.image(posters[b])
            st.write('###### IMDB: ', round(rating[b], 1), 'RUN TIME : ', runtime[b])
            st.write('<t style="font-size:15px; color:red;">OVERVIEW: </t>', overview[b], unsafe_allow_html=True)
        b += 1
    #first column
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.subheader(names[0])
    #     st.image(posters[0])
    #     st.write('IMDB: ',round(rating[0],1),'RUN TIME : ',runtime[0])
    #     st.write('OVERVIEW: ',overview[0])
    # with col2:
    #     st.subheader(names[1])
    #     st.image(posters[1])
    #     st.write('IMDB: ', round(rating[1],1), 'RUN TIME : ', runtime[1])
    #     st.write('OVERVIEW: ', overview[1])
    # with col3:
    #     st.subheader(names[2])
    #     st.image(posters[2])
    #     st.write('IMDB: ', round(rating[2],1), 'RUN TIME : ', runtime[2])
    #     st.write('OVERVIEW: ', overview[2])
    # with col4:
    #     st.subheader(names[3])
    #     st.image(posters[3])
    #     st.write('IMDB: ', round(rating[3],1), 'RUN TIME : ', runtime[3])
    #     st.write('OVERVIEW: ', overview[3])
    # with col5:
    #     st.subheader(names[4])
    #     st.image(posters[4])
    #     st.write('IMDB: ', round(rating[4],1), 'RUN TIME : ', runtime[4])
    #     st.write('OVERVIEW: ', overview[4])


    #second column
    # col6, col7, col8, col9, col10 = st.columns(5)
    # with col6:
    #     st.subheader(names[5])
    #     st.image(posters[5])
    #     st.write('IMDB: ',round(rating[5],1),'RUN TIME : ',runtime[5])
    #     st.write('OVERVIEW: ',overview[5])
    # with col7:
    #     st.subheader(names[6])
    #     st.image(posters[6])
    #     st.write('IMDB: ', round(rating[6],1), 'RUN TIME : ', runtime[6])
    #     st.write('OVERVIEW: ', overview[6])
    # with col8:
    #     st.subheader(names[7])
    #     st.image(posters[7])
    #     st.write('IMDB: ', round(rating[7],1), 'RUN TIME : ', runtime[7])
    #     st.write('OVERVIEW: ', overview[7])
    # with col9:
    #     st.subheader(names[8])
    #     st.image(posters[8])
    #     st.write('IMDB: ', round(rating[8],1), 'RUN TIME : ', runtime[8])
    #     st.write('OVERVIEW: ', overview[8])
    # with col10:
    #     st.subheader(names[9])
    #     st.image(posters[9])
    #     st.write('IMDB: ', round(rating[9],1), 'RUN TIME : ', runtime[9])
    #     st.write('OVERVIEW: ', overview[9])


    # #FIRST COLUMN
    # a=[col1,col2,col3,col4 ,col5]=st.columns(5)
    # b=0
    # for i in a:
    #     with i:
    #         st.subheader(names[b])
    #         st.image(posters[b])
    #         st.write('###### IMDB: ', round(rating[b], 1), 'RUN TIME : ', runtime[b])
    #         st.write('<t style="font-size:15px; color:red;">OVERVIEW: </t>',overview[b],unsafe_allow_html=True)
    #     b+=1
    #
    # #SECOND COLUMN
    # a=[col6, col7, col8, col9, col10] = st.columns(5)
    # b = 5
    # for i in a:
    #     with i:
    #         st.subheader(names[b])
    #         st.image(posters[b])
    #         st.write('###### IMDB: ', round(rating[b], 1), 'RUN TIME : ', runtime[b])
    #         st.write('<t style="font-size:15px; color:red;">OVERVIEW: </t>',overview[b],unsafe_allow_html=True)
    #     b += 1
