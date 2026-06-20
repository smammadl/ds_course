---
title: Streamlit Project
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Streamlit template space
---

# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire.

# Run the app locally

## Step 1: Build the Docker Image

```bash
docker build -t my-streamlit-app .
```
> This will build the Docker image and tag it as `my-streamlit-app`.
> `.` is the location of the Dockerfile.

## Step 2: Run the Docker Container

```bash
docker run -p 8501:8501 my-streamlit-app
```
> This will run the Docker container. Use `-d` to run the container in the background.
> Use `-p 8501:8501` to map the port 8501 on the host to the port 8501 on the container.

## Step 3: Open the app in the browser

```bash
open http://localhost:8501
```
> This will open the app in the browser.