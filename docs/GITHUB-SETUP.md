# 🚀 GitHub Repository Setup Guide

Bu guide, DreamVision AI projesini GitHub'a yüklemek için adım adım talimatlar içerir.

---

## 📋 Ön Hazırlık

### 1. GitHub Hesabı
- [ ] GitHub hesabın var mı? → [github.com](https://github.com)
- [ ] Git yüklü mü? → `git --version` ile kontrol et

---

## 🎯 Adım Adım Kurulum

### Step 1: Lokal Proje Klasörü Oluştur
```bashmkdir dreamvision-ai
cd dreamvision-ai

### Step 2: Git Initialize
```bashgit init
git branch -M main

### Step 3: GitHub'da Repository Oluştur

1. GitHub'da **New Repository**
2. Name: `dreamvision-ai`
3. **IMPORTANT:** Hiçbir şeyi işaretleme (README, .gitignore, license)
4. Create repository

### Step 4: Remote Ekle
```bashgit remote add origin https://github.com/[YOUR_USERNAME]/dreamvision-ai.git

### Step 5: İlk Commit + Push
```bashgit add .
git commit -m "Initial commit: project structure and documentation"
git push -u origin main

---

## 🌿 Branch Strategy

### Main Branch
```bashmain = production ready code

### Feature Branch Oluştur
```bashYeni feature başlat
git checkout -b feature/epic-2.1-fastapi-setupÇalış, commit et
git add .
git commit -m "feat: initialize FastAPI project structure"Push et
git push -u origin feature/epic-2.1-fastapi-setup

### Merge to Main
```bashMain'e geç
git checkout mainFeature'ı merge et
git merge feature/epic-2.1-fastapi-setupPush et
git push

---

## 📝 Commit Message Convention

### Format:<type>: <description>

### Types:feat:     Yeni feature
fix:      Bug fix
docs:     Dokümantasyon
test:     Test ekleme
refactor: Code refactoring
style:    Formatting
chore:    Maintenance

### Örnekler:
```bashgit commit -m "feat: add JWT authentication"
git commit -m "fix: resolve token expiration bug"
git commit -m "docs: update API documentation"
git commit -m "test: add dream analysis tests"

---

## 🔧 Yararlı Git Komutları

### Daily Workflow
```bashStatus
git statusAdd changes
git add .Commit
git commit -m "feat: add feature"Push
git pushPull (güncel kal)
git pull

### Branch Management
```bashBranch listele
git branch -aYeni branch
git checkout -b feature/new-featureBranch değiştir
git checkout mainBranch sil
git branch -d feature/old-feature

### Undo Operations
```bashSon commit'i geri al (değişiklikler kalır)
git reset --soft HEAD~1Dosyayı unstage et
git restore --staged file.pyDosyadaki değişiklikleri geri al
git restore file.py

---

## ⚠️ Önemli Notlar

### Güvenlik
- ❌ ASLA `.env` dosyasını commit etme
- ❌ ASLA API key'leri commit etme
- ✅ `.gitignore` dosyasını kontrol et

### Temizlik
```bashEğer yanlışlıkla .env eklediysen:
git rm --cached .env
git commit -m "fix: remove .env from git"
git push

---

## 🆘 Sorun Giderme

### Problem: Push reddedildi
```bashÇözüm: Önce pull yap
git pull origin main
Çakışmaları çöz
git push

### Problem: Yanlış branch'teyim
```bashÇözüm: Stash yap, branch değiştir
git stash
git checkout correct-branch
git stash pop

### Problem: Commit mesajını değiştirmek istiyorum
```bashSon commit'in mesajını değiştir (henüz push yapmadıysan)
git commit --amend -m "Yeni mesaj"

---

## ✅ Checklist

Kurulum tamamlandı mı?

- [ ] GitHub repository oluşturuldu
- [ ] Lokal repo bağlandı
- [ ] İlk push başarılı
- [ ] .gitignore çalışıyor
- [ ] Branch stratejisi anlaşıldı

---

**Last Updated:** 2025-11-17