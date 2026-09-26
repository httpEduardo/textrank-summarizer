# Textrank Summarizer

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)

Textrank Summarizer summarizes long text using a TextRank-style graph algorithm. It ranks sentences and returns the most representative ones.

## Quick start

```bash
python -m textrank_summarizer.server --port 5173
```

Open http://localhost:5173

## API

- POST `/api/summarize` `{ "text": "", "ratio": 0.3 }`

