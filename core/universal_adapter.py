# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import hashlib
import numpy as np

class UniversalAdapter:
    """
    The 'Bouche' of the System.
    Transforms any input 'x' (Text, Number, Code, Pattern) into a Latent Vector.
    """
    def __init__(self, embedding_dim=64):
        self.embedding_dim = embedding_dim

    def adapt(self, input_data):
        """
        Detects type of input and returns a normalized Tensor.
        """
        if isinstance(input_data, str):
            return self._text_to_vector(input_data)
        elif isinstance(input_data, (int, float)):
            return self._number_to_vector(input_data)
        elif isinstance(input_data, list):
            # Recurse or treat as vector
            if all(isinstance(i, (int, float)) for i in input_data):
                return self._vector_to_tensor(input_data)
            else:
                # Aggregate complex list
                vectors = [self.adapt(i) for i in input_data]
                return torch.mean(torch.stack(vectors), dim=0)
        elif isinstance(input_data, np.ndarray):
             return torch.tensor(input_data, dtype=torch.float32)
        elif isinstance(input_data, torch.Tensor):
            return input_data.float()
        else:
            # Fallback for unknown objects (bytes, files)
            return self._object_to_vector(input_data)

    def _text_to_vector(self, text):
        # Deterministic Chaos Hash Projection
        # Logic: Text -> SHA256 -> Integers -> Vector -> Normalize
        hash_obj = hashlib.sha256(text.encode('utf-8'))
        hex_dig = hash_obj.hexdigest()
        
        # Split hash into chunks to form vector
        # SHA256 is 64 hex chars. 
        # We want embedding_dim. We reuse/cycle the hash.
        vector = []
        for i in range(self.embedding_dim):
            start = (i * 2) % len(hex_dig)
            chunk = hex_dig[start:start+2]
            val = int(chunk, 16)
            vector.append(val)
            
        t = torch.tensor(vector, dtype=torch.float32)
        return (t - 128.0) / 128.0 # Normalize -1 to 1

    def _number_to_vector(self, number):
        # A code is a frequency in the void.
        # We project it across dimensions using frequencies.
        t = torch.arange(self.embedding_dim, dtype=torch.float32)
        return torch.sin(t * number)

    def _vector_to_tensor(self, vec):
        t = torch.tensor(vec, dtype=torch.float32)
        # Pad or Crop to match embedding_dim
        if len(t) < self.embedding_dim:
            pad = torch.zeros(self.embedding_dim - len(t))
            t = torch.cat([t, pad])
        elif len(t) > self.embedding_dim:
            t = t[:self.embedding_dim]
        return t

    def _object_to_vector(self, obj):
        return self._text_to_vector(str(obj))
