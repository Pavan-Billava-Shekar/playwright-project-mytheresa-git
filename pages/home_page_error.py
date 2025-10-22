from playwright.sync_api import Page, ConsoleMessage

class HomePageError:

    def __init__(self, page: Page):
        self.page = page
        self.console_errors = []
        self.page.on("console", self._capture_console_error)

    def _capture_console_error(self, msg: ConsoleMessage):
        if msg.type == "error":
            self.console_errors.append(msg.text)

    def navigate(self, url: str):
        self.page.goto(f"{url}about.html",wait_until="load")
        self.page.wait_for_timeout(2000)

    def get_console_errors(self):
        return self.console_errors
