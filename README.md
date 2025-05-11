<h1 align="center">Welcome to Seek Job Scraper App 👋</h1>

> A project to scrape job listings from [Seek.com.au](https://www.seek.com.au) and expose the data via an API. Designed for developers and researchers interested in programmatically accessing job advertisement data for analysis or integration.

## 📁 Project Structure

```
.
├── api-web-scraper         # Backend API exposing the scraped job data
├── seek-web-scraper        # Scraper logic to collect job postings from Seek
├── .github/workflows       # GitHub Actions CI/CD configuration
├── .gitignore
```

## 🚀 Features

- Scrapes job listings from Seek
- API interface to serve job data
- Advertiser schema support
- GitHub Actions workflow for deployment

## 🛠️ Technologies Used

- Python 3.11
- FastAPI
- Docker
- GitHub Actions for CI/CD

## 🚀 Backend API Deployment (GitHub Actions + Amazon ECR + AWS Lambda)

This project uses **GitHub Actions** to automatically deploy the FastAPI backend to **AWS Lambda** using a Docker container image stored in **Amazon ECR**.

### 🔁 Deployment Workflow

The deployment is triggered on pushes to the `master` branch that affect:

- The `api-web-scraper/` directory
- The workflow file itself

### 📂 Workflow File: `.github/workflows/deploy-api-seek-web-scraper.yml`

Key steps in the workflow:

1. **Checkout the code**
2. **Set up Python 3.11**
3. **Configure AWS credentials using GitHub Secrets**
4. **Login to Amazon ECR**
5. **Build and push Docker image to ECR**
6. **Prune Docker images to free space**
7. **Deploy image to AWS Lambda**

## Author

👤 **Welisson Lima**

* Github: [@whflima](https://github.com/whflima)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/welisson-lima\/](https://linkedin.com/in/welisson-lima)

## Show your support

Give a ⭐️ if this project helped you!

***
