🌾 AgroLink – Farmer & Buyer Connection Platform

AgroLink is a full-stack web application designed to connect farmers and buyers directly, enabling transparent product listing, easy access, and fair trade using modern web technologies.

This project focuses on backend–frontend integration, authentication, and real-world role-based dashboards, making it suitable for academic projects, internships, and entry-level placements.

✨ Features

👨‍🌾 Farmer Dashboard – Manage and list agricultural products

🧑‍💼 Buyer Dashboard – Browse and view available products

🔐 Secure Login & Authentication using JWT

📦 Product Listing & Management

🔄 API-based Frontend–Backend Communication


🚀 Tech Stack
🔹 Backend

⚡ FastAPI (Python)

🗄️ SQLite Database

🔐 JWT Authentication

🔹 Frontend

⚛️ React (Vite)

🎨 CSS

🌐 REST API Integration


▶️ How to Run the Project
🖥️ Backend Setup
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

uvicorn app.main:app --reload
Backend will run at:
👉 http://127.0.0.1:8000


🌐 Frontend Setup
cd frontend/agrolink-frontend
npm install
npm run dev


🔮 Future Enhancements

🤖 AI-based crop price prediction

📊 Demand forecasting using Machine Learning

🌱 Smart farmer recommendation system

💳 Payment gateway integration

📱 Mobile application support

Frontend will run at:
👉 http://localhost:5173


👩‍💻 Developer

Rakshitha R
💻 Full-Stack Developer (FastAPI + React)
🎯 Interested in Backend, AI & Data-Driven Systems

⭐ If you find this project useful, consider giving it a star!


## 📂 Project Structure

```text
AGROLINK/
├── app/                  # FastAPI backend
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   └── agrolink-frontend/ # React frontend
│
├── requirements.txt
├── .gitignore
└── README.md
```


