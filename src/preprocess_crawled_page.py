import nltk
from nltk.tokenize import PunktSentenceTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
import networkx as nx
from nltk.cluster.util import cosine_distance


# Ensure NLTK packages are downloaded
nltk.download("punkt")
nltk.download("stopwords")

punkt_tokenizer = PunktSentenceTokenizer()
tokenizer = RegexpTokenizer(r"\w+")


# Function to calculate sentence similarity
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in tokenizer.tokenize(sent1)]
    sent2 = [w.lower() for w in tokenizer.tokenize(sent2)]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # Create vectors for the sentences
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    # Check for zero vectors to avoid division by zero
    if np.all(vector1 == 0) or np.all(vector2 == 0):
        return 0.0

    return 1 - cosine_distance(vector1, vector2)


# Function to preprocess crawled page
def preprocess_crawled_page(text):
    sentences = punkt_tokenizer.tokenize(text)

    # Creating a similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # Ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                sentences[idx1], sentences[idx2], stopwords.words("english")
            )

    # Applying PageRank algorithm
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)

    # Applying PageRank algorithm with error handling
    try:
        scores = nx.pagerank(sentence_similarity_graph, max_iter=500)
    except nx.PowerIterationFailedConvergence:
        # Handle convergence error, e.g., by using a default value
        scores = {i: 1.0 / len(sentences) for i in range(len(sentences))}

    # Sorting sentences
    ranked_sentence = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True
    )

    # Extracting top sentences as the summary within the 3800 token limit
    summary = []
    token_count = 0
    for score, sentence in ranked_sentence:
        sentence_tokens = tokenizer.tokenize(sentence)
        if token_count + len(sentence_tokens) > 1000:
            break
        summary.append(sentence)
        token_count += len(sentence_tokens)
    return " ".join(summary)
