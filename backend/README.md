# 🔧 DreamVision AI - Backend

FastAPI backend with Supabase integration.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Supabase account
- API keys (Anthropic, Runway)

### Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (coming in next task)
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run server (coming in next task)
uvicorn app.main:app --reload
```

## 📚 Documentation

See [SUPABASE-SETUP.md](../docs/SUPABASE-SETUP.md) for database schema.

## 🗄️ Database

**Supabase PostgreSQL**
- 3 tables: user_profiles, dreams, videos
- Row Level Security enabled
- Auto-triggers for stats

## 🔐 Authentication

Supabase Auth with JWT tokens.

## 📦 Storage

Supabase Storage for video thumbnails.

---

**Status:** Epic 2.1 Complete ✅  
**Next:** Epic 2.2 - FastAPI Project Setup