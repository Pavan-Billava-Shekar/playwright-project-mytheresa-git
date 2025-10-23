from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url

    def goto(self):
        self.page.goto(self.url)    #Open the home page

    def get_all_links(self):
        #get list of all hrefs on the page
        return self.page.eval_on_selector_all("a", "elements => elements.map(el => el.href)")

    def check_links_status(self):
        links = self.get_all_links()
        failed_links = []
        passed_links = []

        for link in links:
            if not link:  # skip empty hrefs
                continue
            try:
                response = self.page.request.get(link)
                status = response.status
                print(f"Checking {link} -> Status: {status}")

                if status >= 400:
                    failed_links.append(f"{link} returned {status}")
                elif status == 200:
                    passed_links.append(f"{link} returned {status}")
                else:
                    passed_links.append(f"{link} returned {status}")
            except Exception as e:
                failed_links.append(f"{link} failed with exception: {e}")

        return passed_links, failed_links
