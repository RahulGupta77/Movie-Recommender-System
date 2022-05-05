# **Movie-Recommender-System**

---

## Site Link 
   - [Click here](https://rahuls-movie-recommender.herokuapp.com/)
---
## Demo
 
![git_movie](https://user-images.githubusercontent.com/63935255/166870689-7e328941-9fe5-468e-91d4-e6d8a9dbfabc.gif)

---
## Tech Stack used 

   - Python
   - Streamlit (for frontend)
   - Heroku (for hosting)
---
## Libraries used 
   - Scikit Learn
   - Natural Language Toolkit 
   - Pickle
   - Pandas 
   - Numpy
---
## Project Description

   - This is a movie recommendor system which is based on *Content based filtering* meaning it uses similarities in a movie such as movie genres, tags,          cast, crew, overview as well as information provided by user to make recommendations. 
   - Content-based filtering makes recommendations by using keywords and attributes assigned to a movie. 
---

## Project Procedure 

1. **Data collection and cleaning** : I used this [dataset](https://www.kaggle.com/code/erikbruin/movie-recommendation-systems-for-tmdb/data) for the project. Did some data cleaning like finding any missing, duplicate data. I took only relevant columns like genres, id, keywords, title, overview, cast, crew from the dataset.
 
2. **Data preprocessing** : I did data *transformation* to get rid of single entities like getting rid of spaces between the names of cast/crew. Used *Stemming technique* to remove similar wordings eg. 'eat' , 'eating'. The stemming process was done with the help of NLTK library. Formed a *Corpose* of each movie containing it's title, genres, casts, crew, etc. 

3. **Text Vectorization** : Performed Vectorization with the help of Scikit-learn and used **Bag of  words** technique to find out the frequency of each word in each corpose. 

4. **Cosine Similarity** : I used cosine similarity technique to find out how similar the selected movie is compared to rest of the movies. Then defined a function which returns top five movies which are similar to the selected movie. 

5. **Streamlit** : Made a frontend using streamlit that has a *navbar* which contains movie name, a user can type or scroll to find their desired movie. There is a recommend button which recommends similar movies. 

6. **The Movie Dataset (TMDB) API** : I used this API to fetch the posters of each movie using it's unique id which is assigned to every movie. You can see the poster of selected movie as well as of the recommended movies. 

7. **Heroku** : Lastly pushed everything on to Heroku and hosted it. 

--- 



