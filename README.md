
# SAR + LLM Viewer

App full-stack para visualizar imágenes SAR y obtener descripciones en lenguaje natural con ayuda de un modelo multimodal como GPT-4o.

## 🧠 Requisitos

- Python 3.11+
- Node.js 18+
- Cuenta de OpenAI con acceso a GPT-4o (si se usa API)

## 🚀 Cómo usar

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Luego abre http://localhost:5173 y sube una imagen SAR (GeoTIFF o PNG en escala de grises).
