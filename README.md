
# Movie Recommendation System using NLP

A content based Recommendation engine for movies using cosine similarity score.
 


## Dataset

 - [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


## API Reference

#### Get movie details

```http
  GET https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `movie_id` | `int` | **Required**. ID of the movie |
| `api_key` | `string` | **Required**. Your API key |





## Documentation

- [Streamlit](https://docs.streamlit.io/)
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)


