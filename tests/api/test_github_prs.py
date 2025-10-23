import pytest

from pages.github_api_page import GithubPRsPage

TOKEN = None
@pytest.mark.asyncio
@pytest.mark.api
async def test_fetch_and_save_prs(repo_list):
    for repo in repo_list:
        github_page = GithubPRsPage(owner=repo["owner"], repo=repo["name"], token=TOKEN)
        prs = github_page.fetch_and_save_open_prs()
        assert prs, f"No open PRs found for {repo['name']}!"
