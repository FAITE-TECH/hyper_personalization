# Hyper-Personalization-AI marketing tool
A FastAPI + PostgreSQL backend that provides **hyper-personalized customer experiences** — similar to Netflix and Spotify recommendations.  
The system stores **users, items, and interactions**, then generates **personalized recommendations**.

## Features
- REST API built with **FastAPI**
- **Swagger UI** for interactive documentation (`/docs`)
- **PostgreSQL + SQLAlchemy** for database management
- **User, Item, Interaction** CRUD endpoints
- Basic **recommendation API**
- Environment variable configuration with `.env`
- Easy seeding of data via SQL file

## Setup Instructions
### 1️) Clone the project
```bash
git clone https://github.com/your-username/hyper-personalization.git
cd hyper-personalization
```

2) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Configure environment
Create a .env file in the root folder
```bash
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/hyperdb
APP_NAME=Hyper Personalization API

```

5) Setup PostgreSQL
- Install PostgreSQL and pgAdmin.
- Create a database called hyperdb.
- Run migrations (or use models.py to create tables)

6) Seed sample data
Run the sql file
```bash
psql -U postgres -d hyperdb -f data/seed_data.sql
```

7) Run the server
uvicorn app.main:app --reload

8) Open Swagger at http://127.0.0.1:8000/docs
