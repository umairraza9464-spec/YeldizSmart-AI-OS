# YeldizSmart AI OS

YeldizSmart AI is a standalone Chromium-based autonomous browser + business OS for AI-powered lead generation and multi-account automation.

## Features (Phase 1 skeleton)

- **Multi-account Playwright engine** with proxy rotation and profile isolation
- **PyQt5 UI** with embedded browser view and side panel integration
- **SQLite data layer** with 14-column lead schema (UNIQUE mobile constraint)
- **Google Sheets webhook sync** for real-time data updates
- **AI classification** (HOT/WARM/COLD leads with owner verification)
- **Automated work scheduler** (4 AM–12 PM IST work window)
- **Zero duplicacy** - no repeat messages even after restart
- **Windows EXE packaging** with one-click installer

## Tech Stack

- **Browser Automation**: Playwright (Python) with headless/headed Chromium
- **UI Framework**: PyQt5 with QWebEngineView
- **AI Models**: Google Gemini API + Llama (Groq/local)
- **Database**: SQLite3 with webhook sync
- **Packaging**: PyInstaller

## Quick Start

### Clone & Setup

```bash
git clone https://github.com/umairraza9464-spec/YeldizSmart-AI-OS.git
cd YeldizSmart-AI-OS

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
playwright install chromium
```

### Run the App

```bash
python app.py
```

### Build EXE (Windows)

```bash
python packaging/build_exe.py
```

Or use the automated installer:

```bash
python packaging/INSTALL_AND_RUN.bat
```

## Project Structure

```
yeldizsmart_ai/
  app.py                    # Main entry point
  requirements.txt
  config/
    settings.example.yaml
  ui/
    main_window.py          # PyQt5 main window + tabs
    mission_control.py      # Campaign dashboard
  engine/
    browser_manager.py      # Playwright contexts
    account_session.py      # FB/OLX account controller
  ai_core/
    gemini_client.py        # Gemini API wrapper
    llama_client.py         # Llama backend
    classifier.py           # Owner vs dealer logic
    ocr.py                  # Number plate extraction
  data/
    db.py                   # SQLite models
    sheets_sync.py          # Webhook poster
    csv_backup.py           # CSV export
  scheduler/
    work_scheduler.py       # 4–12 AM scheduler
  packaging/
    build_exe.py            # PyInstaller config
    INSTALL_AND_RUN.bat     # One-click installer
```

## Configuration

Edit `config/settings.example.yaml`:

```yaml
timezone: "Asia/Kolkata"

work_window:
  start: "04:00"
  end: "12:00"

proxies:
  fb:
    - "http://user:pass@res-proxy-1:port"
  olx:
    - "http://user:pass@res-proxy-2:port"

cities:
  - "Mumbai"
  - "Delhi"
  - "Pune"

ai:
  provider: "gemini"  # or "llama"
  gemini_api_key: "YOUR_GEMINI_KEY"

google_webhook:
  leads_url: "https://script.google.com/macros/s/XXXX/exec"
```

## Data Schema (SQLite)

14-column leads table:

| Column      | Type   | Notes         |
|-------------|--------|---------------|
| id          | INT    | Primary key   |
| date        | TEXT   |               |
| name        | TEXT   |               |
| mobile      | TEXT   | UNIQUE        |
| reg_no      | TEXT   |               |
| car_model   | TEXT   |               |
| variant     | TEXT   |               |
| year        | TEXT   |               |
| km          | TEXT   |               |
| address     | TEXT   |               |
| follow_up   | TEXT   |               |
| source      | TEXT   | FB/OLX + city |
| context     | TEXT   | AI reasoning  |
| license     | TEXT   | User tag      |
| remark      | TEXT   | Notes         |

## Multi-Account Anti-Ban Architecture

- **12 Contexts Minimum**: 6 FB + 6 OLX accounts in isolated tabs
- **Proxy Rotation**: Each context gets dedicated residential/mobile proxy
- **Profile Isolation**: Separate cookies/session per account
- **Dynamic City Switching**: Runtime adjustment without restart

## Roadmap

- [ ] Phase 1: Skeleton (browser UI, DB, scheduler)
- [ ] Phase 2: AI engine (Gemini + classifier + OCR)
- [ ] Phase 3: Auto-messaging with rate limiting
- [ ] Phase 4: Mobile number extraction & webhook sync
- [ ] Phase 5: Full anti-ban multi-account system
- [ ] Phase 6: Dashboard + real-time notifications

## License

MIT License - see LICENSE file for details.

## Support

For issues, open a GitHub issue or contact the maintainer.

---

**Made in India 🇮🇳 | AI-powered automation for everyone**
