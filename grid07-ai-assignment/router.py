from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Bot personas
personas = {
    "bot_A": "I believe AI and crypto will solve all human problems. I am optimistic about Elon Musk and space.",
    "bot_B": "I think tech monopolies are dangerous. I care about privacy, nature and criticize AI.",
    "bot_C": "I focus on markets, trading, ROI, and financial growth.",
}

# Create embeddings
persona_texts = list(personas.values())
persona_embeddings = model.encode(persona_texts)

# FAISS index
dimension = persona_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(persona_embeddings))


def route_post_to_bots(post_content, threshold=0.85):
    post_embedding = model.encode([post_content])

    D, I = index.search(np.array(post_embedding), k=3)

    matched_bots = []

    for idx, dist in zip(I[0], D[0]):
        similarity = 1 / (1 + dist)  # convert distance -> similarity

        if similarity > threshold:
            bot_id = list(personas.keys())[idx]
            matched_bots.append(bot_id)

    return matched_bots
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Bot personas
personas = {
    "bot_A": "I believe AI and crypto will solve all human problems. I am optimistic about Elon Musk and space.",
    "bot_B": "I think tech monopolies are dangerous. I care about privacy, nature and criticize AI.",
    "bot_C": "I focus on markets, trading, ROI, and financial growth.",
}

# Create embeddings
persona_texts = list(personas.values())
persona_embeddings = model.encode(persona_texts)

# FAISS index
dimension = persona_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(persona_embeddings))


def route_post_to_bots(post_content, threshold=0.85):
    post_embedding = model.encode([post_content])

    D, I = index.search(np.array(post_embedding), k=3)

    matched_bots = []

    for idx, dist in zip(I[0], D[0]):
        similarity = 1 / (1 + dist)  # convert distance -> similarity

        if similarity > threshold:
            bot_id = list(personas.keys())[idx]
            matched_bots.append(bot_id)

    return matched_bots
