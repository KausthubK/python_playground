import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
    
    def add(self, emb, ids):
        self.index.add(np.array(emb))
    
    def search(self, query_embedding, num_nearest_neighbours: int = 10) -> tuple[list[float], list[int]]:
        """Search for relevant documents based on a query"""
        distances, indices = self.index.search(np.array([query_embedding]), k = num_nearest_neighbours)
        return distances, indices