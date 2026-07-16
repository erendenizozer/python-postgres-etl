# Python PostgreSQL ETL Project

## About

This project is a simple ETL project that I made using Python, PostgreSQL and Docker.

The program gets data from a public API and saves it into a PostgreSQL database.

## Technologies

- Python
- PostgreSQL
- Docker Compose
- Requests
- Psycopg2

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd python-postgres-etl
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it.

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file using `.env.example`.

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Run the project

```bash
python src/main.py
```

The program will download the data from the API and insert it into the `raw_data` table in PostgreSQL.
