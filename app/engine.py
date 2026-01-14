import math
import re
from collections import Counter

TOKEN_RE = re.compile(r"[a-z0-9]+")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]")


def tokenize(text):
    return TOKEN_RE.findall(text.lower())


def split_sentences(text):
    sentences = [s.strip() for s in SENTENCE_RE.findall(text)]
    if not sentences:
        sentences = [text.strip()] if text.strip() else []
    return sentences


def similarity(a_tokens, b_tokens):
    if not a_tokens or not b_tokens:
        return 0.0
    overlap = len(set(a_tokens) & set(b_tokens))
    denom = math.log(len(a_tokens) + 1) + math.log(len(b_tokens) + 1)
    return overlap / denom if denom else 0.0


def summarize(text, ratio=0.3):
    sentences = split_sentences(text)
    if not sentences:
        return ""
    tokens = [tokenize(sentence) for sentence in sentences]
    n = len(sentences)
    scores = [1.0 / n] * n
    damping = 0.85

    weights = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                weights[i][j] = similarity(tokens[i], tokens[j])

    for _ in range(20):
        new_scores = [0.0] * n
        for i in range(n):
            rank = 0.0
            for j in range(n):
                if weights[j][i] == 0:
                    continue
                outbound = sum(weights[j]) or 1.0
                rank += scores[j] * (weights[j][i] / outbound)
            new_scores[i] = (1 - damping) / n + damping * rank
        scores = new_scores

    count = max(1, int(n * ratio))
    top_indices = sorted(range(n), key=lambda i: scores[i], reverse=True)[:count]
    top_indices.sort()
    return " ".join(sentences[i] for i in top_indices)
