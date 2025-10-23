import requests
import pandas as pd

class GithubPRsPage:
    def __init__(self, owner, repo, token=None):
        self.owner = owner
        self.repo = repo
        self.api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def fetch_and_save_open_prs(self, filename=None):
        all_prs = []
        per_page = 100
        page = 1
        while True:
            params = {"state": "open", "per_page": per_page, "page": page}
            response = requests.get(self.api_url, headers=self.headers, params=params)
            response.raise_for_status()
            prs = response.json()
            if not prs:
                break
            for pr in prs:
                all_prs.append({
                    "PR Name": pr["title"],
                    "Author": pr["user"]["login"],
                    "Created Date": pr["created_at"]
                })
            page += 1
        if not filename:
            filename = f"{self.repo}_open_prs.xlsx"
        df = pd.DataFrame(all_prs)
        df.to_excel(filename, index=False)
        print(f"Saved {len(all_prs)} open PRs to '{filename}'.")
        return all_prs
