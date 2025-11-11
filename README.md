# 🌙 DreamVision AI

**Turn your dreams into cinematic videos powered by AI**

> An AI-powered mobile application that transforms dream descriptions into stunning 5-second videos using Claude Sonnet 4.5 and Runway Gen-3 Alpha.

---

## 📊 Project Status

**Current Phase:** Phase 2 - Backend Development  
**Progress:** 1/6 phases complete (16.67%)  
**Target Launch:** Week 12

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1: Prompt System & Testing | ✅ COMPLETED | 100% |
| Phase 2: Backend Development | 🔄 IN PROGRESS | 0% |
| Phase 3: Database & Authentication | ⏳ PENDING | 0% |
| Phase 4: Frontend Mobile | ⏳ PENDING | 0% |
| Phase 5: Integration & Testing | ⏳ PENDING | 0% |
| Phase 6: Deployment & Launch | ⏳ PENDING | 0% |

---

## 🏗️ Architecture

```
┌─────────────────┐
│  Mobile App     │
│  (React Native) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│   FastAPI       │─────▶│  Claude Sonnet   │
│   Backend       │      │  4.5 (Anthropic) │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│  PostgreSQL     │      │  Runway Gen-3    │
│  Database       │◀─────│  Alpha (Video)   │
└─────────────────┘      └──────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Framework:** FastAPI (Python 3.11+)
- **Database:** PostgreSQL 15
- **ORM:** SQLAlchemy 2.0 (async)
- **Authentication:** JWT (python-jose)
- **API Documentation:** OpenAPI/Swagger

### AI Services
- **Dream Analysis:** Claude Sonnet 4.5 (Anthropic API)
- **Video Generation:** Runway Gen-3 Alpha (kie.ai API)
- **Prompt System:** Minimal Dream Prompt System v2.0

### Frontend
- **Framework:** React Native (Expo)
- **Language:** TypeScript
- **Navigation:** React Navigation
- **State Management:** Zustand
- **HTTP Client:** Axios

### DevOps
- **Version Control:** GitHub
- **Backend Deploy:** Railway
- **Mobile Build:** Expo EAS
- **Monitoring:** Sentry
- **Uptime:** UptimeRobot

---

## 📂 Repository Structure

```
dreamvision-ai/
├── docs/                           # Documentation
│   ├── ROADMAP.md                 # Development roadmap (12 weeks)
│   ├── API.md                     # API documentation
│   ├── ARCHITECTURE.md            # System architecture
│   ├── DEPLOYMENT.md              # Deployment guide
│   └── CHANGELOG.md               # Version history
│
├── backend/                        # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI app entry
│   │   ├── config.py              # Configuration
│   │   ├── api/                   # API routes
│   │   │   ├── routes/
│   │   │   │   ├── auth.py        # Authentication endpoints
│   │   │   │   ├── dreams.py      # Dream analysis endpoints
│   │   │   │   └── videos.py      # Video generation endpoints
│   │   │   └── dependencies.py    # Route dependencies
│   │   ├── core/                  # Core functionality
│   │   │   ├── security.py        # Auth & password hashing
│   │   │   └── database.py        # Database connection
│   │   ├── models/                # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   ├── dream.py
│   │   │   └── video.py
│   │   ├── schemas/               # Pydantic schemas
│   │   │   ├── auth_schema.py
│   │   │   ├── dream_schema.py
│   │   │   └── video_schema.py
│   │   ├── services/              # Business logic
│   │   │   ├── claude_service.py  # Claude API integration
│   │   │   ├── runway_service.py  # Runway API integration
│   │   │   └── database_service.py
│   │   └── utils/                 # Utilities
│   │       ├── error_handlers.py
│   │       └── validation.py
│   ├── tests/                     # Unit & integration tests
│   ├── migrations/                # Alembic migrations
│   ├── requirements.txt           # Python dependencies
│   ├── .env.example              # Environment variables template
│   └── README.md                  # Backend setup guide
│
├── mobile/                        # React Native mobile app
│   ├── src/
│   │   ├── api/                   # API client
│   │   │   ├── client.ts
│   │   │   ├── authApi.ts
│   │   │   ├── dreamApi.ts
│   │   │   └── videoApi.ts
│   │   ├── components/            # Reusable components
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Card.tsx
│   │   │   ├── DreamCard.tsx
│   │   │   └── LoadingSpinner.tsx
│   │   ├── screens/               # Screen components
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
│   │   ├── navigation/            # Navigation config
│   │   │   └── index.tsx
│   │   ├── store/                 # State management
│   │   │   ├── authStore.ts
│   │   │   └── dreamStore.ts
│   │   ├── types/                 # TypeScript types
│   │   ├── utils/                 # Helper functions
│   │   └── constants/             # Constants (theme, colors)
│   │       └── theme.ts
│   ├── assets/                    # Images, fonts
│   ├── app.json                   # Expo configuration
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md                  # Mobile setup guide
│
├── prompts/                       # Prompt engineering
│   ├── minimal-dream-system-v2.txt  # Claude system prompt
│   ├── templates/                 # Category templates
│   │   ├── gothic.txt
│   │   ├── chase.txt
│   │   ├── flight.txt
│   │   ├── transformation.txt
│   │   ├── physics.txt
│   │   └── liminal.txt
│   └── fail-safe-rules.txt       # Fail-safe ruleset
│
├── workflows/                     # n8n workflows (backup)
│   └── telegram-bot.json         # Working Telegram bot workflow
│
├── .gitignore                    # Git ignore rules
├── LICENSE                       # Project license
└── README.md                     # This file
```

---

## 🚀 Quick Start

### Prerequisites
- **Python:** 3.11+
- **Node.js:** 18+
- **PostgreSQL:** 15+
- **Git:** Latest version
- **Expo CLI:** `npm install -g expo-cli`

### Backend Setup

```bash
# Clone repository
git clone https://github.com/[your-username]/dreamvision-ai.git
cd dreamvision-ai/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload

# API will be available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

### Mobile Setup

```bash
cd mobile

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env and add backend API URL

# Start Expo
npx expo start

# Scan QR code with Expo Go app (iOS/Android)
```

---

## 📖 Documentation

- **[ROADMAP.md](docs/ROADMAP.md)** - Complete 12-week development roadmap
- **[API.md](docs/API.md)** - API endpoint documentation (coming soon)
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System architecture details (coming soon)
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production deployment guide (coming soon)

---

## 🎯 Current Sprint (Week 3)

**Epic 2.1: FastAPI Project Setup** (Nov 11-13)
- [ ] Initialize FastAPI project structure
- [ ] Configure development environment
- [ ] Create health check endpoint
- [ ] Setup environment variables
- [ ] Configure CORS middleware

**Next:** Epic 2.2 - Dream Analysis API integration

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Mobile Tests
```bash
cd mobile
npm test
```

---

## 📊 API Endpoints (Planned)

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/refresh` - Refresh access token

### Dreams
- `POST /api/v1/dreams/analyze` - Analyze dream text
- `POST /api/v1/dreams/generate-video` - Analyze + generate video (combined)
- `GET /api/v1/dreams` - Get user's dream history
- `GET /api/v1/dreams/{id}` - Get single dream details
- `GET /api/v1/dreams/stats` - Get user statistics

### Videos
- `POST /api/v1/videos/generate` - Start video generation
- `GET /api/v1/videos/{job_id}` - Get video generation status

### Health
- `GET /health` - API health check
- `GET /api/v1/version` - API version info

---

## 🔑 Environment Variables

### Backend (.env)
```bash
# API Configuration
API_VERSION=v1
ENVIRONMENT=development  # development | staging | production

# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dreamvision_db

# AI Services
ANTHROPIC_API_KEY=your_anthropic_key
RUNWAY_API_KEY=your_runway_key

# Authentication
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
ALLOWED_ORIGINS=http://localhost:19006,http://localhost:8081
```

### Mobile (.env)
```bash
# API Configuration
EXPO_PUBLIC_API_URL=http://localhost:8000/api/v1

# Environment
EXPO_PUBLIC_ENV=development
```

---

## 📈 Performance Metrics

### Current (Phase 1)
- **Prompt Generation:** ~2-3 seconds
- **Token Usage:** ~3,000 tokens per dream
- **Cost per Dream:** $0.011 (91.7% reduction from v1)
- **Video Quality:** 9-9.5/10

### Targets (Phase 6)
- **API Response Time:** <5 seconds
- **Video Generation:** ~2 minutes
- **App Launch Time:** <3 seconds
- **Concurrent Users:** 100+

---

## 🛡️ Security

- **Authentication:** JWT tokens with secure secret key
- **Password Hashing:** Bcrypt
- **Rate Limiting:** 10 requests/minute per IP
- **CORS:** Configured for specific origins only
- **Environment Variables:** Never committed to git
- **API Keys:** Stored securely in environment

---

## 🤝 Contributing

This is currently a solo project, but contributions are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/epic-2.1`
3. Commit your changes: `git commit -m 'Add FastAPI setup'`
4. Push to the branch: `git push origin feature/epic-2.1`
5. Open a Pull Request

---

## 📝 Git Workflow

### Branch Naming
- **Feature branches:** `feature/epic-2.1-fastapi-setup`
- **Bug fixes:** `fix/rate-limiting-bug`
- **Hotfix:** `hotfix/critical-auth-issue`

### Commit Messages
```
feat: add dream analysis endpoint
fix: resolve token expiration issue
docs: update API documentation
test: add integration tests for video generation
refactor: optimize database queries
```

---

## 📅 Version History

### v0.1.0 (Phase 1 - Completed)
- ✅ Minimal Dream Prompt System v2.0
- ✅ 6 core templates (Gothic, Chase, Flight, Transformation, Physics, Liminal)
- ✅ n8n workflow with Telegram bot
- ✅ Claude Sonnet 4.5 integration
- ✅ Runway Gen-3 Alpha integration
- ✅ Cost optimization (91.7% reduction)

### v0.2.0 (Phase 2 - In Progress)
- 🔄 FastAPI backend
- 🔄 Dream analysis API
- 🔄 Video generation API
- 🔄 API documentation

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/[your-username]/dreamvision-ai/issues)
- **Email:** your.email@example.com
- **Documentation:** [docs/](docs/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Anthropic** - Claude Sonnet 4.5 API
- **Runway ML** - Gen-3 Alpha video generation
- **FastAPI** - Modern Python web framework
- **React Native** - Mobile framework
- **Expo** - React Native toolchain

---

## 🎯 Roadmap Links

- [Complete 12-Week Roadmap](docs/ROADMAP.md)
- [Current Sprint (Week 3)](docs/ROADMAP.md#phase-2-backend-development)
- [Architecture Decisions](docs/ARCHITECTURE.md) (coming soon)

---

**Built with ❤️ and AI**

**Status:** 🚧 Under Active Development

**Last Updated:** 2025-11-11
