# 👁️ Vision AI

**A Second Pair of Eyes** — An AI-powered visual assistant designed to help blind and visually impaired people understand their surroundings using Google's Gemini Vision API.

---

## ✨ Features

- **Scene Description**: Captures camera input and delivers clear, spatial descriptions of objects, people, and obstacles (left, center, right).
- **Voice Interaction**: Ask questions naturally via microphone input or voice recordings.
- **Audio Answers**: Text-to-Speech (gTTS) playback answers directly to the user.
- **Dual Interfaces**:
  - Streamlit web UI for interactive testing and camera input.
  - FastAPI backend with static web client support.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Muhammad-Fahad-Javed/visionAi.git
cd visionAi
```

### 2. Set up a virtual environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the application

#### Streamlit UI:
```bash
streamlit run app.py
```

#### FastAPI Backend:
```bash
uvicorn main:app --reload
```

---

## ⚠️ Disclaimer
Vision AI is an assistive tool. Do not rely on it alone for critical navigation or personal safety.
