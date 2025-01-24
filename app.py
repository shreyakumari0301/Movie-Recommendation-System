
import pandas as pd
import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')

# Function to get movie posters
def recommend_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', None)
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error+Loading+Poster"

# Recommendation system logic
def recommend_sys(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"], ["https://via.placeholder.com/500x750?text=No+Recommendations"]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    rec_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_posters.append(recommend_poster(movie_id))
    return rec_movies, rec_posters

# Load data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set Streamlit configuration with dark mode
st.set_page_config(page_title="🎥 Movie Recommendation System", page_icon="🎬", layout="wide")

# Custom CSS for dark mode and styling
st.markdown("""
    <style>
        .stApp {
            background-color: #121212;
            color: #e0e0e0;
        }
        h1, h3, h4 {
            color: #00adb5;
        }
        /* Dropdown size and styling */
        .stSelectbox > div > div > div {
            background-color: #333333;
            color: #e0e0e0;
            border-radius: 8px;
            font-size: 16px; /* Increased font size */
        }
        /* Button styling */
        .stButton button {
            background-color: #00adb5;
            color: #121212;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            padding: 0.5rem 1rem;
            margin-top: 15px; /* Align button vertically with dropdown */
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #007f80;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎥 Movie Recommendation System")

# Dropdown and button on the same line
col1, col2 = st.columns([3, 1])  # Adjust column widths

with col1:
    choice = st.selectbox('🎬 Select a movie to get recommendations:', movies['title'].values)

with col2:
    show_recommendations = st.button('Show Recommendations 🎬')

# Recommendation button and display
if show_recommendations:
    rec_movies, rec_posters = recommend_sys(choice)

    st.markdown("### Recommended Movies:")
    st.markdown("---")

    # Display recommendations
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            if i < len(rec_movies):
                st.markdown(f"""
                    <div style="background-color:#1e1e1e; padding:10px; border-radius:8px; text-align:center; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.2);">
                        <img src="{rec_posters[i]}" style="width:100%; border-radius:8px;">
                        <h4 style="color:#e0e0e0;">{rec_movies[i]}</h4>
                    </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<footer style="text-align: center; font-size: 14px; color: #888888;">
    Created with ❤️ using Streamlit | Powered by TMDb API
</footer>
""", unsafe_allow_html=True)

# import pandas as pd
# import streamlit as st
# import pickle
# import requests
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# # API key stored securely
# API_KEY = os.getenv('TMDB_API_KEY')
#
# def recommend_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#         data = requests.get(url).json()
#         poster_path = data.get('poster_path', None)
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         else:
#             return "https://via.placeholder.com/500x750?text=No+Poster+Available"
#     except Exception as e:
#         return "https://via.placeholder.com/500x750?text=Error+Loading+Poster"
#
# def recommend_sys(movie):
#     if movie not in movies['title'].values:
#         return ["Movie not found"], ["https://via.placeholder.com/500x750?text=No+Recommendations"]
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     rec_movies = []
#     rec_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         rec_movies.append(movies.iloc[i[0]].title)
#         rec_posters.append(recommend_poster(movie_id))
#     return rec_movies, rec_posters
#
# # Load data
# movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Streamlit UI
# st.title('🎥 Movie Recommendation System')
#
# choice = st.selectbox('Select a movie:', movies['title'].values)
#
# if st.button('Show Recommendation'):
#     rec_movies, rec_posters = recommend_sys(choice)
#     cols = st.columns(5)
#     for i, col in enumerate(cols):
#         with col:
#             if i < len(rec_movies):
#                 st.text(rec_movies[i])
#                 st.image(rec_posters[i])
#
#
#
#
#
