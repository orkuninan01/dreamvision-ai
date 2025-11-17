# 🗺️ DreamVision AI - Portfolio Development Roadmap v2.0

## 📊 Project Overview

**Developer:** Solo (23, CS Graduate)  
**Goal:** Portfolio project + Google Play Store launch  
**Daily Time:** 5-6 hours  
**Timeline:** 6 weeks (Core MVP) + 2 weeks (Optional Advanced Features)  
**Target:** Production-ready mobile app with clean architecture

---

## 🎯 Project Status

**Current Phase:** Ready to start Phase 2 (Backend Development)  
**Progress:** Phase 1 complete (16.67%)

| Phase | Duration | Daily Hours | Total Hours | Status |
|-------|----------|-------------|-------------|--------|
| Phase 1: Prompt System ✅ | Week 0 | - | - | COMPLETED |
| Phase 2: Backend + Supabase | Week 1-2 | 5-6h | 60-72h | READY |
| Phase 3: Mobile App | Week 3-4 | 5-6h | 60-72h | PENDING |
| Phase 4: Integration & Polish | Week 5 | 5-6h | 30-36h | PENDING |
| Phase 5: Deployment | Week 6 | 5-6h | 30-36h | PENDING |
| **Core MVP Total** | **6 weeks** | **5-6h/day** | **~200h** | **0%** |
| Phase 6: Web PWA (Optional) | Week 7 | 5-6h | 30-36h | OPTIONAL |
| Phase 7: Analytics (Optional) | Week 8 | 5-6h | 30-36h | OPTIONAL |

---

## 🏗️ Updated Architecture

```
┌──────────────────┐
│   Mobile App     │
│ (React Native +  │
│  Expo)           │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐      ┌────────────────────┐
│   FastAPI        │─────▶│  Claude Sonnet 4.5 │
│   Backend        │      │  (Dream Analysis)  │
│   + REST API     │      └────────────────────┘
└────────┬─────────┘
         │                 ┌────────────────────┐
         ├────────────────▶│  Runway Gen-3      │
         │                 │  (Video Generation)│
         │                 └────────────────────┘
         ▼
┌──────────────────┐
│   Supabase       │
│   - PostgreSQL   │
│   - Auth (JWT)   │
│   - Real-time    │
│   - Storage      │
└──────────────────┘
```

---

## 🛠️ Tech Stack (Updated)

### Backend
- **Framework:** FastAPI (Python 3.11+)
- **API Style:** REST API (JSON)
- **Database:** Supabase (PostgreSQL 15)
- **Authentication:** Supabase Auth (JWT)
- **File Storage:** Supabase Storage (video thumbnails)
- **Deployment:** Railway (backend) + Supabase (cloud)

### AI Services
- **Dream Analysis:** Claude Sonnet 4.5 via Anthropic API
- **Video Generation:** Runway Gen-3 Alpha via REST API
- **Prompt System:** Minimal Dream Prompt System v2.0 (from Phase 1)

### Frontend
- **Framework:** React Native (Expo)
- **Language:** TypeScript
- **UI Library:** React Native Paper / NativeBase
- **Navigation:** React Navigation v6
- **State Management:** Zustand
- **HTTP Client:** Axios

### DevOps & Tools
- **Version Control:** Git + GitHub
- **CI/CD:** GitHub Actions
- **Containerization:** Docker + Docker Compose
- **Backend Deploy:** Railway
- **Mobile Build:** Expo EAS (Android + iOS)
- **Monitoring:** Sentry (error tracking)
- **API Documentation:** Swagger/OpenAPI (auto-generated)

### Development Tools
- **n8n:** Prompt testing only (not in production)
- **Postman/Insomnia:** API testing
- **Expo Go:** Mobile development & testing

---

## 📂 Repository Structure (Updated)

```
dreamvision-ai/
├── .github/
│   └── workflows/
│       ├── backend-ci.yml          # Backend CI/CD
│       └── mobile-build.yml        # Mobile build automation
│
├── docs/
│   ├── ROADMAP.md                  # This file
│   ├── API.md                      # API documentation
│   ├── SUPABASE-SETUP.md          # Supabase configuration guide
│   ├── DEPLOYMENT.md               # Deployment guide
│   ├── GOOGLE-PLAY.md              # Google Play submission guide
│   └── ARCHITECTURE.md             # System architecture details
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── config.py               # Configuration management
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── routes/
│   │   │       │   ├── auth.py     # Auth endpoints (Supabase)
│   │   │       │   ├── dreams.py   # Dream analysis endpoints
│   │   │       │   ├── videos.py   # Video generation endpoints
│   │   │       │   └── health.py   # Health check
│   │   │       └── dependencies.py # FastAPI dependencies
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── supabase.py        # Supabase client
│   │   │   └── security.py         # Security utilities
│   │   ├── models/                 # Pydantic models
│   │   │   ├── dream.py
│   │   │   ├── video.py
│   │   │   └── user.py
│   │   ├── services/               # Business logic
│   │   │   ├── claude_service.py   # Claude API integration
│   │   │   ├── runway_service.py   # Runway API integration
│   │   │   └── supabase_service.py # Supabase operations
│   │   └── utils/
│   │       ├── prompts.py          # Prompt templates
│   │       ├── validators.py
│   │       └── error_handlers.py
│   ├── tests/
│   │   ├── test_api/
│   │   └── test_services/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── mobile/
│   ├── src/
│   │   ├── api/
│   │   │   ├── client.ts           # Axios instance
│   │   │   ├── auth.ts             # Auth API calls
│   │   │   ├── dreams.ts           # Dream API calls
│   │   │   └── videos.ts           # Video API calls
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Input.tsx
│   │   │   │   ├── Card.tsx
│   │   │   │   └── Loading.tsx
│   │   │   └── dream/
│   │   │       ├── DreamCard.tsx
│   │   │       └── VideoPlayer.tsx
│   │   ├── screens/
│   │   │   ├── auth/
│   │   │   │   ├── WelcomeScreen.tsx
│   │   │   │   ├── LoginScreen.tsx
│   │   │   │   └── RegisterScreen.tsx
│   │   │   ├── HomeScreen.tsx
│   │   │   ├── DreamInputScreen.tsx
│   │   │   ├── VideoStatusScreen.tsx
│   │   │   ├── VideoPlayerScreen.tsx
│   │   │   ├── HistoryScreen.tsx
│   │   │   └── ProfileScreen.tsx
│   │   ├── navigation/
│   │   │   └── AppNavigator.tsx
│   │   ├── store/
│   │   │   ├── authStore.ts
│   │   │   └── dreamStore.ts
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   └── useDreams.ts
│   │   ├── types/
│   │   ├── utils/
│   │   └── constants/
│   │       └── theme.ts
│   ├── assets/
│   ├── app.json
│   ├── eas.json                    # EAS Build configuration
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
│
├── prompts/
│   ├── minimal-dream-system-v2.txt # Claude system prompt (from Phase 1)
│   └── templates/
│       ├── gothic.txt
│       ├── chase.txt
│       ├── flight.txt
│       ├── transformation.txt
│       ├── physics.txt
│       └── liminal.txt
│
├── scripts/
│   ├── setup-supabase.sh          # Supabase setup automation
│   └── deploy.sh                   # Deployment script
│
├── .gitignore
├── .env.example
├── docker-compose.yml              # Local development environment
├── LICENSE
└── README.md
```

---

# 📋 DETAILED ROADMAP

## ✅ PHASE 0: Preparation (COMPLETED)

### What We Have:
- ✅ GitHub repository created
- ✅ Project structure initialized
- ✅ Minimal Dream Prompt System v2.0
- ✅ 6 category templates
- ✅ Tested with n8n (prototype phase)
- ✅ Cost optimized ($0.011 per dream)
- ✅ Video quality: 9-9.5/10

---

## 🔄 PHASE 2: Backend Development (Week 1-2)

**Timeline:** 10-12 working days (60-72 hours)  
**Priority:** P0 (Critical Path)  
**Goal:** Production-ready REST API with Supabase integration

---

### Epic 2.1: Supabase Setup & Configuration

**Duration:** Day 1 (5-6 hours)  
**Priority:** P0

#### User Story:
> As a developer, I need a configured Supabase project with database schema and authentication so that I can build the backend API.

#### Acceptance Criteria:
- [ ] Supabase project created
- [ ] Database schema designed and created
- [ ] Authentication configured
- [ ] Storage bucket created
- [ ] API keys secured in .env

#### Technical Tasks:

**Task 2.1.1: Supabase Project Setup** (1 hour)
```bash
Priority: P0
Estimated Time: 1 hour

Steps:
1. Go to supabase.com → Create account
2. Create new project: "dreamvision-production"
3. Region: Closest to you (for low latency)
4. Database password: Generate strong password
5. Wait for project initialization (~2 minutes)
6. Note down:
   - Project URL: https://xxxxx.supabase.co
   - Project API Key (anon, public)
   - Service Role Key (secret, never expose)

Save to .env:
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJxxx...
SUPABASE_SERVICE_KEY=eyJxxx... (backend only)
```

**Task 2.1.2: Database Schema Design** (2 hours)
```sql
Priority: P0
Estimated Time: 2 hours

-- Open Supabase SQL Editor and run:

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table (managed by Supabase Auth, but we add metadata)
CREATE TABLE public.user_profiles (
  id UUID REFERENCES auth.users(id) PRIMARY KEY,
  username TEXT UNIQUE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  subscription_tier TEXT DEFAULT 'free', -- 'free' | 'premium'
  dreams_count INTEGER DEFAULT 0,
  videos_count INTEGER DEFAULT 0
);

-- Dreams table
CREATE TABLE public.dreams (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES public.user_profiles(id) ON DELETE CASCADE,
  dream_text TEXT NOT NULL,
  video_prompt TEXT NOT NULL,
  category TEXT NOT NULL, -- 'gothic' | 'chase' | 'flight' | etc.
  template_used TEXT NOT NULL,
  confidence FLOAT DEFAULT 0.0,
  token_usage JSONB, -- {input: 150, output: 120}
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Videos table
CREATE TABLE public.videos (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  dream_id UUID REFERENCES public.dreams(id) ON DELETE CASCADE,
  job_id TEXT UNIQUE NOT NULL, -- Runway job ID
  status TEXT NOT NULL, -- 'pending' | 'processing' | 'completed' | 'failed'
  video_url TEXT,
  thumbnail_url TEXT,
  duration INTEGER DEFAULT 5,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

-- Indexes for performance
CREATE INDEX idx_dreams_user_id ON public.dreams(user_id);
CREATE INDEX idx_dreams_created_at ON public.dreams(created_at DESC);
CREATE INDEX idx_dreams_category ON public.dreams(category);
CREATE INDEX idx_videos_job_id ON public.videos(job_id);
CREATE INDEX idx_videos_dream_id ON public.videos(dream_id);

-- Row Level Security (RLS)
ALTER TABLE public.user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.dreams ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.videos ENABLE ROW LEVEL SECURITY;

-- Policies: Users can only see their own data
CREATE POLICY "Users can view own profile" ON public.user_profiles
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON public.user_profiles
  FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can view own dreams" ON public.dreams
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own dreams" ON public.dreams
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can view videos for own dreams" ON public.videos
  FOR SELECT USING (
    EXISTS (
      SELECT 1 FROM public.dreams
      WHERE dreams.id = videos.dream_id
      AND dreams.user_id = auth.uid()
    )
  );

-- Function: Update user profile stats
CREATE OR REPLACE FUNCTION update_user_stats()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE public.user_profiles
  SET 
    dreams_count = (SELECT COUNT(*) FROM public.dreams WHERE user_id = NEW.user_id),
    videos_count = (SELECT COUNT(*) FROM public.videos v 
                    JOIN public.dreams d ON v.dream_id = d.id 
                    WHERE d.user_id = NEW.user_id AND v.status = 'completed')
  WHERE id = NEW.user_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Auto-update stats
CREATE TRIGGER trigger_update_user_stats
AFTER INSERT ON public.dreams
FOR EACH ROW EXECUTE FUNCTION update_user_stats();
```

**Task 2.1.3: Supabase Authentication Setup** (1 hour)
```bash
Priority: P0
Estimated Time: 1 hour

Steps (in Supabase Dashboard):
1. Go to Authentication → Settings
2. Enable Email/Password auth
3. Disable email confirmation (for MVP) OR configure email provider
4. Set JWT expiry: 3600 seconds (1 hour)
5. Set Refresh Token expiry: 604800 seconds (7 days)

Optional (for production):
- Configure email templates (Welcome, Password Reset)
- Add custom SMTP (or use Supabase default)
- Enable OAuth providers (Google, Apple) - later

6. Go to Authentication → URL Configuration
   - Site URL: http://localhost:19006 (development)
   - Redirect URLs: Add expo deeplink scheme

7. Test auth in SQL Editor:
   -- Create test user
   INSERT INTO auth.users (email, encrypted_password)
   VALUES ('test@example.com', crypt('password123', gen_salt('bf')));
   
   -- Should auto-create profile via trigger (if you set one up)
```

**Task 2.1.4: Storage Bucket for Thumbnails** (30 minutes)
```bash
Priority: P1
Estimated Time: 30 minutes

Steps (in Supabase Dashboard):
1. Go to Storage → Create bucket
2. Bucket name: "video-thumbnails"
3. Public bucket: Yes (for easy access)
4. File size limit: 5MB
5. Allowed MIME types: image/jpeg, image/png

6. Create bucket policy:
   - Users can upload to their own folder
   - Everyone can read (public thumbnails)

SQL for policy:
CREATE POLICY "Users can upload thumbnails"
ON storage.objects FOR INSERT
WITH CHECK (
  bucket_id = 'video-thumbnails' AND
  auth.uid()::text = (storage.foldername(name))[1]
);

CREATE POLICY "Thumbnails are publicly accessible"
ON storage.objects FOR SELECT
USING (bucket_id = 'video-thumbnails');
```

**Task 2.1.5: Environment Variables & Documentation** (30 minutes)
```bash
Priority: P0
Estimated Time: 30 minutes

Create docs/SUPABASE-SETUP.md with:
- Project URL and API keys
- Database schema explanation
- RLS policies explanation
- How to run migrations
- How to reset database (for testing)

Update backend/.env.example:
# Supabase Configuration
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJxxx... (public, safe for client)
SUPABASE_SERVICE_KEY=eyJxxx... (secret, backend only)

# Note: ANON_KEY respects RLS policies
# SERVICE_KEY bypasses RLS (admin access)
```

#### Deliverables:
- [ ] Supabase project created
- [ ] Database schema implemented
- [ ] RLS policies configured
- [ ] Storage bucket ready
- [ ] Documentation created
- [ ] Environment variables documented

#### Testing Checklist:
```bash
# In Supabase SQL Editor:
- [ ] Run schema SQL → no errors
- [ ] Check tables exist: user_profiles, dreams, videos
- [ ] Check indexes created
- [ ] Test RLS: Try SELECT as anonymous → should fail
- [ ] Create test user → profile auto-created
- [ ] Upload test image to storage → succeeds
```

---

### Epic 2.2: FastAPI Project Setup

**Duration:** Day 2 (5-6 hours)  
**Priority:** P0  
**Dependencies:** Epic 2.1

#### User Story:
> As a developer, I need a well-structured FastAPI project with Supabase integration so that I can build API endpoints.

#### Acceptance Criteria:
- [ ] FastAPI project initialized
- [ ] Supabase client configured
- [ ] Health check endpoint working
- [ ] Docker setup for local development
- [ ] API documentation auto-generated

#### Technical Tasks:

**Task 2.2.1: Project Initialization** (1.5 hours)
```bash
Priority: P0
Estimated Time: 1.5 hours

# In your dreamvision-ai/backend folder:
cd backend
mkdir -p app/api/v1/routes app/core app/models app/services app/utils tests

# Create __init__.py files
touch app/__init__.py
touch app/api/__init__.py
touch app/api/v1/__init__.py
touch app/api/v1/routes/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py
touch app/services/__init__.py
touch app/utils/__init__.py

# Create main files
touch app/main.py
touch app/config.py
touch app/core/supabase.py
touch app/api/v1/routes/health.py
```

**Task 2.2.2: Dependencies Installation** (30 minutes)
```python
Priority: P0
Estimated Time: 30 minutes

# Create requirements.txt:
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
python-dotenv==1.0.0
httpx==0.25.2
anthropic==0.7.7
supabase==2.3.0
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
slowapi==0.1.9
sentry-sdk[fastapi]==1.38.0

# Development dependencies
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
black==23.11.0
flake8==6.1.0
mypy==1.7.1

# Install:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Task 2.2.3: Configuration Management** (1 hour)
```python
Priority: P0
Estimated Time: 1 hour

# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API
    API_VERSION: str = "v1"
    API_PREFIX: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str = "DreamVision AI"
    ENVIRONMENT: str = "development"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Supabase
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_KEY: str
    
    # AI Services
    ANTHROPIC_API_KEY: str
    RUNWAY_API_KEY: str
    
    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:19006",
        "http://localhost:8081",
        "exp://localhost:19000"
    ]
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 10
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
```

**Task 2.2.4: Supabase Client** (1 hour)
```python
Priority: P0
Estimated Time: 1 hour

# app/core/supabase.py
from supabase import create_client, Client
from app.config import settings
from functools import lru_cache

@lru_cache()
def get_supabase_client() -> Client:
    """
    Create and cache Supabase client.
    Uses SERVICE_KEY for backend operations (bypasses RLS).
    """
    return create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_SERVICE_KEY
    )

def get_supabase_anon_client() -> Client:
    """
    Create Supabase client with ANON_KEY.
    Respects RLS policies (for user-scoped operations).
    """
    return create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_ANON_KEY
    )

# Dependency for FastAPI routes
async def get_supabase() -> Client:
    return get_supabase_client()
```

**Task 2.2.5: FastAPI Application** (1.5 hours)
```python
Priority: P0
Estimated Time: 1.5 hours

# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import sentry_sdk

from app.config import settings
from app.api.v1.routes import health

# Initialize Sentry (optional, for monitoring)
if settings.ENVIRONMENT == "production":
    sentry_sdk.init(
        dsn="YOUR_SENTRY_DSN",
        traces_sample_rate=1.0,
    )

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=f"{settings.API_PREFIX}/redoc",
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    health.router,
    prefix=settings.API_PREFIX,
    tags=["Health"]
)

@app.get("/")
async def root():
    return {
        "message": "DreamVision AI API",
        "version": settings.API_VERSION,
        "docs": f"{settings.API_PREFIX}/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
```

**Task 2.2.6: Health Check Endpoint** (30 minutes)
```python
Priority: P0
Estimated Time: 30 minutes

# app/api/v1/routes/health.py
from fastapi import APIRouter, Depends
from supabase import Client
from app.core.supabase import get_supabase
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check(
    supabase: Client = Depends(get_supabase)
):
    """
    Health check endpoint.
    Checks API status and Supabase connection.
    """
    try:
        # Test Supabase connection
        result = supabase.table("user_profiles").select("count").execute()
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return {
        "status": "healthy" if db_status == "connected" else "degraded",
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status,
        "version": "1.0.0"
    }

@router.get("/health/db")
async def database_health(
    supabase: Client = Depends(get_supabase)
):
    """Detailed database health check"""
    try:
        # Test all tables
        tables = ["user_profiles", "dreams", "videos"]
        table_status = {}
        
        for table in tables:
            result = supabase.table(table).select("count").execute()
            table_status[table] = "ok"
        
        return {
            "status": "healthy",
            "tables": table_status
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
```

**Task 2.2.7: Docker Setup** (1 hour)
```dockerfile
Priority: P1
Estimated Time: 1 hour

# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml (in root directory)
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Deliverables:
- [ ] FastAPI application running
- [ ] Supabase client configured
- [ ] Health check endpoint responding
- [ ] Docker setup complete
- [ ] API documentation at /docs

#### Testing Checklist:
```bash
# Start server
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# Test endpoints:
- [ ] curl http://localhost:8000/ → Returns API info
- [ ] curl http://localhost:8000/api/v1/health → Returns healthy
- [ ] curl http://localhost:8000/api/v1/health/db → Returns table status
- [ ] Open http://localhost:8000/api/v1/docs → Swagger UI loads
- [ ] Docker: docker-compose up → Backend starts

# Test Supabase connection:
- [ ] Health check shows "connected"
- [ ] No errors in console
```

---

### Epic 2.3: Dream Analysis API

**Duration:** Day 3-4 (10-12 hours)  
**Priority:** P0  
**Dependencies:** Epic 2.2

#### User Story:
> As a mobile app, I need to send dream text and receive an optimized video prompt so that I can generate dream videos.

#### Acceptance Criteria:
- [ ] POST /api/v1/dreams/analyze endpoint working
- [ ] Claude Sonnet 4.5 integrated with Minimal Prompt System v2.0
- [ ] Dream saved to Supabase
- [ ] Response time < 5 seconds
- [ ] Rate limiting active
- [ ] Error handling for API failures

#### Technical Tasks:

**Task 2.3.1: Pydantic Models** (1 hour)
```python
Priority: P0
Estimated Time: 1 hour

# app/models/dream.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from uuid import UUID

class DreamAnalysisRequest(BaseModel):
    dream_text: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        description="User's dream description"
    )
    user_id: Optional[UUID] = None
    
    @validator('dream_text')
    def validate_dream_text(cls, v):
        if not v.strip():
            raise ValueError("Dream text cannot be empty")
        return v.strip()

class DreamAnalysisResponse(BaseModel):
    dream_id: UUID
    video_prompt: str
    category: str
    template_used: str
    confidence: float
    token_usage: dict
    processing_time_ms: int
    created_at: datetime

class DreamDetail(BaseModel):
    id: UUID
    user_id: UUID
    dream_text: str
    video_prompt: str
    category: str
    template_used: str
    confidence: float
    created_at: datetime
    video_status: Optional[str] = None
    video_url: Optional[str] = None

class DreamListResponse(BaseModel):
    dreams: list[DreamDetail]
    total: int
    page: int
    limit: int
    pages: int
```

**Task 2.3.2: Claude Service with Minimal Prompt System v2.0** (3 hours)
```python
Priority: P0
Estimated Time: 3 hours

# app/services/claude_service.py
from anthropic import Anthropic
from app.config import settings
from app.utils.prompts import get_system_prompt
import time
import json

class ClaudeService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.system_prompt = get_system_prompt()
        self.model = "claude-sonnet-4-20250514"
    
    async def analyze_dream(self, dream_text: str) -> dict:
        """
        Analyze dream text and return optimized Runway prompt.
        Uses Minimal Dream Prompt System v2.0.
        """
        start_time = time.time()
        
        try:
            # Create message with Claude
            message = self.client.messages.create(
                model=self.model,
                max_tokens=200,  # Short output (just the prompt)
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": f"Dream: {dream_text}\n\nGenerate Runway prompt:"
                    }
                ]
            )
            
            # Parse response
            response_text = message.content[0].text
            
            # Extract structured data from response
            # Expected format: CATEGORY: <category>\nPROMPT: <prompt>
            lines = response_text.strip().split('\n')
            category = "unknown"
            video_prompt = response_text
            template_used = "GENERAL"
            
            for line in lines:
                if line.startswith("CATEGORY:"):
                    category = line.replace("CATEGORY:", "").strip().lower()
                elif line.startswith("TEMPLATE:"):
                    template_used = line.replace("TEMPLATE:", "").strip()
                elif line.startswith("PROMPT:"):
                    video_prompt = line.replace("PROMPT:", "").strip()
            
            processing_time = int((time.time() - start_time) * 1000)
            
            return {
                "video_prompt": video_prompt,
                "category": category,
                "template_used": template_used,
                "confidence": 0.95,  # Can be calculated based on Claude response
                "token_usage": {
                    "input": message.usage.input_tokens,
                    "output": message.usage.output_tokens
                },
                "processing_time_ms": processing_time
            }
            
        except Exception as e:
            raise Exception(f"Claude API error: {str(e)}")
```

**Task 2.3.3: Prompt Templates Utility** (2 hours)
```python
Priority: P0
Estimated Time: 2 hours

# app/utils/prompts.py
"""
Minimal Dream Prompt System v2.0
(Load from your Phase 1 work)
"""

def get_system_prompt() -> str:
    """
    Returns the complete Minimal Dream Prompt System v2.0.
    This is the same prompt you optimized in Phase 1.
    """
    return """You are a dream-to-video prompt specialist for Runway Gen-3 Alpha.

OBJECTIVE: Transform dream descriptions into precise 5-second video prompts.

CORE TEMPLATES:

1. GOTHIC/NIGHTMARE:
POV continuous glide through [twisted/decaying space], [oppressive element dominates frame], [unnatural lighting], slow push forward, dread mounting.

2. CHASE/PURSUIT:
POV rapid movement through [location], [threat] gaining in peripheral, sharp turns, [environmental obstacles], accelerating panic, abrupt cuts.

3. FLIGHT/FLOATING:
POV gentle rise through [environment], [surreal elements] drift past, weightless perspective shifts, impossible angles, dreamlike momentum.

4. TRANSFORMATION:
POV fixed on [subject/space], [element] gradually shifts/morphs, reality bends, [detail] transforms, unsettling transition, surreal revelation.

5. PHYSICS-DEFYING:
POV [impossible camera movement] through [space], [objects/gravity] behaving wrong, [architectural impossibility], reality glitches.

6. LIMINAL/UNCANNY:
POV slow track through [familiar space made wrong], [uncanny detail], sterile/fluorescent lighting, empty wrongness, mounting unease.

FAIL-SAFE RULES:
1. Output 100-150 words maximum
2. ONE continuous shot only
3. Lead with POV camera movement
4. NO character names - use "the dreamer" or "a figure"
5. NO shot lists or sequences - ONE SCENE
6. Maintain 5-second focus
7. Build single atmospheric moment
8. Use active verbs (glide, push, track, drift)
9. Include lighting direction
10. End with emotional beat
11. Format: Start with template, add 2-3 dream-specific details

PROCESS:
1. Identify dream category
2. Select matching template
3. Insert dream's key visual elements
4. Ensure POV clarity
5. Verify 5-second scope

OUTPUT FORMAT:
CATEGORY: [category]
TEMPLATE: [template_name]
PROMPT: [final prompt]

Example:
Dream: "I was in my old school but the hallways kept getting longer and the lights were flickering."

CATEGORY: liminal
TEMPLATE: LIMINAL
PROMPT: POV slow track through endless school corridor, fluorescent lights stutter overhead, doors stretch further apart, familiar lockers distort at edges, sterile wrongness, mounting unease as perspective warps.

Now analyze the dream and generate the prompt."""

def get_template(category: str) -> str:
    """Get specific template by category"""
    templates = {
        "gothic": "POV continuous glide through [twisted/decaying space], [oppressive element dominates frame], [unnatural lighting], slow push forward, dread mounting.",
        "chase": "POV rapid movement through [location], [threat] gaining in peripheral, sharp turns, [environmental obstacles], accelerating panic, abrupt cuts.",
        "flight": "POV gentle rise through [environment], [surreal elements] drift past, weightless perspective shifts, impossible angles, dreamlike momentum.",
        "transformation": "POV fixed on [subject/space], [element] gradually shifts/morphs, reality bends, [detail] transforms, unsettling transition, surreal revelation.",
        "physics": "POV [impossible camera movement] through [space], [objects/gravity] behaving wrong, [architectural impossibility], reality glitches.",
        "liminal": "POV slow track through [familiar space made wrong], [uncanny detail], sterile/fluorescent lighting, empty wrongness, mounting unease."
    }
    return templates.get(category, templates["gothic"])
```

**Task 2.3.4: Supabase Service for Dreams** (2 hours)
```python
Priority: P0
Estimated Time: 2 hours

# app/services/supabase_service.py
from supabase import Client
from uuid import UUID
from datetime import datetime
from typing import Optional

class SupabaseService:
    def __init__(self, client: Client):
        self.client = client
    
    async def create_dream(
        self,
        user_id: UUID,
        dream_text: str,
        video_prompt: str,
        category: str,
        template_used: str,
        confidence: float,
        token_usage: dict
    ) -> dict:
        """Save dream analysis to Supabase"""
        try:
            result = self.client.table("dreams").insert({
                "user_id": str(user_id),
                "dream_text": dream_text,
                "video_prompt": video_prompt,
                "category": category,
                "template_used": template_used,
                "confidence": confidence,
                "token_usage": token_usage
            }).execute()
            
            return result.data[0]
        except Exception as e:
            raise Exception(f"Database error: {str(e)}")
    
    async def get_user_dreams(
        self,
        user_id: UUID,
        page: int = 1,
        limit: int = 20,
        category: Optional[str] = None
    ) -> tuple[list[dict], int]:
        """Get user's dreams with pagination"""
        offset = (page - 1) * limit
        
        query = self.client.table("dreams").select(
            "*, videos(*)",
            count="exact"
        ).eq("user_id", str(user_id)).order(
            "created_at",
            desc=True
        ).range(offset, offset + limit - 1)
        
        if category:
            query = query.eq("category", category)
        
        result = query.execute()
        
        return result.data, result.count
    
    async def get_dream_by_id(
        self,
        dream_id: UUID,
        user_id: UUID
    ) -> Optional[dict]:
        """Get single dream with video info"""
        result = self.client.table("dreams").select(
            "*, videos(*)"
        ).eq("id", str(dream_id)).eq(
            "user_id", str(user_id)
        ).single().execute()
        
        return result.data if result.data else None
```

**Task 2.3.5: Dream Analysis Endpoint** (2 hours)
```python
Priority: P0
Estimated Time: 2 hours

# app/api/v1/routes/dreams.py
from fastapi import APIRouter, Depends, HTTPException, status
from slowapi import Limiter
from slowapi.util import get_remote_address
from supabase import Client
from uuid import UUID

from app.models.dream import (
    DreamAnalysisRequest,
    DreamAnalysisResponse,
    DreamDetail,
    DreamListResponse
)
from app.services.claude_service import ClaudeService
from app.services.supabase_service import SupabaseService
from app.core.supabase import get_supabase
from app.api.v1.dependencies import get_current_user

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/dreams/analyze", response_model=DreamAnalysisResponse)
@limiter.limit("10/minute")
async def analyze_dream(
    request: DreamAnalysisRequest,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """
    Analyze dream text and generate video prompt.
    
    - **dream_text**: User's dream description (10-2000 chars)
    - Returns: Video prompt, category, template used
    """
    try:
        # Initialize services
        claude = ClaudeService()
        db = SupabaseService(supabase)
        
        # Analyze dream with Claude
        analysis = await claude.analyze_dream(request.dream_text)
        
        # Save to database
        dream = await db.create_dream(
            user_id=UUID(current_user["id"]),
            dream_text=request.dream_text,
            video_prompt=analysis["video_prompt"],
            category=analysis["category"],
            template_used=analysis["template_used"],
            confidence=analysis["confidence"],
            token_usage=analysis["token_usage"]
        )
        
        return DreamAnalysisResponse(
            dream_id=dream["id"],
            video_prompt=analysis["video_prompt"],
            category=analysis["category"],
            template_used=analysis["template_used"],
            confidence=analysis["confidence"],
            token_usage=analysis["token_usage"],
            processing_time_ms=analysis["processing_time_ms"],
            created_at=dream["created_at"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Dream analysis failed: {str(e)}"
        )

@router.get("/dreams", response_model=DreamListResponse)
async def get_dreams(
    page: int = 1,
    limit: int = 20,
    category: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """Get user's dream history with pagination"""
    db = SupabaseService(supabase)
    dreams, total = await db.get_user_dreams(
        user_id=UUID(current_user["id"]),
        page=page,
        limit=limit,
        category=category
    )
    
    pages = (total + limit - 1) // limit
    
    return DreamListResponse(
        dreams=dreams,
        total=total,
        page=page,
        limit=limit,
        pages=pages
    )

@router.get("/dreams/{dream_id}", response_model=DreamDetail)
async def get_dream(
    dream_id: UUID,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """Get single dream details"""
    db = SupabaseService(supabase)
    dream = await db.get_dream_by_id(
        dream_id=dream_id,
        user_id=UUID(current_user["id"])
    )
    
    if not dream:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dream not found"
        )
    
    return dream
```

**Task 2.3.6: Authentication Dependency** (1 hour)
```python
Priority: P0
Estimated Time: 1 hour

# app/api/v1/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client
from app.core.supabase import get_supabase

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    supabase: Client = Depends(get_supabase)
) -> dict:
    """
    Validate JWT token with Supabase and return user.
    """
    token = credentials.credentials
    
    try:
        # Verify token with Supabase
        user = supabase.auth.get_user(token)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        
        return user.user.model_dump()
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed: {str(e)}"
        )
```

#### Deliverables:
- [ ] Dream analysis endpoint working
- [ ] Claude integration with Minimal Prompt System v2.0
- [ ] Dreams saved to Supabase
- [ ] Rate limiting active
- [ ] Authentication required
- [ ] Error handling complete

#### Testing Checklist:
```bash
# Register user first (we'll add this endpoint next)
# Then get token

# Test dream analysis:
curl -X POST http://localhost:8000/api/v1/dreams/analyze \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dream_text": "I was flying over a dark forest with twisted trees"
  }'

# Expected response:
{
  "dream_id": "uuid",
  "video_prompt": "POV gentle rise through dark forest...",
  "category": "flight",
  "template_used": "FLIGHT",
  "confidence": 0.95,
  "token_usage": {"input": 150, "output": 120},
  "processing_time_ms": 2341,
  "created_at": "2025-11-11T12:00:00Z"
}

# Test rate limiting (send 11 requests quickly):
- [ ] First 10 succeed
- [ ] 11th returns 429 Too Many Requests

# Test authentication:
- [ ] Without token → 401 Unauthorized
- [ ] With invalid token → 401 Unauthorized
- [ ] With valid token → 200 OK

# Check Supabase:
- [ ] Open Supabase → Table Editor → dreams
- [ ] See your dream saved with correct data
```

---

### Epic 2.4: Video Generation API

**Duration:** Day 5-6 (10-12 hours)  
**Priority:** P0  
**Dependencies:** Epic 2.3

#### User Story:
> As a mobile app, I need to request video generation and check status so that users can get their dream videos.

#### Acceptance Criteria:
- [ ] POST /api/v1/videos/generate starts video generation
- [ ] GET /api/v1/videos/{job_id} returns status
- [ ] Runway Gen-3 Alpha integrated
- [ ] Video metadata saved to Supabase
- [ ] Status polling works correctly

#### Technical Tasks:

**Task 2.4.1: Video Models** (30 minutes)
```python
Priority: P0
Estimated Time: 30 minutes

# app/models/video.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class VideoGenerationRequest(BaseModel):
    dream_id: UUID = Field(..., description="Dream ID to generate video for")
    duration: int = Field(default=5, ge=5, le=10, description="Video duration in seconds")

class VideoGenerationResponse(BaseModel):
    video_id: UUID
    job_id: str
    status: str  # 'pending' | 'processing' | 'completed' | 'failed'
    created_at: datetime
    estimated_completion_time: Optional[datetime] = None

class VideoStatusResponse(BaseModel):
    video_id: UUID
    job_id: str
    status: str
    progress: Optional[int] = None  # 0-100
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    duration: int
    created_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None

class CombinedDreamVideoRequest(BaseModel):
    dream_text: str = Field(..., min_length=10, max_length=2000)
    duration: int = Field(default=5, ge=5, le=10)

class CombinedDreamVideoResponse(BaseModel):
    dream_analysis: DreamAnalysisResponse
    video_generation: VideoGenerationResponse
```

**Task 2.4.2: Runway Service** (3 hours)
```python
Priority: P0
Estimated Time: 3 hours

# app/services/runway_service.py
import httpx
from app.config import settings
from typing import Optional
import asyncio

class RunwayService:
    def __init__(self):
        self.api_key = settings.RUNWAY_API_KEY
        self.base_url = "https://api.runwayml.com/v1"  # Or kie.ai URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def generate_video(
        self,
        prompt: str,
        duration: int = 5
    ) -> dict:
        """
        Start video generation with Runway Gen-3 Alpha.
        
        Returns job_id and initial status.
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/generations",
                    headers=self.headers,
                    json={
                        "prompt": prompt,
                        "duration": duration,
                        "model": "gen3a_turbo",  # Gen-3 Alpha Turbo
                        "ratio": "16:9"
                    },
                    timeout=30.0
                )
                
                response.raise_for_status()
                data = response.json()
                
                return {
                    "job_id": data["id"],
                    "status": "pending",
                    "created_at": data["createdAt"]
                }
                
            except httpx.HTTPError as e:
                raise Exception(f"Runway API error: {str(e)}")
    
    async def check_status(self, job_id: str) -> dict:
        """
        Check video generation status.
        
        Returns status, progress, and video_url when ready.
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/generations/{job_id}",
                    headers=self.headers,
                    timeout=10.0
                )
                
                response.raise_for_status()
                data = response.json()
                
                # Map Runway status to our status
                runway_status = data["status"]
                our_status = {
                    "PENDING": "pending",
                    "RUNNING": "processing",
                    "SUCCEEDED": "completed",
                    "FAILED": "failed"
                }.get(runway_status, "pending")
                
                result = {
                    "status": our_status,
                    "progress": data.get("progress", 0),
                }
                
                # Add video URL if completed
                if our_status == "completed":
                    result["video_url"] = data["output"][0]
                    result["completed_at"] = data["completedAt"]
                
                # Add error if failed
                if our_status == "failed":
                    result["error_message"] = data.get("error", "Unknown error")
                
                return result
                
            except httpx.HTTPError as e:
                raise Exception(f"Runway API error: {str(e)}")
    
    async def wait_for_completion(
        self,
        job_id: str,
        max_wait_seconds: int = 300,
        poll_interval: int = 5
    ) -> dict:
        """
        Poll video status until completed or timeout.
        (Optional - for testing/debugging)
        """
        start_time = asyncio.get_event_loop().time()
        
        while True:
            elapsed = asyncio.get_event_loop().time() - start_time
            
            if elapsed > max_wait_seconds:
                raise TimeoutError("Video generation timeout")
            
            status = await self.check_status(job_id)
            
            if status["status"] in ["completed", "failed"]:
                return status
            
            await asyncio.sleep(poll_interval)
```

**Task 2.4.3: Supabase Video Service** (1.5 hours)
```python
Priority: P0
Estimated Time: 1.5 hours

# Update app/services/supabase_service.py
# Add video methods:

async def create_video(
    self,
    dream_id: UUID,
    job_id: str,
    status: str = "pending"
) -> dict:
    """Create video record in Supabase"""
    try:
        result = self.client.table("videos").insert({
            "dream_id": str(dream_id),
            "job_id": job_id,
            "status": status
        }).execute()
        
        return result.data[0]
    except Exception as e:
        raise Exception(f"Database error: {str(e)}")

async def update_video_status(
    self,
    job_id: str,
    status: str,
    video_url: Optional[str] = None,
    thumbnail_url: Optional[str] = None,
    completed_at: Optional[datetime] = None,
    error_message: Optional[str] = None
) -> dict:
    """Update video status in Supabase"""
    update_data = {"status": status}
    
    if video_url:
        update_data["video_url"] = video_url
    if thumbnail_url:
        update_data["thumbnail_url"] = thumbnail_url
    if completed_at:
        update_data["completed_at"] = completed_at.isoformat()
    if error_message:
        update_data["error_message"] = error_message
    
    result = self.client.table("videos").update(
        update_data
    ).eq("job_id", job_id).execute()
    
    return result.data[0]

async def get_video_by_job_id(self, job_id: str) -> Optional[dict]:
    """Get video by Runway job_id"""
    result = self.client.table("videos").select(
        "*, dreams(*)"
    ).eq("job_id", job_id).single().execute()
    
    return result.data if result.data else None
```

**Task 2.4.4: Video Endpoints** (3 hours)
```python
Priority: P0
Estimated Time: 3 hours

# app/api/v1/routes/videos.py
from fastapi import APIRouter, Depends, HTTPException, status
from supabase import Client
from uuid import UUID
from datetime import datetime, timedelta

from app.models.video import (
    VideoGenerationRequest,
    VideoGenerationResponse,
    VideoStatusResponse,
    CombinedDreamVideoRequest,
    CombinedDreamVideoResponse
)
from app.services.runway_service import RunwayService
from app.services.supabase_service import SupabaseService
from app.core.supabase import get_supabase
from app.api.v1.dependencies import get_current_user

router = APIRouter()

@router.post("/videos/generate", response_model=VideoGenerationResponse)
async def generate_video(
    request: VideoGenerationRequest,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """
    Start video generation for a dream.
    
    - **dream_id**: UUID of the dream to visualize
    - **duration**: Video duration (5-10 seconds)
    - Returns: job_id to poll for status
    """
    try:
        db = SupabaseService(supabase)
        runway = RunwayService()
        
        # Get dream
        dream = await db.get_dream_by_id(
            dream_id=request.dream_id,
            user_id=UUID(current_user["id"])
        )
        
        if not dream:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Dream not found"
            )
        
        # Start video generation with Runway
        result = await runway.generate_video(
            prompt=dream["video_prompt"],
            duration=request.duration
        )
        
        # Save video record to database
        video = await db.create_video(
            dream_id=request.dream_id,
            job_id=result["job_id"],
            status="pending"
        )
        
        # Estimate completion time (Runway usually takes 1-3 minutes)
        estimated_time = datetime.utcnow() + timedelta(minutes=2)
        
        return VideoGenerationResponse(
            video_id=video["id"],
            job_id=result["job_id"],
            status="pending",
            created_at=video["created_at"],
            estimated_completion_time=estimated_time
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Video generation failed: {str(e)}"
        )

@router.get("/videos/{job_id}", response_model=VideoStatusResponse)
async def get_video_status(
    job_id: str,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """
    Get video generation status.
    
    - **job_id**: Runway job ID from /videos/generate
    - Returns: Current status, progress, video_url when ready
    """
    try:
        db = SupabaseService(supabase)
        runway = RunwayService()
        
        # Get video record from database
        video = await db.get_video_by_job_id(job_id)
        
        if not video:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Video not found"
            )
        
        # Verify user owns this dream
        if video["dreams"]["user_id"] != current_user["id"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
        
        # If not completed, check Runway for updates
        if video["status"] not in ["completed", "failed"]:
            runway_status = await runway.check_status(job_id)
            
            # Update database with new status
            if runway_status["status"] != video["status"]:
                video = await db.update_video_status(
                    job_id=job_id,
                    status=runway_status["status"],
                    video_url=runway_status.get("video_url"),
                    completed_at=runway_status.get("completed_at"),
                    error_message=runway_status.get("error_message")
                )
        
        return VideoStatusResponse(
            video_id=video["id"],
            job_id=video["job_id"],
            status=video["status"],
            progress=runway_status.get("progress") if video["status"] == "processing" else None,
            video_url=video.get("video_url"),
            thumbnail_url=video.get("thumbnail_url"),
            duration=video.get("duration", 5),
            created_at=video["created_at"],
            completed_at=video.get("completed_at"),
            error_message=video.get("error_message")
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get status: {str(e)}"
        )

@router.post("/dreams/generate-video", response_model=CombinedDreamVideoResponse)
async def analyze_and_generate(
    request: CombinedDreamVideoRequest,
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """
    Combined endpoint: Analyze dream AND start video generation.
    
    This is the main endpoint mobile app will use.
    """
    try:
        # Step 1: Analyze dream (use existing logic from dreams route)
        from app.services.claude_service import ClaudeService
        
        claude = ClaudeService()
        db = SupabaseService(supabase)
        runway = RunwayService()
        
        # Analyze dream
        analysis = await claude.analyze_dream(request.dream_text)
        
        # Save dream
        dream = await db.create_dream(
            user_id=UUID(current_user["id"]),
            dream_text=request.dream_text,
            video_prompt=analysis["video_prompt"],
            category=analysis["category"],
            template_used=analysis["template_used"],
            confidence=analysis["confidence"],
            token_usage=analysis["token_usage"]
        )
        
        # Step 2: Start video generation
        video_result = await runway.generate_video(
            prompt=analysis["video_prompt"],
            duration=request.duration
        )
        
        # Save video record
        video = await db.create_video(
            dream_id=UUID(dream["id"]),
            job_id=video_result["job_id"],
            status="pending"
        )
        
        estimated_time = datetime.utcnow() + timedelta(minutes=2)
        
        return CombinedDreamVideoResponse(
            dream_analysis=DreamAnalysisResponse(
                dream_id=dream["id"],
                video_prompt=analysis["video_prompt"],
                category=analysis["category"],
                template_used=analysis["template_used"],
                confidence=analysis["confidence"],
                token_usage=analysis["token_usage"],
                processing_time_ms=analysis["processing_time_ms"],
                created_at=dream["created_at"]
            ),
            video_generation=VideoGenerationResponse(
                video_id=video["id"],
                job_id=video_result["job_id"],
                status="pending",
                created_at=video["created_at"],
                estimated_completion_time=estimated_time
            )
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process dream: {str(e)}"
        )
```

#### Deliverables:
- [ ] Video generation endpoint
- [ ] Video status endpoint
- [ ] Combined dream+video endpoint
- [ ] Runway API integrated
- [ ] Video records in Supabase
- [ ] Status polling works

#### Testing Checklist:
```bash
# Test video generation:
curl -X POST http://localhost:8000/api/v1/videos/generate \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dream_id": "DREAM_UUID",
    "duration": 5
  }'

# Response:
{
  "video_id": "uuid",
  "job_id": "run_abc123",
  "status": "pending",
  "created_at": "2025-11-11T12:00:00Z",
  "estimated_completion_time": "2025-11-11T12:02:00Z"
}

# Test status polling (wait 10 seconds, then check):
curl http://localhost:8000/api/v1/videos/run_abc123 \
  -H "Authorization: Bearer YOUR_TOKEN"

# Response (processing):
{
  "video_id": "uuid",
  "job_id": "run_abc123",
  "status": "processing",
  "progress": 45,
  ...
}

# Response (completed):
{
  "video_id": "uuid",
  "job_id": "run_abc123",
  "status": "completed",
  "video_url": "https://cdn.runwayml.com/...",
  "thumbnail_url": "https://...",
  ...
}

# Test combined endpoint:
curl -X POST http://localhost:8000/api/v1/dreams/generate-video \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dream_text": "I was flying over mountains",
    "duration": 5
  }'

# Should return both dream analysis AND video job_id
```

---

### Epic 2.5: Authentication Routes

**Duration:** Day 7 (5-6 hours)  
**Priority:** P0  
**Dependencies:** Epic 2.2

#### User Story:
> As a user, I need to register and login via the API so that I can use the mobile app.

#### Acceptance Criteria:
- [ ] POST /api/v1/auth/register creates user
- [ ] POST /api/v1/auth/login returns JWT token
- [ ] Supabase Auth handles authentication
- [ ] User profile auto-created on registration
- [ ] Token validation works

#### Technical Tasks:

**Task 2.5.1: Auth Models** (30 minutes)
```python
Priority: P0
Estimated Time: 30 minutes

# app/models/auth.py
from pydantic import BaseModel, EmailStr, Field, validator

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    username: str = Field(..., min_length=3, max_length=30)
    
    @validator('password')
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain digit')
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user: dict

class UserProfile(BaseModel):
    id: str
    email: str
    username: str
    subscription_tier: str
    dreams_count: int
    videos_count: int
    created_at: datetime
```

**Task 2.5.2: Auth Service** (2 hours)
```python
Priority: P0
Estimated Time: 2 hours

# app/services/auth_service.py
from supabase import Client
from app.models.auth import UserRegister, UserLogin

class AuthService:
    def __init__(self, client: Client):
        self.client = client
    
    async def register(self, user_data: UserRegister) -> dict:
        """
        Register new user with Supabase Auth.
        Auto-creates profile via database trigger.
        """
        try:
            # Sign up with Supabase
            auth_response = self.client.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password
            })
            
            if not auth_response.user:
                raise Exception("Registration failed")
            
            # Create user profile
            profile = self.client.table("user_profiles").insert({
                "id": auth_response.user.id,
                "username": user_data.username
            }).execute()
            
            return {
                "access_token": auth_response.session.access_token,
                "refresh_token": auth_response.session.refresh_token,
                "token_type": "bearer",
                "expires_in": auth_response.session.expires_in,
                "user": {
                    "id": auth_response.user.id,
                    "email": auth_response.user.email,
                    "username": user_data.username
                }
            }
            
        except Exception as e:
            raise Exception(f"Registration failed: {str(e)}")
    
    async def login(self, credentials: UserLogin) -> dict:
        """Login with email/password"""
        try:
            auth_response = self.client.auth.sign_in_with_password({
                "email": credentials.email,
                "password": credentials.password
            })
            
            if not auth_response.session:
                raise Exception("Invalid credentials")
            
            # Get user profile
            profile = self.client.table("user_profiles").select(
                "*"
            ).eq("id", auth_response.user.id).single().execute()
            
            return {
                "access_token": auth_response.session.access_token,
                "refresh_token": auth_response.session.refresh_token,
                "token_type": "bearer",
                "expires_in": auth_response.session.expires_in,
                "user": {
                    "id": auth_response.user.id,
                    "email": auth_response.user.email,
                    "username": profile.data["username"] if profile.data else None
                }
            }
            
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")
    
    async def refresh_token(self, refresh_token: str) -> dict:
        """Refresh access token"""
        try:
            auth_response = self.client.auth.refresh_session(refresh_token)
            
            return {
                "access_token": auth_response.session.access_token,
                "refresh_token": auth_response.session.refresh_token,
                "token_type": "bearer",
                "expires_in": auth_response.session.expires_in
            }
            
        except Exception as e:
            raise Exception(f"Token refresh failed: {str(e)}")
```

**Task 2.5.3: Auth Endpoints** (2 hours)
```python
Priority: P0
Estimated Time: 2 hours

# Update app/api/v1/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from supabase import Client
from app.models.auth import (
    UserRegister,
    UserLogin,
    TokenResponse,
    UserProfile
)
from app.services.auth_service import AuthService
from app.core.supabase import get_supabase
from app.api.v1.dependencies import get_current_user

router = APIRouter()

@router.post("/auth/register", response_model=TokenResponse)
async def register(
    user_data: UserRegister,
    supabase: Client = Depends(get_supabase)
):
    """
    Register new user.
    
    - **email**: Valid email address
    - **password**: Min 8 chars, must include uppercase and digit
    - **username**: 3-30 characters, unique
    - Returns: JWT tokens
    """
    try:
        auth = AuthService(supabase)
        result = await auth.register(user_data)
        return TokenResponse(**result)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/auth/login", response_model=TokenResponse)
async def login(
    credentials: UserLogin,
    supabase: Client = Depends(get_supabase)
):
    """
    Login with email and password.
    
    Returns JWT tokens for authentication.
    """
    try:
        auth = AuthService(supabase)
        result = await auth.login(credentials)
        return TokenResponse(**result)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

@router.post("/auth/refresh", response_model=TokenResponse)
async def refresh_token(
    refresh_token: str,
    supabase: Client = Depends(get_supabase)
):
    """Refresh access token using refresh token"""
    try:
        auth = AuthService(supabase)
        result = await auth.refresh_token(refresh_token)
        return TokenResponse(**result)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

@router.get("/auth/me", response_model=UserProfile)
async def get_current_user_profile(
    current_user: dict = Depends(get_current_user),
    supabase: Client = Depends(get_supabase)
):
    """Get current user's profile"""
    try:
        profile = supabase.table("user_profiles").select(
            "*"
        ).eq("id", current_user["id"]).single().execute()
        
        return UserProfile(**profile.data)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
```

**Task 2.5.4: Update main.py with Auth Routes** (30 minutes)
```python
Priority: P0
Estimated Time: 30 minutes

# In app/main.py, add:
from app.api.v1.routes import auth, dreams, videos

app.include_router(
    auth.router,
    prefix=settings.API_PREFIX,
    tags=["Authentication"]
)

app.include_router(
    dreams.router,
    prefix=settings.API_PREFIX,
    tags=["Dreams"]
)

app.include_router(
    videos.router,
    prefix=settings.API_PREFIX,
    tags=["Videos"]
)
```

#### Deliverables:
- [ ] Register endpoint
- [ ] Login endpoint
- [ ] Token refresh endpoint
- [ ] Get profile endpoint
- [ ] Supabase Auth integrated
- [ ] JWT validation working

#### Testing Checklist:
```bash
# Test registration:
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123",
    "username": "testuser"
  }'

# Response:
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "uuid",
    "email": "test@example.com",
    "username": "testuser"
  }
}

# Test login:
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123"
  }'

# Test get profile:
curl http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Check Supabase:
- [ ] Open Supabase → Authentication → Users
- [ ] See your test user
- [ ] Open Table Editor → user_profiles
- [ ] See profile created automatically
```

---

### Epic 2.6: Backend Testing & Documentation

**Duration:** Day 8 (5-6 hours)  
**Priority:** P1  
**Dependencies:** All Phase 2 Epics

#### User Story:
> As a developer, I need comprehensive tests and documentation so that the backend is reliable and maintainable.

#### Acceptance Criteria:
- [ ] API tests cover all endpoints
- [ ] OpenAPI documentation complete
- [ ] README updated with examples
- [ ] Environment setup documented
- [ ] Deployment guide ready

#### Technical Tasks:

**Task 2.6.1: Unit Tests** (2 hours)
```python
Priority: P1
Estimated Time: 2 hours

# tests/test_services/test_claude_service.py
import pytest
from app.services.claude_service import ClaudeService

@pytest.mark.asyncio
async def test_analyze_dream():
    service = ClaudeService()
    result = await service.analyze_dream(
        "I was flying over dark mountains"
    )
    
    assert "video_prompt" in result
    assert "category" in result
    assert result["category"] in ["flight", "gothic", "chase", "transformation", "physics", "liminal"]
    assert len(result["video_prompt"]) >= 100
    assert len(result["video_prompt"]) <= 200

# tests/test_api/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "password": "SecurePass123",
        "username": "testuser"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "user" in data

def test_login():
    # First register
    client.post("/api/v1/auth/register", json={
        "email": "test2@example.com",
        "password": "SecurePass123",
        "username": "testuser2"
    })
    
    # Then login
    response = client.post("/api/v1/auth/login", json={
        "email": "test2@example.com",
        "password": "SecurePass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
```

**Task 2.6.2: API Documentation** (1.5 hours)
```python
Priority: P1
Estimated Time: 1.5 hours

# Enhance OpenAPI docs in routes:
# Each endpoint should have:
# - Detailed description
# - Request/response examples
# - Error responses documented

# Example enhancement in dreams.py:
@router.post(
    "/dreams/analyze",
    response_model=DreamAnalysisResponse,
    responses={
        200: {
            "description": "Dream analyzed successfully",
            "content": {
                "application/json": {
                    "example": {
                        "dream_id": "123e4567-e89b-12d3-a456-426614174000",
                        "video_prompt": "POV gentle rise through dark forest...",
                        "category": "flight",
                        "template_used": "FLIGHT",
                        "confidence": 0.95,
                        "token_usage": {"input": 150, "output": 120},
                        "processing_time_ms": 2341,
                        "created_at": "2025-11-11T12:00:00Z"
                    }
                }
            }
        },
        401: {"description": "Unauthorized - Invalid or missing token"},
        429: {"description": "Rate limit exceeded"},
        500: {"description": "Internal server error"}
    },
    summary="Analyze dream and generate video prompt",
    description="""
    Analyzes dream text using Claude Sonnet 4.5 and generates
    an optimized Runway Gen-3 Alpha prompt.
    
    The analysis includes:
    - Dream category detection (gothic, chase, flight, etc.)
    - Template selection from 6 core templates
    - Optimized 100-150 word prompt generation
    - Confidence score
    
    Requires authentication. Rate limited to 10 requests/minute.
    """
)
```

**Task 2.6.3: Backend README** (1 hour)
```markdown
Priority: P1
Estimated Time: 1 hour

# Create backend/README.md with:
- Setup instructions
- Environment variables
- Running locally
- Running with Docker
- API endpoints list
- Testing instructions
- Deployment guide
```

**Task 2.6.4: API Documentation File** (1 hour)
```markdown
Priority: P1
Estimated Time: 1 hour

# Create docs/API.md with:
- All endpoints documented
- Request/response examples
- Authentication flow
- Error codes
- Rate limits
- Pagination
```

#### Deliverables:
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] OpenAPI docs enhanced
- [ ] Backend README complete
- [ ] API.md documentation

#### Testing Checklist:
```bash
# Run tests:
cd backend
pytest tests/ -v --cov=app

# Expected:
- [ ] All tests pass
- [ ] Coverage > 70%

# Check documentation:
- [ ] Open http://localhost:8000/api/v1/docs
- [ ] All endpoints have descriptions
- [ ] Examples are present
- [ ] Error responses documented
```

---

## 📊 PHASE 2 SUMMARY

### What You've Built (Week 1-2):

✅ **Supabase Backend:**
- PostgreSQL database with RLS
- User authentication (JWT)
- Storage for video thumbnails

✅ **FastAPI REST API:**
- Health check endpoints
- Dream analysis (Claude integration)
- Video generation (Runway integration)
- Combined dream → video endpoint
- User authentication (register/login)
- Rate limiting (10 req/min)

✅ **AI Integration:**
- Claude Sonnet 4.5 with Minimal Prompt System v2.0
- Runway Gen-3 Alpha video generation
- 6 category templates

✅ **Developer Tools:**
- Docker setup
- OpenAPI documentation
- Unit & integration tests
- Comprehensive README

### API Endpoints Summary:

```
GET  /                          → API info
GET  /api/v1/health            → Health check
GET  /api/v1/health/db         → Database health

POST /api/v1/auth/register     → Register user
POST /api/v1/auth/login        → Login user
POST /api/v1/auth/refresh      → Refresh token
GET  /api/v1/auth/me           → Get profile

POST /api/v1/dreams/analyze    → Analyze dream
GET  /api/v1/dreams            → Get dream history
GET  /api/v1/dreams/{id}       → Get dream details

POST /api/v1/videos/generate   → Start video generation
GET  /api/v1/videos/{job_id}   → Get video status

POST /api/v1/dreams/generate-video  → Combined (analyze + generate)
```

### Costs So Far:

- **Supabase:** Free tier (500MB database)
- **Claude API:** ~$0.011 per dream analysis
- **Runway API:** ~$0.05 per 5-second video
- **Total per user dream:** ~$0.061

---

## 🎯 NEXT: PHASE 3 (Mobile App Development)

**Start Date:** Week 3  
**Duration:** 2 weeks (60-72 hours)  
**Goal:** React Native mobile app with full backend integration

You're 33% done! Ready to continue? 🚀

---

**Roadmap Version:** 2.0  
**Last Updated:** 2025-11-11  
**Status:** Phase 2 Ready to Start
