# SummitScribe

SummitScribe summarizes long text using a TextRank-style graph algorithm. It ranks sentences and returns the most representative ones.

## Quick start

```bash
python -m app.server --port 5173
```

Open http://localhost:5173

## API

- POST `/api/summarize` `{ "text": "", "ratio": 0.3 }`

