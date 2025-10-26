# application/pipelines.py
from ..infrastructure.llm import BaseLLM
from ..infrastructure.embedding import EmbeddingStrategy
import numpy as np

class SimilarityPipeline:
    def __init__(self, embedder: EmbeddingStrategy):
        self.embedder = embedder
    @staticmethod
    def cosine(a:np.ndarray,b:np.ndarray)->float:
        return float(a @ b / (np.linalg.norm(a)*np.linalg.norm(b) + 1e-9))
    # add: load stored vectors from DB and compute top-k