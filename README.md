# Airports ETL (Docker + PostgreSQL)

An end-to-end ETL (Extract, Transform, Load) project that loads global airport data from a public CSV dataset into a PostgreSQL database, using Python and Docker Compose.

---

## Features

- **Extract**: Reads raw airport data from [OurAirports CSV Dataset](https://davidmegginson.github.io/ourairports-data/airports.csv)
- **Transform**: Selects and renames relevant columns with `pandas`
- **Load**: Inserts the cleaned data into a PostgreSQL table
- **Dockerized**: Run the whole pipeline in isolated containers

---

## Tech Stack

- Python 3.10  
- pandas  
- psycopg2  
- PostgreSQL 14  
- Docker & Docker Compose  
- `.env` file for environment config  
- Logging to `.log` file for ETL runs

---

## How to Run

```bash
1. Clone this repo
git clone https://github.com/Jamorno/Airports-ETL-Docker.git

2. Create a `.env` file

DB_HOST=db
DB_PORT=5432
DB_NAME=airports_etl
DB_USER=postgres
DB_PASSWORD=postgres

3. Build and run with Docker Compose
docker compose up --build