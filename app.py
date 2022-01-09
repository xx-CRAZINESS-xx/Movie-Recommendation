import joblib
import streamlit as st
import httpx
from utils import img_to_bytes,local_css


# @st.cache(allow_output_mutation=True)
@st.experimental_memo(persist="disk")
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    request = httpx.get(url)
    data = request.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# @st.cache(allow_output_mutation=True)
@st.experimental_memo(persist="disk")
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_rating=[]
    recommended_movie_votes=[]
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_rating.append(movies.iloc[i[0]].rating)
        recommended_movie_votes.append(movies.iloc[i[0]].votes)



    return recommended_movie_names,recommended_movie_posters,recommended_movie_rating,recommended_movie_votes


header_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='max-height: 255px; margin-left: 965px;margin-top: -62px; margin-bottom: -34px;'>".format(
    img_to_bytes("images/logo.png"))

st.markdown(
    header_html, unsafe_allow_html=True)

local_css("images/style.css")

movies = joblib.load('movies_list.sav')
similarity = joblib.load('similarity.sav')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_rating,recommended_movie_votes= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        (st.image(recommended_movie_posters[0]))
        st.write("{}/10".format(recommended_movie_rating[0]),'''
        <span>&#11088;</span>
        ''',unsafe_allow_html=True)
        st.write("{:,}".format(recommended_movie_votes[0]),'''
        <span>&#128077;</span>
        ''',unsafe_allow_html=True)


    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.write("{}/10".format(recommended_movie_rating[1]),'''
        <span>&#11088;</span>
        ''',unsafe_allow_html=True)
        st.write("{:,}".format(recommended_movie_votes[1]),'''
        <span>&#128077;</span>
        ''',unsafe_allow_html=True)


    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.write("{}/10".format(recommended_movie_rating[2]),'''
        <span>&#11088;</span>
        ''',unsafe_allow_html=True)
        st.write("{:,}".format(recommended_movie_votes[2]),'''
        <span>&#128077;</span>
        ''',unsafe_allow_html=True)


    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.write("{}/10".format(recommended_movie_rating[3]),'''
        <span>&#11088;</span>
        ''',unsafe_allow_html=True)
        st.write("{:,}".format(recommended_movie_votes[3]),'''
        <span>&#128077;</span>
        ''',unsafe_allow_html=True)


    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.write("{}/10".format(recommended_movie_rating[4]),'''
        <span>&#11088;</span>
        ''',unsafe_allow_html=True)
        st.write("{:,}".format(recommended_movie_votes[4]),'''
        <span>&#128077;</span>
        ''',unsafe_allow_html=True)