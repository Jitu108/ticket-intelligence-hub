# infrastructure/embeddings.py
from abc import ABC, abstractmethod
import numpy as np

class EmbeddingStrategy(ABC):
    @abstractmethod
    def embed(self, text:str) -> np.ndarray: ...

class OpenAIEmbedding(EmbeddingStrategy):
    def __init__(self, model:str): self.model = model
    def embed(self, text:str)->np.ndarray:
        # return np.array([...], dtype=np.float32)
        ...

class LocalEmbedding(EmbeddingStrategy):
    def __init__(self, model:str): self.model = model
    def embed(self, text:str)->np.ndarray: ...