import os
import csv
from playwright.sync_api import Page

class GitHubPRPage:

    def __init__(self, page: Page, repo_url: str):
        self.page = page
        self.url = repo_url

    def goto(self):
        self.page.goto(self.url)

    def get_all_open_prs(self):
        all_prs = []

        while True:
            # Wait for PR rows to appear
            self.page.wait_for_selector("div.js-issue-row")
            pr_elements = self.page.query_selector_all("div.js-issue-row")

            # get PRs on current page
            for pr in pr_elements:
                title = pr.query_selector("a.Link--primary").inner_text().strip()
                author = pr.query_selector("a.Link--muted").inner_text().strip()
                created_at = pr.query_selector("relative-time").get_attribute("datetime")
                all_prs.append({"title": title, "author": author, "created_at": created_at})

            # Check if a Next page exists
            next_btn = self.page.query_selector("a[rel='next']")
            if next_btn and next_btn.is_visible():
                next_url = next_btn.get_attribute("href")
                self.page.goto("https://github.com" + next_url)
            else:
                break

        return all_prs

    def save_prs_to_csv(self, prs, folder="reports", filename="open_prs.csv"):
        os.makedirs(folder, exist_ok=True)
        csv_path = os.path.join(folder, filename)
        with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "author", "created_at"])
            writer.writeheader()
            for pr in prs:
                writer.writerow(pr)
        return csv_path
