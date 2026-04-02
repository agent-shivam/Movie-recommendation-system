import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

import os

class MovieRecommender:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        self.index = faiss.read_index(
            os.path.join(BASE_DIR, "models", "faiss_index.bin")
        )

        self.df = pd.read_csv(
            os.path.join(BASE_DIR, "models", "movies.csv")
        )

    def recommend(self, query, k=5):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec), k)
        return self.df.iloc[I[0]]['title'].tolist()