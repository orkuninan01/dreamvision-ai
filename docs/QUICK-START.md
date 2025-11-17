🚀 Quick Start - DreamVision AI

## 📦 Başlamadan Önce

### Gereksinimler:
- ✅ GitHub hesabı
- ✅ Supabase hesabı
- ✅ Anthropic API key
- ✅ Runway API key
- ✅ Python 3.11+
- ✅ Node.js 18+
- ✅ VS Code

---

## ⚡ 5 Dakikada Başla

### 1️⃣ Backend Setup (Day 1)
```bashSupabase

supabase.com → Sign up
Create project: "dreamvision-production"
Copy API keys
Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt.env oluştur
cp .env.example .env
API key'leri ekleÇalıştır
uvicorn app.main:app --reload

### 2️⃣ Mobile Setup (Week 3)
```bashcd mobile
npm install
npx expo start

---

## 📚 Dokümantasyon

| Dosya | İçerik | Ne Zaman |
|-------|--------|----------|
| **ROADMAP-v2.md** | Week 1-2 (Backend) | Her gün |
| **ROADMAP-v2-PART2.md** | Week 3-6 (Mobile+Deploy) | Week 3'ten sonra |
| **ROADMAP-NAVIGATION.md** | Navigasyon rehberi | Kaybolduğunda |
| **GITHUB-SETUP.md** | Git workflow | Git sorunlarında |

---

## 🎯 Günlük Workflow
```bash1. Branch oluştur
git checkout -b feature/epic-2.12. Çalış...3. Commit
git add .
git commit -m "feat: add feature"4. Push
git push -u origin feature/epic-2.15. Notion'da checkbox işaretle ✓

---

## 📊 Haftalık Plan

| Week | Goal | Dosya |
|------|------|-------|
| 1-2 | Backend | ROADMAP-v2.md |
| 3-4 | Mobile | ROADMAP-v2-PART2.md |
| 5 | Integration | ROADMAP-v2-PART2.md |
| 6 | Deploy | ROADMAP-v2-PART2.md |

---

## 🔑 API Keys

### Backend (.env):
```bashSUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_KEY=eyJ...
ANTHROPIC_API_KEY=sk-ant-...
RUNWAY_API_KEY=...

### Mobile (.env):
```bashEXPO_PUBLIC_API_URL=http://localhost:8000/api/v1
EXPO_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=eyJ...

---

## ⚠️ Hatırlatmalar

- ❌ `.env` dosyasını commit etme
- ✅ Her gün progress güncelle
- ✅ Küçük commit'ler yap
- ✅ ROADMAP'i açık tut

---

## 🆘 Yardım

**Backend:** → ROADMAP-v2.md  
**Mobile:** → ROADMAP-v2-PART2.md  
**Git:** → GITHUB-SETUP.md  
**Kayboldum:** → ROADMAP-NAVIGATION.md

---

## 🎉 İlk Task

**Yarın sabah:**ROADMAP-v2.md → Phase 2 → Epic 2.1 → Task 2.1.1
"Supabase Project Setup" (1 hour)

---

**Motto:** "One task at a time!" 🚀

**Last Updated:** 2025-11-17