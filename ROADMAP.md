# 🗺️ AI Destekli Rüya Video Uygulaması - Development Roadmap

## 📊 Project Overview

**Project Name:** DreamVision AI  
**Current Phase:** Phase 1 ✅ COMPLETED (Prompt System + n8n Workflow)  
**Next Phase:** Phase 2 → Backend Development  
**Target:** MVP Launch in 8-10 weeks

---

## 🎯 Phase Status

| Phase | Status | Duration | Completion |
|-------|--------|----------|------------|
| Phase 1: Prompt System & Testing | ✅ COMPLETED | 2 weeks | 100% |
| Phase 2: Backend Development | 🔄 READY | 3 weeks | 0% |
| Phase 3: Database & Auth | ⏳ PENDING | 2 weeks | 0% |
| Phase 4: Frontend Mobile | ⏳ PENDING | 3 weeks | 0% |
| Phase 5: Integration & Testing | ⏳ PENDING | 1 week | 0% |
| Phase 6: Deployment & Launch | ⏳ PENDING | 1 week | 0% |

---

# 📋 EPIC BREAKDOWN

## ✅ PHASE 1: Prompt System & Testing (COMPLETED)

### Epic 1.1: Prompt Engineering ✅
**Status:** COMPLETED  
**Duration:** 1 week  
**Owner:** AI Team

#### Achievements:
- ✅ Claude Sonnet 4.5 system prompt developed
- ✅ 6 core templates (Gothic, Chase, Flight, Transformation, Physics, Liminal)
- ✅ 11 fail-safe rules implemented
- ✅ Token optimization (17K → 3K, 82% reduction)
- ✅ Cost optimization ($0.132 → $0.011, 91.7% reduction)

#### Deliverables:
- ✅ Minimal Dream Prompt System v2.0
- ✅ Template library
- ✅ Fail-safe ruleset

---

### Epic 1.2: Workflow Automation ✅
**Status:** COMPLETED  
**Duration:** 1 week  
**Owner:** DevOps Team

#### Achievements:
- ✅ n8n workflow configured
- ✅ Telegram bot integration
- ✅ Claude API integration (Anthropic)
- ✅ Runway Gen-3 Alpha integration (kie.ai)
- ✅ 3 category tests (all 9+ quality)

#### Deliverables:
- ✅ Working Telegram bot
- ✅ Automated dream → video pipeline
- ✅ Quality metrics (9-9.5/10)

---

## 🔄 PHASE 2: Backend Development (CURRENT)

**Timeline:** Week 3-5 (3 weeks)  
**Priority:** P0 (Critical Path)  
**Dependencies:** None

---

### Epic 2.1: FastAPI Project Setup

**Priority:** P0  
**Duration:** 3 days  
**Owner:** Backend Team

#### User Story:
> As a developer, I need a properly structured FastAPI project so that I can build scalable API endpoints.

#### Acceptance Criteria:
- [ ] FastAPI project initialized with proper folder structure
- [ ] Development environment configured
- [ ] Hot reload working
- [ ] Basic health check endpoint responds
- [ ] API documentation auto-generated (Swagger/ReDoc)

#### Technical Tasks:

**Task 2.1.1: Project Initialization** (4 hours)
```bash
Priority: P0
Dependencies: None

Subtasks:
- [ ] Create project directory structure
  ├── app/
  │   ├── __init__.py
  │   ├── main.py
  │   ├── config.py
  │   ├── api/
  │   │   ├── __init__.py
  │   │   ├── routes/
  │   │   └── dependencies.py
  │   ├── core/
  │   │   ├── __init__.py
  │   │   ├── security.py
  │   │   └── config.py
  │   ├── models/
  │   ├── schemas/
  │   ├── services/
  │   └── utils/
  ├── tests/
  ├── requirements.txt
  ├── .env.example
  └── README.md

- [ ] Initialize git repository
- [ ] Create .gitignore (Python, .env, __pycache__)
- [ ] Setup virtual environment
```

**Task 2.1.2: Dependencies Installation** (2 hours)
```bash
Priority: P0
Dependencies: 2.1.1

Subtasks:
- [ ] Create requirements.txt with:
  - fastapi==0.104.1
  - uvicorn[standard]==0.24.0
  - pydantic==2.5.0
  - pydantic-settings==2.1.0
  - python-dotenv==1.0.0
  - httpx==0.25.2
  - anthropic==0.7.7
  - python-multipart==0.0.6

- [ ] Install dependencies: pip install -r requirements.txt
- [ ] Verify installations
```

**Task 2.1.3: Basic FastAPI App** (3 hours)
```python
Priority: P0
Dependencies: 2.1.2

Subtasks:
- [ ] Create main.py with basic FastAPI app
- [ ] Configure CORS middleware
- [ ] Add health check endpoint: GET /health
- [ ] Add version endpoint: GET /api/v1/version
- [ ] Test with uvicorn: uvicorn app.main:app --reload
- [ ] Verify Swagger docs at /docs
```

**Task 2.1.4: Environment Configuration** (2 hours)
```bash
Priority: P0
Dependencies: 2.1.3

Subtasks:
- [ ] Create .env.example with required variables:
  - API_VERSION
  - ENVIRONMENT (dev/staging/prod)
  - ANTHROPIC_API_KEY
  - RUNWAY_API_KEY
  - ALLOWED_ORIGINS

- [ ] Create config.py with Pydantic Settings
- [ ] Load and validate environment variables
- [ ] Document all environment variables in README
```

#### Deliverables:
- [ ] Working FastAPI application
- [ ] requirements.txt
- [ ] .env.example
- [ ] README.md with setup instructions
- [ ] Health check endpoint functional

#### Testing Checklist:
- [ ] `curl http://localhost:8000/health` returns 200
- [ ] Swagger UI accessible at `/docs`
- [ ] Hot reload works (change main.py and verify)
- [ ] Environment variables load correctly

---

### Epic 2.2: Dream Analysis API

**Priority:** P0  
**Duration:** 5 days  
**Owner:** Backend Team  
**Dependencies:** Epic 2.1

#### User Story:
> As a mobile app, I need to send dream text and receive a Runway-ready prompt so that I can generate dream videos.

#### Acceptance Criteria:
- [ ] POST /api/v1/dreams/analyze accepts dream text
- [ ] Claude API integrated with minimal prompt system
- [ ] Response includes optimized video prompt
- [ ] Response time < 5 seconds
- [ ] Error handling for API failures
- [ ] Rate limiting implemented

#### Technical Tasks:

**Task 2.2.1: Claude Service Layer** (6 hours)
```python
Priority: P0
Dependencies: Epic 2.1

Subtasks:
- [ ] Create services/claude_service.py
- [ ] Implement ClaudeService class
- [ ] Load Minimal Dream Prompt System v2.0
- [ ] Create analyze_dream() method
- [ ] Handle API errors and retries
- [ ] Add response validation
- [ ] Log token usage and costs

Code Structure:
class ClaudeService:
    def __init__(self, api_key: str, system_prompt: str)
    def analyze_dream(self, dream_text: str) -> PromptResponse
    def _validate_response(self, response: dict) -> bool
    def _handle_error(self, error: Exception) -> ErrorResponse
```

**Task 2.2.2: Dream Analysis Schema** (3 hours)
```python
Priority: P0
Dependencies: 2.2.1

Subtasks:
- [ ] Create schemas/dream_schema.py
- [ ] Define DreamAnalysisRequest model:
  - dream_text: str (max 2000 chars)
  - user_id: Optional[str]
  - metadata: Optional[dict]

- [ ] Define PromptResponse model:
  - video_prompt: str
  - category: str
  - confidence: float
  - template_used: str
  - token_usage: dict

- [ ] Add validation rules
- [ ] Document schema in README
```

**Task 2.2.3: Dream Analysis Endpoint** (4 hours)
```python
Priority: P0
Dependencies: 2.2.1, 2.2.2

Subtasks:
- [ ] Create api/routes/dreams.py
- [ ] Implement POST /api/v1/dreams/analyze
- [ ] Validate request body
- [ ] Call ClaudeService
- [ ] Return PromptResponse
- [ ] Add error handling
- [ ] Add request/response logging

Endpoint Spec:
POST /api/v1/dreams/analyze
Body: {
  "dream_text": "I was flying over a dark forest...",
  "user_id": "optional"
}
Response: {
  "video_prompt": "POV continuous glide through twisted...",
  "category": "flight",
  "confidence": 0.95,
  "template_used": "FLIGHT",
  "token_usage": {"input": 150, "output": 120},
  "processing_time_ms": 2341
}
```

**Task 2.2.4: Rate Limiting** (3 hours)
```python
Priority: P1
Dependencies: 2.2.3

Subtasks:
- [ ] Install slowapi: pip install slowapi
- [ ] Configure rate limiter (10 requests/minute per IP)
- [ ] Add rate limit decorator to endpoint
- [ ] Return 429 with Retry-After header
- [ ] Log rate limit violations
- [ ] Test with concurrent requests
```

**Task 2.2.5: Integration Testing** (4 hours)
```bash
Priority: P0
Dependencies: 2.2.4

Subtasks:
- [ ] Create tests/test_dream_analysis.py
- [ ] Test valid dream text → success
- [ ] Test empty dream text → 400 error
- [ ] Test very long text (>2000 chars) → 400 error
- [ ] Test Claude API failure → proper error response
- [ ] Test rate limiting
- [ ] Measure response times (target: <5s)
```

#### Deliverables:
- [ ] `/api/v1/dreams/analyze` endpoint
- [ ] ClaudeService integration
- [ ] Request/response schemas
- [ ] Rate limiting
- [ ] Integration tests
- [ ] API documentation

#### Testing Checklist:
```bash
# Valid request
curl -X POST http://localhost:8000/api/v1/dreams/analyze \
  -H "Content-Type: application/json" \
  -d '{"dream_text": "I was flying over mountains"}'

# Expected: 200 OK with video_prompt

# Invalid request (empty text)
curl -X POST http://localhost:8000/api/v1/dreams/analyze \
  -H "Content-Type: application/json" \
  -d '{"dream_text": ""}'

# Expected: 400 Bad Request

# Rate limit test
for i in {1..15}; do
  curl -X POST http://localhost:8000/api/v1/dreams/analyze \
    -H "Content-Type: application/json" \
    -d '{"dream_text": "Test '$i'"}'
done

# Expected: First 10 succeed, next 5 return 429
```

---

### Epic 2.3: Video Generation API

**Priority:** P0  
**Duration:** 5 days  
**Owner:** Backend Team  
**Dependencies:** Epic 2.2

#### User Story:
> As a mobile app, I need to request video generation and poll for completion so that users can see their dream videos.

#### Acceptance Criteria:
- [ ] POST /api/v1/videos/generate accepts prompt and starts generation
- [ ] GET /api/v1/videos/{job_id} returns status
- [ ] Runway Gen-3 Alpha integrated
- [ ] Job status tracking (pending/processing/completed/failed)
- [ ] Video URL returned when ready
- [ ] Webhook support for completion notification

#### Technical Tasks:

**Task 2.3.1: Runway Service Layer** (6 hours)
```python
Priority: P0
Dependencies: Epic 2.2

Subtasks:
- [ ] Create services/runway_service.py
- [ ] Implement RunwayService class
- [ ] Create generate_video() method
- [ ] Create check_status() method
- [ ] Create get_video_url() method
- [ ] Handle API errors and retries
- [ ] Log generation costs

Code Structure:
class RunwayService:
    def __init__(self, api_key: str, base_url: str)
    def generate_video(self, prompt: str, duration: int = 5) -> JobResponse
    def check_status(self, job_id: str) -> StatusResponse
    def get_video_url(self, job_id: str) -> str
    def _handle_error(self, error: Exception) -> ErrorResponse
```

**Task 2.3.2: Video Generation Schema** (3 hours)
```python
Priority: P0
Dependencies: 2.3.1

Subtasks:
- [ ] Create schemas/video_schema.py
- [ ] Define VideoGenerationRequest model:
  - video_prompt: str
  - duration: int (default 5)
  - user_id: Optional[str]
  - dream_analysis_id: Optional[str]

- [ ] Define JobResponse model:
  - job_id: str
  - status: str (pending/processing/completed/failed)
  - created_at: datetime
  - estimated_completion_time: Optional[datetime]

- [ ] Define VideoResponse model:
  - job_id: str
  - status: str
  - video_url: Optional[str]
  - thumbnail_url: Optional[str]
  - duration: int
  - created_at: datetime
  - completed_at: Optional[datetime]

- [ ] Add validation rules
```

**Task 2.3.3: Video Generation Endpoint** (5 hours)
```python
Priority: P0
Dependencies: 2.3.1, 2.3.2

Subtasks:
- [ ] Create api/routes/videos.py
- [ ] Implement POST /api/v1/videos/generate
- [ ] Validate request body
- [ ] Call RunwayService.generate_video()
- [ ] Return job_id immediately (async processing)
- [ ] Add error handling
- [ ] Add request logging

Endpoint Spec:
POST /api/v1/videos/generate
Body: {
  "video_prompt": "POV continuous glide through...",
  "duration": 5,
  "user_id": "optional"
}
Response: {
  "job_id": "run_abc123xyz",
  "status": "pending",
  "created_at": "2025-11-11T10:30:00Z",
  "estimated_completion_time": "2025-11-11T10:32:00Z"
}
```

**Task 2.3.4: Job Status Endpoint** (4 hours)
```python
Priority: P0
Dependencies: 2.3.3

Subtasks:
- [ ] Implement GET /api/v1/videos/{job_id}
- [ ] Call RunwayService.check_status()
- [ ] Return current status
- [ ] Include video_url when completed
- [ ] Handle job not found (404)
- [ ] Add caching for completed jobs (1 hour)

Endpoint Spec:
GET /api/v1/videos/{job_id}
Response (pending):
{
  "job_id": "run_abc123xyz",
  "status": "processing",
  "progress": 45,
  "created_at": "2025-11-11T10:30:00Z"
}

Response (completed):
{
  "job_id": "run_abc123xyz",
  "status": "completed",
  "video_url": "https://cdn.runwayml.com/videos/...",
  "thumbnail_url": "https://cdn.runwayml.com/thumbs/...",
  "duration": 5,
  "created_at": "2025-11-11T10:30:00Z",
  "completed_at": "2025-11-11T10:32:15Z"
}
```

**Task 2.3.5: Combined Dream-to-Video Endpoint** (4 hours)
```python
Priority: P1
Dependencies: 2.3.4

Subtasks:
- [ ] Create POST /api/v1/dreams/generate-video
- [ ] Accept dream_text in request
- [ ] Call ClaudeService (analyze dream)
- [ ] Call RunwayService (generate video)
- [ ] Return both prompt and job_id
- [ ] Add error handling for both services

Endpoint Spec:
POST /api/v1/dreams/generate-video
Body: {
  "dream_text": "I was flying over mountains"
}
Response: {
  "dream_analysis": {
    "video_prompt": "POV continuous glide...",
    "category": "flight",
    "template_used": "FLIGHT"
  },
  "video_generation": {
    "job_id": "run_abc123xyz",
    "status": "pending",
    "estimated_completion_time": "2025-11-11T10:32:00Z"
  }
}
```

**Task 2.3.6: Integration Testing** (4 hours)
```bash
Priority: P0
Dependencies: 2.3.5

Subtasks:
- [ ] Create tests/test_video_generation.py
- [ ] Test video generation → returns job_id
- [ ] Test job status polling → returns correct status
- [ ] Test completed job → returns video URL
- [ ] Test job not found → 404 error
- [ ] Test Runway API failure → proper error response
- [ ] Test end-to-end: dream text → video URL
```

#### Deliverables:
- [ ] `/api/v1/videos/generate` endpoint
- [ ] `/api/v1/videos/{job_id}` endpoint
- [ ] `/api/v1/dreams/generate-video` endpoint (combined)
- [ ] RunwayService integration
- [ ] Job status tracking
- [ ] Integration tests

---

### Epic 2.4: API Documentation & Error Handling

**Priority:** P1  
**Duration:** 2 days  
**Owner:** Backend Team  
**Dependencies:** Epic 2.3

#### User Story:
> As a frontend developer, I need comprehensive API documentation so that I can integrate the backend easily.

#### Acceptance Criteria:
- [ ] OpenAPI/Swagger documentation complete
- [ ] All endpoints documented with examples
- [ ] Error codes documented
- [ ] Rate limits documented
- [ ] Authentication flow documented (ready for Phase 3)

#### Technical Tasks:

**Task 2.4.1: OpenAPI Enhancement** (4 hours)
```python
Priority: P1
Dependencies: Epic 2.3

Subtasks:
- [ ] Add detailed descriptions to all endpoints
- [ ] Add request/response examples
- [ ] Add error response examples
- [ ] Configure Swagger UI theme
- [ ] Add API version info
- [ ] Test Swagger UI at /docs
```

**Task 2.4.2: Error Handling Standardization** (4 hours)
```python
Priority: P1
Dependencies: 2.4.1

Subtasks:
- [ ] Create utils/error_handlers.py
- [ ] Define standard error response format:
  {
    "error": {
      "code": "DREAM_ANALYSIS_FAILED",
      "message": "Failed to analyze dream",
      "details": "Claude API returned 500",
      "timestamp": "2025-11-11T10:30:00Z",
      "request_id": "req_abc123"
    }
  }

- [ ] Create custom exception classes
- [ ] Add global exception handler
- [ ] Map HTTP status codes
- [ ] Add request_id to all responses
```

**Task 2.4.3: README Documentation** (3 hours)
```markdown
Priority: P1
Dependencies: 2.4.2

Subtasks:
- [ ] Update README.md with:
  - Project overview
  - Tech stack
  - Setup instructions
  - Environment variables
  - API endpoints list
  - Example requests/responses
  - Error codes
  - Rate limits
  - Development workflow

- [ ] Add architecture diagram
- [ ] Add API flow diagram
- [ ] Add troubleshooting section
```

#### Deliverables:
- [ ] Complete OpenAPI documentation
- [ ] Standardized error handling
- [ ] Comprehensive README
- [ ] API flow diagrams

---

## ⏳ PHASE 3: Database & Authentication

**Timeline:** Week 6-7 (2 weeks)  
**Priority:** P0 (Critical Path)  
**Dependencies:** Phase 2

---

### Epic 3.1: Database Setup

**Priority:** P0  
**Duration:** 4 days  
**Owner:** Backend Team  
**Dependencies:** Phase 2

#### User Story:
> As a system, I need to persist user data, dream history, and video metadata so that users can access their past dreams.

#### Acceptance Criteria:
- [ ] PostgreSQL database configured
- [ ] Database migrations working
- [ ] ORM (SQLAlchemy) configured
- [ ] Connection pooling configured
- [ ] Database backup strategy defined

#### Technical Tasks:

**Task 3.1.1: PostgreSQL Setup** (3 hours)
```bash
Priority: P0
Dependencies: Phase 2

Subtasks:
- [ ] Install PostgreSQL locally (or Docker)
- [ ] Create database: dreamvision_db
- [ ] Create database user with limited privileges
- [ ] Configure connection string in .env
- [ ] Test connection
```

**Task 3.1.2: SQLAlchemy Configuration** (4 hours)
```python
Priority: P0
Dependencies: 3.1.1

Subtasks:
- [ ] Install dependencies:
  - sqlalchemy==2.0.23
  - alembic==1.13.0
  - asyncpg==0.29.0

- [ ] Create core/database.py
- [ ] Configure async engine
- [ ] Configure session factory
- [ ] Add database dependency for routes
- [ ] Test database connection
```

**Task 3.1.3: Database Models** (6 hours)
```python
Priority: P0
Dependencies: 3.1.2

Subtasks:
- [ ] Create models/user.py:
  - id (UUID, primary key)
  - email (unique, indexed)
  - username (unique)
  - created_at
  - updated_at
  - is_active
  - subscription_tier (free/premium)

- [ ] Create models/dream.py:
  - id (UUID, primary key)
  - user_id (foreign key)
  - dream_text (text)
  - video_prompt (text)
  - category (string)
  - template_used (string)
  - created_at

- [ ] Create models/video.py:
  - id (UUID, primary key)
  - dream_id (foreign key)
  - job_id (string, unique, indexed)
  - status (enum: pending/processing/completed/failed)
  - video_url (string, nullable)
  - thumbnail_url (string, nullable)
  - duration (integer)
  - created_at
  - completed_at (nullable)

- [ ] Add relationships between models
- [ ] Add indexes for common queries
```

**Task 3.1.4: Alembic Migrations** (3 hours)
```bash
Priority: P0
Dependencies: 3.1.3

Subtasks:
- [ ] Initialize Alembic: alembic init migrations
- [ ] Configure alembic.ini
- [ ] Create initial migration: alembic revision --autogenerate
- [ ] Review migration file
- [ ] Run migration: alembic upgrade head
- [ ] Test rollback: alembic downgrade -1
- [ ] Document migration workflow
```

**Task 3.1.5: Database Service Layer** (4 hours)
```python
Priority: P0
Dependencies: 3.1.4

Subtasks:
- [ ] Create services/database_service.py
- [ ] Implement CRUD operations for User
- [ ] Implement CRUD operations for Dream
- [ ] Implement CRUD operations for Video
- [ ] Add query methods (get_user_dreams, get_video_by_job_id)
- [ ] Add pagination support
- [ ] Test all CRUD operations
```

#### Deliverables:
- [ ] PostgreSQL database configured
- [ ] SQLAlchemy models defined
- [ ] Alembic migrations working
- [ ] Database service layer
- [ ] CRUD operations tested

---

### Epic 3.2: User Authentication

**Priority:** P0  
**Duration:** 4 days  
**Owner:** Backend Team  
**Dependencies:** Epic 3.1

#### User Story:
> As a user, I need to register and login so that I can save my dream history.

#### Acceptance Criteria:
- [ ] User registration endpoint
- [ ] User login endpoint (JWT tokens)
- [ ] Password hashing (bcrypt)
- [ ] JWT token validation middleware
- [ ] Refresh token support
- [ ] Protected endpoints require authentication

#### Technical Tasks:

**Task 3.2.1: Authentication Dependencies** (2 hours)
```bash
Priority: P0
Dependencies: Epic 3.1

Subtasks:
- [ ] Install dependencies:
  - python-jose[cryptography]==3.3.0
  - passlib[bcrypt]==1.7.4
  - python-multipart==0.0.6

- [ ] Test installations
```

**Task 3.2.2: Password Hashing** (3 hours)
```python
Priority: P0
Dependencies: 3.2.1

Subtasks:
- [ ] Create core/security.py
- [ ] Implement password hashing (bcrypt)
- [ ] Implement password verification
- [ ] Add password strength validation
- [ ] Test hashing/verification
```

**Task 3.2.3: JWT Token Service** (4 hours)
```python
Priority: P0
Dependencies: 3.2.2

Subtasks:
- [ ] Add JWT configuration to .env:
  - SECRET_KEY (generate secure random key)
  - ALGORITHM (HS256)
  - ACCESS_TOKEN_EXPIRE_MINUTES (30)
  - REFRESH_TOKEN_EXPIRE_DAYS (7)

- [ ] Implement create_access_token()
- [ ] Implement create_refresh_token()
- [ ] Implement verify_token()
- [ ] Add token expiration handling
- [ ] Test token creation/validation
```

**Task 3.2.4: Registration Endpoint** (4 hours)
```python
Priority: P0
Dependencies: 3.2.3

Subtasks:
- [ ] Create api/routes/auth.py
- [ ] Implement POST /api/v1/auth/register
- [ ] Validate email format
- [ ] Check email uniqueness
- [ ] Hash password
- [ ] Create user in database
- [ ] Return access token and refresh token
- [ ] Add error handling

Endpoint Spec:
POST /api/v1/auth/register
Body: {
  "email": "user@example.com",
  "username": "dreamuser",
  "password": "SecurePass123!"
}
Response: {
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "username": "dreamuser"
  },
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer"
}
```

**Task 3.2.5: Login Endpoint** (3 hours)
```python
Priority: P0
Dependencies: 3.2.4

Subtasks:
- [ ] Implement POST /api/v1/auth/login
- [ ] Validate credentials
- [ ] Verify password
- [ ] Generate tokens
- [ ] Return tokens
- [ ] Add error handling (invalid credentials)

Endpoint Spec:
POST /api/v1/auth/login
Body: {
  "email": "user@example.com",
  "password": "SecurePass123!"
}
Response: {
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer"
}
```

**Task 3.2.6: Token Refresh Endpoint** (2 hours)
```python
Priority: P1
Dependencies: 3.2.5

Subtasks:
- [ ] Implement POST /api/v1/auth/refresh
- [ ] Validate refresh token
- [ ] Generate new access token
- [ ] Return new access token
- [ ] Add error handling

Endpoint Spec:
POST /api/v1/auth/refresh
Body: {
  "refresh_token": "eyJ..."
}
Response: {
  "access_token": "eyJ...",
  "token_type": "bearer"
}
```

**Task 3.2.7: Authentication Middleware** (4 hours)
```python
Priority: P0
Dependencies: 3.2.6

Subtasks:
- [ ] Create api/dependencies.py
- [ ] Implement get_current_user() dependency
- [ ] Extract token from Authorization header
- [ ] Verify token
- [ ] Load user from database
- [ ] Handle expired tokens (401)
- [ ] Handle invalid tokens (401)
- [ ] Test middleware with protected routes
```

**Task 3.2.8: Protect Existing Endpoints** (3 hours)
```python
Priority: P0
Dependencies: 3.2.7

Subtasks:
- [ ] Add authentication to POST /api/v1/dreams/analyze
- [ ] Add authentication to POST /api/v1/videos/generate
- [ ] Add authentication to POST /api/v1/dreams/generate-video
- [ ] Save user_id with dream records
- [ ] Save user_id with video records
- [ ] Test authenticated requests
```

#### Deliverables:
- [ ] User registration endpoint
- [ ] User login endpoint
- [ ] JWT token authentication
- [ ] Password hashing
- [ ] Protected API endpoints
- [ ] Authentication middleware

---

### Epic 3.3: User Dream History

**Priority:** P1  
**Duration:** 2 days  
**Owner:** Backend Team  
**Dependencies:** Epic 3.2

#### User Story:
> As a user, I want to view my past dreams and videos so that I can revisit them.

#### Acceptance Criteria:
- [ ] GET /api/v1/dreams returns user's dream history
- [ ] Pagination support (20 items per page)
- [ ] Filtering by category
- [ ] Sorting by date (newest first)
- [ ] Dream details include video status

#### Technical Tasks:

**Task 3.3.1: Dream History Endpoint** (4 hours)
```python
Priority: P1
Dependencies: Epic 3.2

Subtasks:
- [ ] Create GET /api/v1/dreams endpoint
- [ ] Require authentication
- [ ] Implement pagination (page, limit)
- [ ] Filter by category (optional)
- [ ] Sort by created_at DESC
- [ ] Include video status in response
- [ ] Add total count in response

Endpoint Spec:
GET /api/v1/dreams?page=1&limit=20&category=flight
Headers: {
  "Authorization": "Bearer eyJ..."
}
Response: {
  "dreams": [
    {
      "id": "uuid",
      "dream_text": "I was flying...",
      "video_prompt": "POV continuous glide...",
      "category": "flight",
      "template_used": "FLIGHT",
      "created_at": "2025-11-11T10:30:00Z",
      "video": {
        "status": "completed",
        "video_url": "https://...",
        "thumbnail_url": "https://..."
      }
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 45,
    "pages": 3
  }
}
```

**Task 3.3.2: Single Dream Details** (2 hours)
```python
Priority: P1
Dependencies: 3.3.1

Subtasks:
- [ ] Create GET /api/v1/dreams/{dream_id}
- [ ] Require authentication
- [ ] Verify dream belongs to user
- [ ] Return dream details
- [ ] Include full video information
- [ ] Handle not found (404)

Endpoint Spec:
GET /api/v1/dreams/{dream_id}
Headers: {
  "Authorization": "Bearer eyJ..."
}
Response: {
  "id": "uuid",
  "dream_text": "I was flying over mountains...",
  "video_prompt": "POV continuous glide through...",
  "category": "flight",
  "template_used": "FLIGHT",
  "confidence": 0.95,
  "created_at": "2025-11-11T10:30:00Z",
  "video": {
    "id": "uuid",
    "job_id": "run_abc123",
    "status": "completed",
    "video_url": "https://...",
    "thumbnail_url": "https://...",
    "duration": 5,
    "created_at": "2025-11-11T10:30:00Z",
    "completed_at": "2025-11-11T10:32:15Z"
  }
}
```

**Task 3.3.3: Dream Statistics** (3 hours)
```python
Priority: P2
Dependencies: 3.3.2

Subtasks:
- [ ] Create GET /api/v1/dreams/stats
- [ ] Require authentication
- [ ] Calculate total dreams
- [ ] Calculate dreams by category
- [ ] Calculate total videos generated
- [ ] Return statistics

Endpoint Spec:
GET /api/v1/dreams/stats
Headers: {
  "Authorization": "Bearer eyJ..."
}
Response: {
  "total_dreams": 45,
  "total_videos": 42,
  "dreams_by_category": {
    "flight": 12,
    "chase": 8,
    "gothic": 15,
    "transformation": 5,
    "physics": 3,
    "liminal": 2
  },
  "most_used_template": "GOTHIC",
  "first_dream_date": "2025-10-01T00:00:00Z",
  "last_dream_date": "2025-11-11T10:30:00Z"
}
```

#### Deliverables:
- [ ] Dream history endpoint with pagination
- [ ] Single dream details endpoint
- [ ] Dream statistics endpoint
- [ ] User-scoped queries

---

## ⏳ PHASE 4: Frontend Mobile (React Native + Expo)

**Timeline:** Week 8-10 (3 weeks)  
**Priority:** P0 (Critical Path)  
**Dependencies:** Phase 3

---

### Epic 4.1: Expo Project Setup

**Priority:** P0  
**Duration:** 2 days  
**Owner:** Frontend Team  
**Dependencies:** Phase 3

#### User Story:
> As a developer, I need a properly configured React Native project so that I can build mobile screens.

#### Acceptance Criteria:
- [ ] Expo project initialized
- [ ] TypeScript configured
- [ ] Navigation configured (React Navigation)
- [ ] State management configured (Zustand or Context API)
- [ ] API client configured (Axios)
- [ ] Development environment working (iOS/Android simulators)

#### Technical Tasks:

**Task 4.1.1: Project Initialization** (3 hours)
```bash
Priority: P0
Dependencies: Phase 3

Subtasks:
- [ ] Create Expo project: npx create-expo-app dreamvision-mobile
- [ ] Choose TypeScript template
- [ ] Install dependencies:
  - @react-navigation/native
  - @react-navigation/native-stack
  - @react-navigation/bottom-tabs
  - axios
  - zustand
  - react-native-safe-area-context
  - react-native-screens
  - expo-secure-store (for tokens)

- [ ] Test on iOS simulator
- [ ] Test on Android emulator
- [ ] Configure ESLint and Prettier
```

**Task 4.1.2: Project Structure** (2 hours)
```bash
Priority: P0
Dependencies: 4.1.1

Subtasks:
- [ ] Create folder structure:
  src/
  ├── api/          # API client
  ├── components/   # Reusable components
  ├── screens/      # Screen components
  ├── navigation/   # Navigation config
  ├── store/        # State management
  ├── types/        # TypeScript types
  ├── utils/        # Helper functions
  └── constants/    # Constants (colors, API URLs)

- [ ] Create index files
- [ ] Configure absolute imports (tsconfig.json)
```

**Task 4.1.3: API Client Setup** (3 hours)
```typescript
Priority: P0
Dependencies: 4.1.2

Subtasks:
- [ ] Create src/api/client.ts
- [ ] Configure Axios instance
- [ ] Add base URL from environment
- [ ] Add request interceptor (add auth token)
- [ ] Add response interceptor (handle errors)
- [ ] Create API service methods
- [ ] Test API connection

Code Structure:
// src/api/client.ts
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.EXPO_PUBLIC_API_URL,
  timeout: 30000,
});

// Request interceptor (add token)
apiClient.interceptors.request.use(...);

// Response interceptor (handle errors)
apiClient.interceptors.response.use(...);

export default apiClient;
```

**Task 4.1.4: Navigation Setup** (4 hours)
```typescript
Priority: P0
Dependencies: 4.1.3

Subtasks:
- [ ] Create src/navigation/index.tsx
- [ ] Configure NavigationContainer
- [ ] Create Auth Stack (Login, Register)
- [ ] Create Main Stack (Home, DreamInput, VideoView, History)
- [ ] Create Bottom Tabs (Home, History, Profile)
- [ ] Configure navigation types
- [ ] Test navigation flow
```

**Task 4.1.5: State Management** (3 hours)
```typescript
Priority: P0
Dependencies: 4.1.4

Subtasks:
- [ ] Create src/store/authStore.ts
- [ ] Create src/store/dreamStore.ts
- [ ] Implement auth state (user, token, login, logout)
- [ ] Implement dream state (dreams, loading, error)
- [ ] Persist auth token (SecureStore)
- [ ] Test state management
```

#### Deliverables:
- [ ] Working Expo project
- [ ] Navigation configured
- [ ] API client ready
- [ ] State management ready
- [ ] TypeScript types defined

---

### Epic 4.2: Authentication Screens

**Priority:** P0  
**Duration:** 3 days  
**Owner:** Frontend Team  
**Dependencies:** Epic 4.1

#### User Story:
> As a user, I want to register and login from my mobile device so that I can start using the app.

#### Acceptance Criteria:
- [ ] Welcome/Splash screen
- [ ] Login screen with email/password
- [ ] Register screen with validation
- [ ] Password visibility toggle
- [ ] Loading states
- [ ] Error messages displayed
- [ ] Successful login navigates to home

#### Technical Tasks:

**Task 4.2.1: Welcome Screen** (2 hours)
```typescript
Priority: P1
Dependencies: Epic 4.1

Subtasks:
- [ ] Create src/screens/WelcomeScreen.tsx
- [ ] Add app logo
- [ ] Add tagline: "Turn your dreams into videos"
- [ ] Add "Get Started" button → navigates to Register
- [ ] Add "Already have an account?" → navigates to Login
- [ ] Add simple animations (fade in)
```

**Task 4.2.2: Register Screen** (5 hours)
```typescript
Priority: P0
Dependencies: 4.2.1

Subtasks:
- [ ] Create src/screens/RegisterScreen.tsx
- [ ] Add email input (validate format)
- [ ] Add username input
- [ ] Add password input (with strength indicator)
- [ ] Add confirm password input
- [ ] Add "Show Password" toggle
- [ ] Add "Sign Up" button
- [ ] Add "Already have an account?" link
- [ ] Integrate with /api/v1/auth/register
- [ ] Handle validation errors
- [ ] Show loading spinner during request
- [ ] Save token on success
- [ ] Navigate to Home on success
```

**Task 4.2.3: Login Screen** (4 hours)
```typescript
Priority: P0
Dependencies: 4.2.2

Subtasks:
- [ ] Create src/screens/LoginScreen.tsx
- [ ] Add email input
- [ ] Add password input
- [ ] Add "Show Password" toggle
- [ ] Add "Login" button
- [ ] Add "Forgot Password?" link (placeholder)
- [ ] Add "Don't have an account?" link
- [ ] Integrate with /api/v1/auth/login
- [ ] Handle authentication errors
- [ ] Show loading spinner during request
- [ ] Save token on success
- [ ] Navigate to Home on success
```

**Task 4.2.4: Form Validation** (2 hours)
```typescript
Priority: P0
Dependencies: 4.2.3

Subtasks:
- [ ] Create src/utils/validation.ts
- [ ] Implement email validation
- [ ] Implement password strength check
- [ ] Implement username validation
- [ ] Add inline error messages
- [ ] Test all validation rules
```

#### Deliverables:
- [ ] Welcome screen
- [ ] Register screen
- [ ] Login screen
- [ ] Form validation
- [ ] Auth flow working end-to-end

---

### Epic 4.3: Dream Input & Analysis

**Priority:** P0  
**Duration:** 4 days  
**Owner:** Frontend Team  
**Dependencies:** Epic 4.2

#### User Story:
> As a user, I want to enter my dream text and get a video generated so that I can see my dream visualized.

#### Acceptance Criteria:
- [ ] Dream input screen with large text area
- [ ] Character count (max 2000)
- [ ] "Generate Video" button
- [ ] Loading state during analysis
- [ ] Display generated prompt
- [ ] Video generation status
- [ ] Navigate to video view when ready

#### Technical Tasks:

**Task 4.3.1: Home Screen** (3 hours)
```typescript
Priority: P0
Dependencies: Epic 4.2

Subtasks:
- [ ] Create src/screens/HomeScreen.tsx
- [ ] Add welcome message with user's name
- [ ] Add "Create New Dream Video" button
- [ ] Show recent dreams (last 3)
- [ ] Add stats card (total dreams, total videos)
- [ ] Navigate to DreamInputScreen on button click
```

**Task 4.3.2: Dream Input Screen** (5 hours)
```typescript
Priority: P0
Dependencies: 4.3.1

Subtasks:
- [ ] Create src/screens/DreamInputScreen.tsx
- [ ] Add large multiline text input
- [ ] Add character counter (0/2000)
- [ ] Add placeholder text: "Describe your dream..."
- [ ] Add helpful tips card (be descriptive, emotions, etc.)
- [ ] Add "Generate Video" button (disabled if empty)
- [ ] Validate text length
- [ ] Integrate with /api/v1/dreams/generate-video
- [ ] Show loading spinner during request
- [ ] Navigate to VideoStatusScreen on success
```

**Task 4.3.3: Video Status Screen** (5 hours)
```typescript
Priority: P0
Dependencies: 4.3.2

Subtasks:
- [ ] Create src/screens/VideoStatusScreen.tsx
- [ ] Display dream analysis result:
  - Generated prompt
  - Category detected
  - Template used
  - Confidence score

- [ ] Display video generation status:
  - "Pending" → clock icon
  - "Processing" → spinner + progress
  - "Completed" → checkmark
  - "Failed" → error icon

- [ ] Poll video status every 5 seconds (GET /api/v1/videos/{job_id})
- [ ] Show estimated completion time
- [ ] Add "View Video" button when completed
- [ ] Navigate to VideoPlayerScreen on button click
- [ ] Add error handling for failed generation
```

**Task 4.3.4: API Integration** (3 hours)
```typescript
Priority: P0
Dependencies: 4.3.3

Subtasks:
- [ ] Create src/api/dreamApi.ts
- [ ] Implement generateDreamVideo(dreamText)
- [ ] Implement getVideoStatus(jobId)
- [ ] Handle API errors
- [ ] Add retry logic for network failures
- [ ] Test API methods
```

#### Deliverables:
- [ ] Home screen
- [ ] Dream input screen
- [ ] Video status screen with polling
- [ ] API integration
- [ ] Loading and error states

---

### Epic 4.4: Video Player & History

**Priority:** P0  
**Duration:** 3 days  
**Owner:** Frontend Team  
**Dependencies:** Epic 4.3

#### User Story:
> As a user, I want to watch my generated videos and view my history so that I can revisit past dreams.

#### Acceptance Criteria:
- [ ] Video player screen with playback controls
- [ ] Share video option
- [ ] History screen with list of dreams
- [ ] Filter by category
- [ ] Thumbnail previews
- [ ] Tap to view video

#### Technical Tasks:

**Task 4.4.1: Video Player Screen** (4 hours)
```typescript
Priority: P0
Dependencies: Epic 4.3

Subtasks:
- [ ] Create src/screens/VideoPlayerScreen.tsx
- [ ] Use expo-av for video playback
- [ ] Add video player with controls
- [ ] Add play/pause button
- [ ] Add progress bar
- [ ] Add fullscreen option
- [ ] Add replay button
- [ ] Add share button (expo-sharing)
- [ ] Display dream text below video
- [ ] Add "Create Another" button
```

**Task 4.4.2: History Screen** (5 hours)
```typescript
Priority: P0
Dependencies: 4.4.1

Subtasks:
- [ ] Create src/screens/HistoryScreen.tsx
- [ ] Integrate with GET /api/v1/dreams
- [ ] Display dream list (FlatList)
- [ ] Show thumbnail, date, category for each dream
- [ ] Add pagination (load more on scroll)
- [ ] Add filter dropdown (category)
- [ ] Add pull-to-refresh
- [ ] Tap dream → navigate to VideoPlayerScreen
- [ ] Show empty state if no dreams
- [ ] Add loading skeleton
```

**Task 4.4.3: Dream Card Component** (2 hours)
```typescript
Priority: P1
Dependencies: 4.4.2

Subtasks:
- [ ] Create src/components/DreamCard.tsx
- [ ] Display video thumbnail
- [ ] Display dream text preview (first 100 chars)
- [ ] Display category badge
- [ ] Display date (relative: "2 hours ago")
- [ ] Add video status indicator
- [ ] Add tap handler
- [ ] Style component
```

**Task 4.4.4: Profile Screen** (3 hours)
```typescript
Priority: P1
Dependencies: 4.4.3

Subtasks:
- [ ] Create src/screens/ProfileScreen.tsx
- [ ] Display user info (email, username)
- [ ] Display statistics:
  - Total dreams
  - Total videos
  - Favorite category
  - Member since date

- [ ] Add "Logout" button
- [ ] Clear token on logout
- [ ] Navigate to Login screen
```

#### Deliverables:
- [ ] Video player screen
- [ ] History screen with pagination
- [ ] Dream card component
- [ ] Profile screen
- [ ] Share functionality

---

### Epic 4.5: UI/UX Polish

**Priority:** P1  
**Duration:** 2 days  
**Owner:** Frontend Team  
**Dependencies:** Epic 4.4

#### User Story:
> As a user, I want a beautiful and intuitive interface so that using the app is enjoyable.

#### Acceptance Criteria:
- [ ] Consistent color scheme
- [ ] Dark mode support
- [ ] Smooth animations
- [ ] Loading skeletons
- [ ] Error states with retry
- [ ] Toast notifications
- [ ] Responsive layouts

#### Technical Tasks:

**Task 4.5.1: Design System** (3 hours)
```typescript
Priority: P1
Dependencies: Epic 4.4

Subtasks:
- [ ] Create src/constants/theme.ts
- [ ] Define color palette:
  - Primary: #6366F1 (indigo)
  - Secondary: #EC4899 (pink)
  - Background: #0F172A (dark blue)
  - Surface: #1E293B
  - Text: #F1F5F9
  - Error: #EF4444

- [ ] Define typography scales
- [ ] Define spacing scales
- [ ] Define border radius values
- [ ] Create theme provider
```

**Task 4.5.2: Common Components** (4 hours)
```typescript
Priority: P1
Dependencies: 4.5.1

Subtasks:
- [ ] Create src/components/Button.tsx (primary, secondary, ghost)
- [ ] Create src/components/Input.tsx (with label, error)
- [ ] Create src/components/Card.tsx
- [ ] Create src/components/Badge.tsx (category badges)
- [ ] Create src/components/LoadingSpinner.tsx
- [ ] Create src/components/EmptyState.tsx
- [ ] Create src/components/ErrorState.tsx (with retry)
- [ ] Style all components with theme
```

**Task 4.5.3: Animations** (3 hours)
```typescript
Priority: P2
Dependencies: 4.5.2

Subtasks:
- [ ] Add fade-in animations (react-native-reanimated)
- [ ] Add slide-in animations for screens
- [ ] Add scale animation for buttons
- [ ] Add skeleton loaders for loading states
- [ ] Add pull-to-refresh animation
- [ ] Test performance on devices
```

**Task 4.5.4: Dark Mode** (2 hours)
```typescript
Priority: P2
Dependencies: 4.5.3

Subtasks:
- [ ] Implement dark mode theme
- [ ] Add theme toggle in ProfileScreen
- [ ] Persist theme preference
- [ ] Update all screens for dark mode
- [ ] Test contrast ratios
```

#### Deliverables:
- [ ] Design system
- [ ] Common UI components
- [ ] Animations
- [ ] Dark mode support

---

## ⏳ PHASE 5: Integration & Testing

**Timeline:** Week 11 (1 week)  
**Priority:** P0 (Critical Path)  
**Dependencies:** Phase 4

---

### Epic 5.1: End-to-End Testing

**Priority:** P0  
**Duration:** 3 days  
**Owner:** QA Team  
**Dependencies:** Phase 4

#### User Story:
> As a product owner, I need to ensure the entire flow works correctly so that we can launch confidently.

#### Acceptance Criteria:
- [ ] Complete user journey tested (register → dream input → video generation → viewing)
- [ ] API error scenarios tested
- [ ] Network failure handling tested
- [ ] Performance benchmarks met
- [ ] All critical bugs fixed

#### Technical Tasks:

**Task 5.1.1: Manual Testing** (8 hours)
```bash
Priority: P0
Dependencies: Phase 4

Test Cases:
1. User Registration Flow
   - [ ] Register with valid data → success
   - [ ] Register with existing email → error
   - [ ] Register with weak password → error
   - [ ] Validate email format

2. User Login Flow
   - [ ] Login with valid credentials → success
   - [ ] Login with invalid credentials → error
   - [ ] Token persists after app restart
   - [ ] Logout clears token

3. Dream Video Generation Flow
   - [ ] Enter dream text → generate video
   - [ ] Video status updates correctly
   - [ ] Video player loads video
   - [ ] Video controls work (play, pause, fullscreen)
   - [ ] Share button works

4. History Flow
   - [ ] History shows all dreams
   - [ ] Filter by category works
   - [ ] Pagination loads more dreams
   - [ ] Pull-to-refresh updates list
   - [ ] Tap dream opens video player

5. Error Scenarios
   - [ ] Network failure during registration
   - [ ] API timeout during video generation
   - [ ] Invalid token → logout
   - [ ] Video generation fails → show error
   - [ ] Retry button works after error

6. Performance
   - [ ] App launches in <3 seconds
   - [ ] Dream analysis completes in <5 seconds
   - [ ] Video loads in <5 seconds
   - [ ] History list scrolls smoothly
   - [ ] No memory leaks
```

**Task 5.1.2: Backend API Testing** (4 hours)
```bash
Priority: P0
Dependencies: 5.1.1

Subtasks:
- [ ] Test all endpoints with Postman/Insomnia
- [ ] Create API test collection
- [ ] Test authentication flow
- [ ] Test rate limiting (should return 429)
- [ ] Test error responses (400, 401, 404, 500)
- [ ] Measure API response times
- [ ] Document any issues
```

**Task 5.1.3: Load Testing** (3 hours)
```bash
Priority: P1
Dependencies: 5.1.2

Subtasks:
- [ ] Install locust or artillery
- [ ] Create load test scenarios:
  - 10 concurrent users registering
  - 50 concurrent users generating videos
  - 100 concurrent users fetching history

- [ ] Run load tests
- [ ] Identify bottlenecks
- [ ] Optimize slow endpoints
- [ ] Document performance metrics
```

#### Deliverables:
- [ ] Complete test coverage
- [ ] Bug report with priorities
- [ ] Performance benchmark report
- [ ] API test collection

---

### Epic 5.2: Bug Fixes & Optimization

**Priority:** P0  
**Duration:** 2 days  
**Owner:** Dev Team  
**Dependencies:** Epic 5.1

#### User Story:
> As a developer, I need to fix all critical bugs so that the app is stable for launch.

#### Acceptance Criteria:
- [ ] All P0 bugs fixed
- [ ] All P1 bugs fixed or documented
- [ ] Performance optimizations applied
- [ ] Code reviewed
- [ ] Re-tested

#### Technical Tasks:

**Task 5.2.1: Critical Bug Fixes** (8 hours)
```bash
Priority: P0
Dependencies: Epic 5.1

Subtasks:
- [ ] Fix any P0 bugs found in testing
- [ ] Add regression tests for fixed bugs
- [ ] Update error handling
- [ ] Re-test affected flows
```

**Task 5.2.2: Performance Optimization** (4 hours)
```bash
Priority: P1
Dependencies: 5.2.1

Subtasks:
- [ ] Optimize database queries (add indexes)
- [ ] Implement response caching (Redis, optional)
- [ ] Optimize image/thumbnail loading
- [ ] Reduce bundle size (code splitting)
- [ ] Minimize API calls (batch requests)
- [ ] Test performance improvements
```

**Task 5.2.3: Code Review & Refactoring** (4 hours)
```bash
Priority: P1
Dependencies: 5.2.2

Subtasks:
- [ ] Review backend code
- [ ] Review frontend code
- [ ] Remove unused code
- [ ] Add missing comments
- [ ] Ensure consistent code style
- [ ] Update documentation
```

#### Deliverables:
- [ ] All critical bugs fixed
- [ ] Performance optimizations applied
- [ ] Clean, reviewed codebase
- [ ] Updated documentation

---

## ⏳ PHASE 6: Deployment & Launch

**Timeline:** Week 12 (1 week)  
**Priority:** P0 (Critical Path)  
**Dependencies:** Phase 5

---

### Epic 6.1: Backend Deployment

**Priority:** P0  
**Duration:** 2 days  
**Owner:** DevOps Team  
**Dependencies:** Phase 5

#### User Story:
> As a developer, I need to deploy the backend to production so that users can access the API.

#### Acceptance Criteria:
- [ ] Backend deployed to Railway
- [ ] PostgreSQL database provisioned
- [ ] Environment variables configured
- [ ] HTTPS enabled
- [ ] API accessible via public URL
- [ ] Health check endpoint responding

#### Technical Tasks:

**Task 6.1.1: Railway Setup** (3 hours)
```bash
Priority: P0
Dependencies: Phase 5

Subtasks:
- [ ] Create Railway account
- [ ] Create new project: dreamvision-backend
- [ ] Connect GitHub repository
- [ ] Configure Python buildpack
- [ ] Set up PostgreSQL service
- [ ] Test database connection
```

**Task 6.1.2: Environment Configuration** (2 hours)
```bash
Priority: P0
Dependencies: 6.1.1

Subtasks:
- [ ] Add environment variables in Railway:
  - DATABASE_URL
  - ANTHROPIC_API_KEY
  - RUNWAY_API_KEY
  - SECRET_KEY
  - ALLOWED_ORIGINS (frontend URL)
  - ENVIRONMENT=production

- [ ] Test environment variables
- [ ] Verify CORS configuration
```

**Task 6.1.3: Database Migration** (2 hours)
```bash
Priority: P0
Dependencies: 6.1.2

Subtasks:
- [ ] Run Alembic migrations on production database
- [ ] Verify tables created
- [ ] Test database connection from app
- [ ] Create initial admin user (optional)
```

**Task 6.1.4: Deploy & Verify** (2 hours)
```bash
Priority: P0
Dependencies: 6.1.3

Subtasks:
- [ ] Push code to GitHub main branch
- [ ] Railway auto-deploys
- [ ] Wait for deployment to complete
- [ ] Check deployment logs
- [ ] Test health endpoint: curl https://api.dreamvision.app/health
- [ ] Test API documentation: https://api.dreamvision.app/docs
- [ ] Test dream analysis endpoint
- [ ] Monitor for errors
```

#### Deliverables:
- [ ] Backend live on Railway
- [ ] Public API URL
- [ ] Database provisioned
- [ ] Environment configured

---

### Epic 6.2: Mobile App Deployment

**Priority:** P0  
**Duration:** 2 days  
**Owner:** Mobile Team  
**Dependencies:** Epic 6.1

#### User Story:
> As a user, I want to install the app on my phone so that I can start using it.

#### Acceptance Criteria:
- [ ] Expo build configuration complete
- [ ] App builds successfully for iOS and Android
- [ ] TestFlight build uploaded (iOS)
- [ ] Internal testing APK available (Android)
- [ ] App connects to production API

#### Technical Tasks:

**Task 6.2.1: Expo Configuration** (2 hours)
```bash
Priority: P0
Dependencies: Epic 6.1

Subtasks:
- [ ] Update app.json/app.config.js:
  - name: "DreamVision"
  - slug: "dreamvision-ai"
  - version: "1.0.0"
  - icon, splash screen
  - iOS bundle ID
  - Android package name

- [ ] Add production API URL to environment
- [ ] Configure app permissions (camera, storage)
- [ ] Test configuration locally
```

**Task 6.2.2: iOS Build (TestFlight)** (3 hours)
```bash
Priority: P0
Dependencies: 6.2.1

Subtasks:
- [ ] Install EAS CLI: npm install -g eas-cli
- [ ] Login to Expo: eas login
- [ ] Configure iOS build: eas build:configure
- [ ] Create Apple Developer account (if needed)
- [ ] Generate credentials: eas credentials
- [ ] Build iOS app: eas build --platform ios
- [ ] Wait for build (~20 minutes)
- [ ] Download IPA file
- [ ] Upload to TestFlight
- [ ] Add internal testers
```

**Task 6.2.3: Android Build (APK)** (2 hours)
```bash
Priority: P0
Dependencies: 6.2.2

Subtasks:
- [ ] Configure Android build: eas build:configure
- [ ] Build Android APK: eas build --platform android --profile preview
- [ ] Wait for build (~15 minutes)
- [ ] Download APK
- [ ] Install on test device
- [ ] Test app functionality
- [ ] Share APK with internal testers
```

**Task 6.2.4: Production Testing** (3 hours)
```bash
Priority: P0
Dependencies: 6.2.3

Subtasks:
- [ ] Install app on iOS device
- [ ] Install app on Android device
- [ ] Test complete user flow on both platforms
- [ ] Verify API calls go to production
- [ ] Test video generation end-to-end
- [ ] Check for crashes or errors
- [ ] Document any issues
```

#### Deliverables:
- [ ] iOS build on TestFlight
- [ ] Android APK for testing
- [ ] App connects to production API
- [ ] Production testing complete

---

### Epic 6.3: Monitoring & Launch

**Priority:** P0  
**Duration:** 1 day  
**Owner:** DevOps Team  
**Dependencies:** Epic 6.2

#### User Story:
> As a product owner, I need monitoring in place so that I can track app health after launch.

#### Acceptance Criteria:
- [ ] Error tracking configured (Sentry)
- [ ] Analytics configured (optional)
- [ ] Uptime monitoring configured
- [ ] Launch checklist complete
- [ ] Public announcement ready

#### Technical Tasks:

**Task 6.3.1: Error Tracking** (2 hours)
```bash
Priority: P0
Dependencies: Epic 6.2

Subtasks:
- [ ] Create Sentry account (free tier)
- [ ] Add Sentry to backend:
  - pip install sentry-sdk
  - Configure in main.py
  - Test error reporting

- [ ] Add Sentry to mobile app:
  - expo install sentry-expo
  - Configure in app.json
  - Test error reporting

- [ ] Create alert rules
```

**Task 6.3.2: Uptime Monitoring** (1 hour)
```bash
Priority: P1
Dependencies: 6.3.1

Subtasks:
- [ ] Create UptimeRobot account (free tier)
- [ ] Add HTTP monitor for /health endpoint
- [ ] Set check interval: 5 minutes
- [ ] Add alert email
- [ ] Test alert
```

**Task 6.3.3: Launch Checklist** (2 hours)
```bash
Priority: P0
Dependencies: 6.3.2

Pre-Launch Checklist:
- [ ] Backend API accessible and healthy
- [ ] Database migrations applied
- [ ] All environment variables set
- [ ] CORS configured correctly
- [ ] Rate limiting active
- [ ] Mobile app builds working
- [ ] Production testing complete
- [ ] Error tracking active
- [ ] Uptime monitoring active
- [ ] Backup strategy documented
- [ ] Support email configured
- [ ] Privacy policy ready (if collecting data)
- [ ] Terms of service ready

Launch Steps:
- [ ] Announce to internal team
- [ ] Share TestFlight link (iOS)
- [ ] Share APK link (Android)
- [ ] Monitor Sentry for errors
- [ ] Monitor UptimeRobot for downtime
- [ ] Gather initial user feedback
```

#### Deliverables:
- [ ] Error tracking active
- [ ] Uptime monitoring active
- [ ] Launch checklist complete
- [ ] App launched! 🚀

---

## 📊 PROJECT SUMMARY

### Timeline Overview

| Phase | Duration | Start Week | End Week |
|-------|----------|------------|----------|
| Phase 1: Prompt System ✅ | 2 weeks | Week 1 | Week 2 |
| Phase 2: Backend | 3 weeks | Week 3 | Week 5 |
| Phase 3: Database & Auth | 2 weeks | Week 6 | Week 7 |
| Phase 4: Frontend Mobile | 3 weeks | Week 8 | Week 10 |
| Phase 5: Testing | 1 week | Week 11 | Week 11 |
| Phase 6: Deployment | 1 week | Week 12 | Week 12 |
| **Total** | **12 weeks** | | |

### Resource Requirements

**Team:**
- 1 Backend Developer (Phases 2-3)
- 1 Frontend Developer (Phase 4)
- 1 QA Tester (Phase 5)
- 1 DevOps Engineer (Phase 6)

**Budget:**
- Anthropic API: ~$0.011 per dream analysis
- Runway API: ~$0.05 per 5-second video
- Railway hosting: $5-20/month
- Expo EAS: Free for limited builds
- Domain: $10-15/year
- Total initial: ~$100-200 for MVP

### Critical Path

```
Phase 1 ✅
    ↓
Phase 2 (Backend) → CURRENT FOCUS
    ↓
Phase 3 (Database & Auth)
    ↓
Phase 4 (Mobile Frontend)
    ↓
Phase 5 (Testing)
    ↓
Phase 6 (Deployment)
    ↓
LAUNCH 🚀
```

### Risk Mitigation

**Risk 1: API Rate Limits**
- Mitigation: Implement rate limiting and queue system
- Backup: User-facing rate limits (10 dreams/day)

**Risk 2: Video Generation Delays**
- Mitigation: Show progress and estimated time
- Backup: Email notification when ready

**Risk 3: High API Costs**
- Mitigation: Optimize prompts, monitor usage
- Backup: Implement usage limits per user tier

**Risk 4: Mobile Build Issues**
- Mitigation: Test early and often
- Backup: Web PWA as alternative (Phase 7)

---

## 🎯 NEXT STEPS

### Week 3 - Getting Started

**Day 1-2:**
1. ✅ Review this roadmap
2. ✅ Set up development environment
3. ✅ Start Epic 2.1 (FastAPI Project Setup)

**Day 3-5:**
4. Complete Epic 2.2 (Dream Analysis API)
5. Test with n8n workflow integration

**Day 6-7:**
6. Start Epic 2.3 (Video Generation API)
7. Weekly progress review

### Tools & Accounts Needed

- [ ] GitHub account
- [ ] Railway account (for backend deploy)
- [ ] Expo account (for mobile build)
- [ ] Anthropic API key (already have)
- [ ] Runway API key (already have)
- [ ] Sentry account (for error tracking)
- [ ] UptimeRobot account (for monitoring)

### Development Workflow

1. **Daily Standups** (if team > 1)
   - What did I complete yesterday?
   - What will I work on today?
   - Any blockers?

2. **Weekly Reviews**
   - Review completed epics
   - Demo progress
   - Adjust timeline if needed

3. **Git Workflow**
   - Branch per epic: `feature/epic-2.1-fastapi-setup`
   - Pull request with review
   - Merge to `main` when tested

4. **Documentation**
   - Update README as you go
   - Document API changes
   - Keep roadmap updated

---

## 📝 NOTES

- This roadmap is **modular** - each epic can be developed independently
- Priorities (P0/P1/P2) help focus on critical path
- Time estimates are realistic but may vary
- Test early and often to catch issues
- Celebrate milestones! 🎉

**Remember:** You've already completed the hardest part (prompt engineering)! Now it's systematic execution.

Good luck! 🚀

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-11  
**Status:** Ready for Development
