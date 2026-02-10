# GitHub Gists API

This project provides a simple HTTP API that returns public GitHub gists for a user.

## Features
- Fetch public gists for a GitHub user
- Pagination support
- GitHub API rate-limit handling
- Automated tests
- Production-ready Docker image (non-root, small size)

## Prerequisites
- Docker installed

## Build the Docker image
docker build -t github-gists-api .

## Run the container
docker run -p 8080:8080 github-gists-api

## Test the API
curl "http://localhost:8080/octocat?page=1&per_page=5"

## Run tests locally (optional)
pytest

## Notes
- The application listens on port 8080
- No system-wide changes required
- Container runs as a non-root user
