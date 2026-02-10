from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI()
GITHUB_API = "https://api.github.com"

@app.get("/{username}")
def get_gists(
    username: str,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    url = f"{GITHUB_API}/users/{username}/gists"
    params = {"page": page, "per_page": per_page}
    response = requests.get(url, params=params)

    if response.status_code == 403:
        raise HTTPException(status_code=429, detail="GitHub API rate limit exceeded")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="GitHub user not found")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching data from GitHub")

    return [
        {
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"],
            "created_at": gist["created_at"]
        }
        for gist in response.json()
    ]
