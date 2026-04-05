# 🗄️ Supabase Setup Guide

## 📋 Project Information

**Project Name:** dreamvision-production  
**Region:** Southeast Asia (Singapore)  
**Database:** PostgreSQL 15  
**Created:** 2026-04-02

---
 
## 🔑 API Keys

**Project URL:** https://eflvbxyvrqqlreigwaqk.supabase.co

**Keys:**
- **anon public key:** Used in mobile app (safe to expose)
- **service_role key:** Used in backend (SECRET, never expose!)

**Location:** Stored in `backend/.env`

---

## 🗃️ Database Schema

### Tables

#### 1. user_profiles
```sql
- id: UUID (references auth.users)
- username: TEXT (unique)
- subscription_tier: TEXT (default: 'free')
- dreams_count: INTEGER (default: 0)
- videos_count: INTEGER (default: 0)
- created_at: TIMESTAMPTZ
- updated_at: TIMESTAMPTZ
```

**Indexes:**
- Primary key on `id`
- Unique index on `username`

**RLS:** Enabled
- Users can view/update own profile

---

#### 2. dreams
```sql
- id: UUID (primary key)
- user_id: UUID (foreign key → user_profiles)
- dream_text: TEXT
- video_prompt: TEXT
- category: TEXT (gothic/chase/flight/transformation/physics/liminal)
- template_used: TEXT
- confidence: FLOAT
- token_usage: JSONB
- created_at: TIMESTAMPTZ
```

**Indexes:**
- Primary key on `id`
- Index on `user_id`
- Index on `created_at DESC`
- Index on `category`

**RLS:** Enabled
- Users can only view/insert/update/delete own dreams

---

#### 3. videos
```sql
- id: UUID (primary key)
- dream_id: UUID (foreign key → dreams)
- job_id: TEXT (unique, Runway job ID)
- status: TEXT (pending/processing/completed/failed)
- video_url: TEXT
- thumbnail_url: TEXT
- duration: INTEGER (default: 5)
- created_at: TIMESTAMPTZ
- completed_at: TIMESTAMPTZ
- error_message: TEXT
```

**Indexes:**
- Primary key on `id`
- Unique index on `job_id`
- Index on `dream_id`
- Index on `status`

**RLS:** Enabled
- Users can view videos for their own dreams

---

## 🔐 Row Level Security (RLS)

All tables have RLS enabled for security.

**Policies:**
- `user_profiles`: 3 policies (view/update/insert own)
- `dreams`: 4 policies (view/insert/update/delete own)
- `videos`: 1 policy (view for own dreams)

---

## 🔄 Triggers & Functions

### 1. handle_new_user()
**Purpose:** Auto-create user profile when new user signs up  
**Trigger:** After INSERT on auth.users

### 2. update_user_stats()
**Purpose:** Update dreams_count when dream is created  
**Trigger:** After INSERT on dreams

### 3. update_video_count()
**Purpose:** Update videos_count when video completes  
**Trigger:** After UPDATE on videos (when status → 'completed')

### 4. update_updated_at()
**Purpose:** Auto-update updated_at timestamp  
**Trigger:** Before UPDATE on user_profiles

---

## 📦 Storage

### Bucket: video-thumbnails

**Configuration:**
- Public bucket: ✅ Yes
- File size limit: 5 MB
- Allowed types: image/jpeg, image/png, image/webp

**Policies:**
- Users can upload to their own folder: `{user_id}/filename.jpg`
- Public read access (no auth required)

**Public URL Format:*
https://xxxxx.supabase.co/storage/v1/object/public/video-thumbnails/{user_id}/{filename}
---

## 🔧 Authentication

**Provider:** Email/Password

**Settings:**
- Email confirmation: DISABLED (development)
- JWT expiry: 3600 seconds (1 hour)
- Password policy: Min 8 chars, uppercase, lowercase, numbers

**Redirect URLs:**
- http://localhost:19006 (Expo)
- http://localhost:8081 (Expo alternative)
- http://localhost:3000 (web)
- exp://localhost:19000 (Expo deep link)

---

## 🧪 Test Users
Email: test@dreamvision.ai
Password: Test123456!
Username: testuser
**Created for development testing.**

---

## 🔄 How to Reset Database

**⚠️ WARNING: This will delete all data!**
```sql
-- Drop all tables (careful!)
DROP TABLE IF EXISTS public.videos CASCADE;
DROP TABLE IF EXISTS public.dreams CASCADE;
DROP TABLE IF EXISTS public.user_profiles CASCADE;

-- Then re-run the schema creation SQL
```

---

## 📝 Migration Notes

**Database schema created on:** 2026-04-02  
**Version:** 1.0  
**Last updated:** 2026-04-02

**Future migrations:**
- Use Supabase Migrations for schema changes
- Never manually edit production schema
- Always test in development first

---

## 🆘 Troubleshooting

### Issue: RLS blocking queries
**Solution:** Check policies, ensure auth.uid() matches user_id

### Issue: Trigger not firing
**Solution:** Check function exists, trigger enabled

### Issue: Storage upload fails
**Solution:** Check bucket policy, verify auth token

---

**Created:** 2026-04-02  
**Last Updated:** 2026-04-02