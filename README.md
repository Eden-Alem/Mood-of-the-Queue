# Mood of the Queue

**A simple internal tool for logging and visualizing the mood of patient support ticket queues — built with Python, Streamlit, and Google Sheets.**

---

## 🎯 Project Overview

Our Operations team handles hundreds of patient support tickets daily. Each ticket carries an emotional “vibe” — from frustrating to joyful. Capturing this mood in real time helps the team understand trends and improve workflows.

This tool enables support agents to log the mood of the ticket queue quickly, optionally add a short note, and visualize the aggregated mood counts for the day.

---

## 🚀 Features

- **Log a Mood:** Select an emoji mood and add an optional note.
- **Store Data:** All entries append to a Google Sheet with timestamp.
- **Visualize Mood:** Interactive Plotly bar chart showing mood counts for the current day.
- **Simple UI:** Built with Streamlit for fast and intuitive use.

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit (UI)
- gspread + Google Sheets API (storage)
- Plotly (visualizations)

---

## 📦 Getting Started

### Prerequisites

- Python 3.10 or newer installed
- Google Cloud service account with Sheets API enabled
- Google Sheet created with the name "MoodQueue" and the following columns in the first row:

    Timestamp | Mood | Note

- Service account JSON key file downloaded

---

### Installation

1. Clone the repo:

 ```bash
 git clone https://github.com/Eden-Alem/Mood-of-the-Queue.git
 cd mood-of-the-queue
 ```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure Google Sheets credentials:

    If running locally, place your service account JSON as creds.json

5. Running the App Locally

```bash
streamlit run src/app.py
```

Open your browser to the URL printed in the console (usually http://localhost:8501).


## 📁 Project Structure

```
mood-of-the-queue/
├── src/
│   ├── app.py            # Main Streamlit app
│   ├── mood_logger.py    # Google Sheets integration and mood logging logic
│   ├── mood_plotter.py   # Mood data processing and Plotly chart generation
├── requirements.txt      # Python dependencies
├── .gitignore
├── README.md
└── creds.json (ignored)
```

## 🧪 Testing

This project includes tests for:

- `test_mood_logger.py`: ensures mood logging and Google Sheets interactions work correctly.

Tests are written using `pytest`. To run tests:

```bash
pytest tests/
```


### 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.
