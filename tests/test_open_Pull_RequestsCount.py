from pages.openPullPage import GitHubPRPage


def test_github_open_prs(page, repo_url):
    """verify user is able to Fetch all open PRs and save them to CSV."""
    github_page = GitHubPRPage(page, repo_url) # navigate to gitrepo url
    github_page.goto()
    prs = github_page.get_all_open_prs()    #fetch open prs
    csv_path = github_page.save_prs_to_csv(prs) # write to CSV file
    print(f"Saved {len(prs)} open PRs to {csv_path}")
    assert prs, "No open PRs found"
