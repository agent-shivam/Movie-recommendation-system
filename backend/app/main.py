from fastapi import FastAPI
from app.recommender import MovieRecommender

app = FastAPI()
recommender = MovieRecommender()

@app.get("/")
def home():
    return {"message": "Movie Recommender API Running 🚀"}

@app.get("/recommend")
def recommend(query: str):
    results = recommender.recommend(query)
    return {"recommendations": results}