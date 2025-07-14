# particle41-assignment

# 1. SimpleTimeService

A minimal Flask-based microservice that returns the current UTC timestamp and the IP address of the client in JSON format.

## 🔧 Features

- Returns current timestamp in ISO 8601 format
- Shows IP address of the requester
- Lightweight container image using Python 3.11-slim
- Runs as a **non-root user**

---

## 🚀 How to Deploy

### 1. Pull and run the Docker image

```bash
docker pull riddhigala18/simple-time-service:latest
```
``` bash
docker run -d -p 5000:5000 simple-time-service:latest 
```
### 2. Test the service

```bash
curl http://localhost:5000/
```
Expected response:
```json
{
    "ip":"172.17.0.1",
    "timestamp":"2025-07-14T06:00:29.333965Z"
}
```

# Task 2 - Terraform and Cloud: create the infrastructure to host your container.

## ⚙️ Prerequisites

### 1. Create an IAM user with the following permissions:
   - AmazonEC2FullAccess
   - AmazonECS_FullAccess
   - AmazonECRFullAccess
   - IAMFullAccess
   - ElasticLoadBalancingFullAccess
### 2. Create and store the following secrets in your GitHub repo:
   - Step 1: Open Your GitHub Repository
   - Step 2: Go to Secrets Settings
     - Click on **Settings** (top tab in the repository).
     -  In the left sidebar, go to: **Secrets and variables** → **Actions**
     -  Click on **"New repository secret"**
   - Step 3: Add Your AWS Secrets
     -You need to add at least **two secrets** from your AWS IAM credentials:

      | Secret Name              | Value (from AWS Console)             |
      |--------------------------|--------------------------------------|
      | `AWS_ACCESS_KEY_ID`      | Your access key ID (e.g., `AKIA...`) |
      | `AWS_SECRET_ACCESS_KEY`  | Your secret access key               |

      > ⚠️ **Important:** Never share these keys publicly.

      ### 🔧 Example

        - **Name:** `AWS_ACCESS_KEY_ID`  
        - **Value:** `AKIAIOSFODNN7EXAMPLE`

        Click **"Add secret"** after entering each one.

### 3. Create a Private Repo on Amazon ECR named: simple-time-service
  I have already push the image on my repo.

## 🚀 How to Deploy (CI/CD will handle it):

### 1. Fork or clone this repo.
### 2. Go to GitHub Actions -> CI/CD Pipline - Docker + Terraform -> Run Workflow
### 3. Select branch 'main'
### 4. If you want to build and publish new docker image then type 'true' or else if you want to reuse the existig image from the repo then type 'false'.
### 5. This will:
   - Build your Docker image from SimpleTimeService/
   - Push it to AWS ECR
   - Apply Terraform to create/update the infrastructure
### 6. After deployment, ** get the ALB DNS from Terraform outputs or AWS Console → EC2 → Load Balancers **
### 7. Open any browser and type: `http://<alb-dns>:5000`

Expected response:
```json
{
    "ip":"172.17.0.1",
    "timestamp":"2025-07-14T06:00:29.333965Z"
}
```
### 6. To Destroy the infrastructure created in 'step5', go to GitHub Actions -> Destroy Infrastructure -> Run Workflow and Select branch 'main'.
          
