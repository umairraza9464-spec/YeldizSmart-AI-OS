from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, headless: bool = False):
        self.headless = headless
        self._playwright = None
        self._browser = None
        self.contexts = {}

    def start(self):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self.headless)
        return self

    def stop(self):
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()

    def new_context(self, name: str, proxy: dict | None = None):
        if proxy:
            context = self._browser.new_context(proxy=proxy)
        else:
            context = self._browser.new_context()
        self.contexts[name] = context
        return context

    def new_page(self, context_name: str):
        ctx = self.contexts[context_name]
        return ctx.new_page()
