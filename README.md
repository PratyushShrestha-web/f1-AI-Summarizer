#  V6 Turbo AI

An AI-powered Formula 1 race intelligence dashboard that transforms live race data into a professional, interactive race analysis experience.

The application retrieves Formula 1 session data, race results, driver and constructor standings, race control events, and circuit information. It then uses AI to analyze important race events and generate a structured race intelligence report.

##  Live Demo

[View the Live Demo](https://f1-ai-summarizer.onrender.com/)

## Screenshots
  ## dashboard
  ---------------------------------------------------------------------------------------------------------------------------
<img width="1891" height="906" alt="image" src="https://github.com/user-attachments/assets/3ce3c086-6a5b-4fff-b9dd-f5ae4fc94d4b" />


##  Features

###  Race Dashboard

* Latest completed Formula 1 race
* Race date and circuit information
* Driver results and finishing positions
* Podium visualization
* Championship standings
* Constructor standings
* Important race events

###  AI Race Analysis

The application analyzes race control events and generates a structured AI-powered report containing:

* Race Overview
* Key Incidents
* Race Analysis
* Final Verdict

The AI is instructed to only use the supplied race data and avoid inventing race events or unsupported information.

###  Circuit Visualization

* Interactive world map of Formula 1 circuits
* Circuit locations displayed using Leaflet
* Circuit information and country details
* Interactive map markers

###  Driver Profiles

View individual driver information and their current championship standing.

###  Formula 1 Data

The application provides:

* Race results
* Driver standings
* Constructor standings
* Race control events
* Circuit information

##  Tech Stack

### Backend

* Python
* Flask
* REST APIs
* Google Gemini API

### Frontend

* HTML
* CSS
* Tailwind CSS
* JavaScript
* Leaflet.js
* Lucide Icons
* GSAP

### Data & AI

* OpenF1 API
* Google Gemini 2.5 Flash
* JSON caching

### Deployment

* Render
* Gunicorn

##  Project Structure

```text
f1-AI-Summarizer/
│
├── app.py
├── api.py
├── ai.py
├── analyzer.py
├── coordinates.py
├── main.py
├── report.py
├── utils.py
├── requirements.txt
│
├── data/
│   └── summary_cache.json
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   └── car.png
│   └── js/
│       └── animations.js
│
└── templates/
    ├── index.html
    ├── analysis.html
    ├── circuitnav.html
    ├── driver.html
    ├── race.html
    ├── standingsnav.html
    │
    └── components/
        ├── ai_summary.html
        ├── championship.html
        ├── circuits.html
        ├── constructors.html
        ├── drivers.html
        ├── events.html
        ├── hero.html
        ├── latest_race.html
        ├── navbar.html
        └── results.html
```

##  How It Works

```text
OpenF1 API
     ↓
Fetch Latest Race Data
     ↓
Fetch Drivers, Results, Standings
     ↓
Fetch Race Control Events
     ↓
Analyze Important Events
     ↓
Build AI Prompt
     ↓
Google Gemini
     ↓
Professional Race Intelligence Report
```

##  Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/PratyushShrestha-web/f1-AI-Summarizer.git
cd f1-AI-Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

##  Environment Variables

| Variable         | Description                               |
| ---------------- | ----------------------------------------- |
| `GEMINI_API_KEY` | API key used to generate AI race analysis |

Never commit your `.env` file or API keys to GitHub.

##  Data Sources

This project uses:

* OpenF1 API for Formula 1 session, driver, results, standings, and race control data.
* Google Gemini API for AI-powered race analysis.

##  Project Goals

This project was built to explore the integration of:

* REST APIs
* Data processing
* AI-powered analysis
* Flask web applications
* Interactive data visualization
* API caching
* Production deployment

##  Future Improvements

Possible future improvements include:

* Historical race comparison
* Driver performance trends
* Lap-by-lap visualization
* Pit stop analysis
* Advanced telemetry analysis
* User accounts and saved reports
* More detailed AI race insights

##  Author

**Pratyush Shrestha**

GitHub: [PratyushShrestha-web](https://github.com/PratyushShrestha-web)

---

Built with Python, Flask, Formula 1 data, and AI.
