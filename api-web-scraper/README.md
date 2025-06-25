<h1 align="center">
  <p>Welcome to API Web Scraper 👋</p>
  <p>(Work in Progress)</p>
</h1>

> This directory contains the FastAPI backend for serving scraped job data via a RESTful API.

## 📦 Features

- Provides endpoints for accessing job listings.
- Built for deployment to AWS Lambda using Docker.

## 🔧 Main Files and Structure

- `main.py`: Entry point of the FastAPI application.
- `app/api/`: Defines the API routes and endpoints.
- `app/core/`: Configuration files such as:
  - `configs.py`: Environment and settings.
  - `database.py`: Database connections.
  - `container.py`: Dependency injection setup.
- `app/model/`: Defines the API database models.
- `app/repository/`: Data access layer (queries, inserts, updates).
- `app/service/`: Business logic layer.
- `app/schema/`: Pydantic models for request and response validation.
- `app/utils/`: Utility functions (e.g., AWS S3 integration).

## 📦 Setup & Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/seek-job-scraper.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd seek-job-scraper/api-web-scraper
   ```

2. **Run with Docker**
   ```bash
   docker build -t api-web-scraper .
   docker run -p 8000:8000 api-web-scraper
   ```

3. **Or set up a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Start FastAPI application server**
    ```bash
    uvicorn main:app --reload
    ```

> ⚠️ Make sure you have Docker and Python 3.11 installed.

## 📚 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/adveriser`        | Returns scraped job data |
