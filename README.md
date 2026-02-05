🌾 AgroLink – Farmer & Buyer Connection Platform

AgroLink is a full-stack web application designed to connect farmers and buyers directly, enabling transparent product listing, easy access, and fair trade using modern web technologies.

🚀 Tech Stack

🔹 Backend
⚡ FastAPI (Python)
🗄️ SQLite Database
🔐 JWT Authentication


🔹 Frontend
⚛️ React (Vite)
🎨 CSS
🌐 REST API Integration

✨ Features

👨‍🌾 Farmer Dashboard
🧑‍💼 Buyer Dashboard
🔐 Secure Login & Authentication
📦 Product Listing & Management
🔄 API-based Frontend–Backend Communication

📂 Project Structure
AGROLINK/
│── app/                  # FastAPI backend
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── utils/
│   └── main.py
│
│── frontend/
│   └── agrolink-frontend/ # React frontend
│
│── requirements.txt
│── .gitignore
│── README.md

▶️ How to Run the Project
🖥️ Backend Setup
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs at:
👉 http://127.0.0.1:8000

🌐 Frontend Setup
cd frontend/agrolink-frontend
npm install
npm run dev


Frontend runs at:
👉 http://localhost:5173

🔮 Future Scope

🤖 AI-based crop price prediction
📊 Demand forecasting using Machine Learning
🌱 Smart farmer recommendation system
💳 Payment gateway integration
📱 Mobile app version

👩‍💻 Developer

Rakshitha R
💻 Full Stack Developer (FastAPI + React)
🌟 Aspiring AI & Data Professional

⭐ If you like this project, give it a star on GitHub!