# 🚀 Nebula AI Suite

**Nebula** is a multi-platform AI assistant system supporting OpenAI, Claude, and Gemini. It spans CLI, Electron, Web, Mobile, Chrome Extension, and VS Code — complete with SaaS monetization, investor docs, and launch materials.

![NebulaChat UI](launch/screenshot.png)

---

## ✨ Features
- Chat across **CLI, Web, Electron, Mobile, VS Code**
- Supports **OpenAI, Claude, Gemini**
- Persistent **session manager** with SQLite
- Themeable **GUI settings** & Markdown export
- Stripe-integrated **dashboard**
- **Product Hunt ready**: launch assets included
- **Offline LLM** support hooks (Ollama, GPT4All, LM Studio)

---

## 📁 Folder Structure

```
core/               ← CLI + backend chat logic  
frontend/           ← Web, Chrome, and SaaS GUI  
electron-app/       ← Electron desktop app  
mobile/             ← Native & Chrome wrapper builds  
vscode-extension/   ← VSIX and docs  
dashboard/          ← Stripe + analytics UIs  
offline_mode/       ← Hooks for local LLMs  
docs/               ← MkDocs config  
installers/         ← DMG, EXE, APK bundles  
launch/             ← Tweet, PH copy, email, screenshot  
investor/           ← Pitch deck and financials  
monetization/       ← SaaS logic, pricing  
utils/              ← Shared scripts  
```

---

## 🛠️ Local Dev Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python core/main.py
```

---

## 📦 Installers + Extensions

- [nebula-chat.vsix](vscode-extension/)
- [Electron installers](installers/)
- [Mobile ZIPs](mobile/)

---

## 🐙 GitHub Actions (in .github/workflows/)
- Deploy Docs
- Build Electron + Mobile
- Auto-Release with Launch Attachments

---

## 🌍 License

MIT — yours to fork, ship, and scale.