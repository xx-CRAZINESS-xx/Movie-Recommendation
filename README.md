
# Movie Recommendation System

At some point each one of us must have wondered where all the recommendations that Netflix, Amazon, Google give us, come from. We often rate products on the internet and all the preferences we express and data we share (explicitly or not), are used by recommender systems to generate, in fact, recommendations.

It turns out that there are (mostly) three ways to build a recommendation engine
- Collaborative filtering
- Content-Based Filtering
- Hybrid Recommendation Systems

Here I used content based recommendation engine

## Data collection

The data was scraped from IMDb, in which 6000+ movies were collected based on release date from 2000-2021 and number of votes.

https://www.imdb.com/search/title/?title_type=feature&year=2000-01-01,2021-12-31&sort=num_votes,desc&start=0&ref_=adv_nxt


The features used are id,title,genre,director,stars,overview,rating and votes

## Model building

- Cleaned the data using regex
- Joined genre,director,stars and overview and created a new feature called combined which was lemmatized using WordNetLemmatizer
- Used TfidfVectorizer to transform the data(combined) into vectors
- Finally used cosine similarity to calculate the similarity score of the movies 




### How cosine similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Movie-Recommendation/blob/main/images/cosine.png)



## Deployment

- Here I used streamlit to create a web app which was deployed on heroku

- To get the poster of the recommended movies, used TMDB api 

https://movie---recommendation.herokuapp.com/

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Movie-Recommendation/blob/main/images/shot.png?raw=true "Title")


**If you are not getting the web app just like the above image then you have to change the streamlit theme**

- Click <span>&#8801;</span> on the top right corner
- Settings > Theme > Dark







## Run Locally

Clone the project

```bash
  git clone https://github.com/xx-CRAZINESS-xx/Movie-Recommendation.git
```

Go to the project directory

```bash
  cd Movie-Recommendation
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

