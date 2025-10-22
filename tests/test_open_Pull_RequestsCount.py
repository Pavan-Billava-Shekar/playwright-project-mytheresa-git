from pages.openPullPage import GitHubPRPage


def test_github_open_prs(page, repo_url):
    """Fetch all open PRs and save them to CSV."""
    github_page = GitHubPRPage(page, repo_url)
    github_page.goto()

    prs = github_page.get_all_open_prs()
    csv_path = github_page.save_prs_to_csv(prs)

    print(f"Saved {len(prs)} open PRs to {csv_path}")

    assert prs, "No open PRs found"
