# 🌙 DreamVision AI

**Turn your dreams into cinematic videos powered by AI**

> An AI-powered mobile application that transforms dream descriptions into stunning 5-second videos using Claude Sonnet 4.5 and Runway Gen-3 Alpha.

---

## 📊 Project Status

**Current Phase:** Phase 2 - Backend Development  
**Progress:** Phase 1 complete (16.67%)  
**Target Launch:** Week 6 (Core MVP) | Week 8 (Full-Featured)

| Phase | Duration | Status | Progress |
|-------|----------|--------|----------|
| Phase 1: Prompt System & Testing | Week 0 | ✅ COMPLETED | 100% |
| Phase 2: Backend + Supabase | Week 1-2 | 🔄 READY TO START | 0% |
| Phase 3: Mobile App (React Native) | Week 3-4 | ⏳ PENDING | 0% |
| Phase 4: Integration & Polish | Week 5 | ⏳ PENDING | 0% |
| Phase 5: Deployment & Launch | Week 6 | ⏳ PENDING | 0% |
| Phase 6: Web PWA (Optional) | Week 7 | 📦 OPTIONAL | 0% |
| Phase 7: Analytics (Optional) | Week 8 | 📦 OPTIONAL | 0% |

---

## 🏗️ Architecture

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

## 🛠️ Tech Stack

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
- **Prompt System:** Minimal Dream Prompt System v2.0

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

---

## 📖 Documentation

- **[ROADMAP-v2.md](docs/ROADMAP-v2.md)** - Week 1-2: Backend Development
- **[ROADMAP-v2-PART2.md](docs/ROADMAP-v2-PART2.md)** - Week 3-8: Mobile + Deployment
- **[ROADMAP-NAVIGATION.md](docs/ROADMAP-NAVIGATION.md)** - How to navigate the roadmap
- **[GITHUB-SETUP.md](docs/GITHUB-SETUP.md)** - Git workflow & best practices
- **[QUICK-START.md](docs/QUICK-START.md)** - Quick reference guide

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Supabase Account
- Anthropic API Key
- Runway API Key

### Backend Setup (Week 1-2)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
uvicorn app.main:app --reload
```

### Mobile Setup (Week 3-4)

```bash
cd mobile
npm install
cp .env.example .env
npx expo start
```

---

## 📊 API Endpoints

- `GET /api/v1/health` - Health check
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/dreams/generate-video` - Analyze dream + generate video
- `GET /api/v1/videos/{job_id}` - Get video status

---

## 💰 Cost per Dream

| Service | Cost |
|---------|------|
| Claude Sonnet 4.5 | $0.011 |
| Runway Gen-3 Alpha | $0.050 |
| **Total** | **$0.061** |

---

## 🎯 Next Steps

**Tomorrow (Week 1, Day 1):**
1. Open `docs/ROADMAP-v2.md`
2. Start Epic 2.1: Supabase Setup
3. Complete Task 2.1.1: Create Supabase project

---

**Built with ❤️ and AI**

**Status:** 🚧 Under Active Development  
**Last Updated:** 2025-11-17  
**Current Focus:** Backend Development (Week 1-2)
