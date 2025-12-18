import time
from typing import Literal

class AccountSession:
    def __init__(self, name: str, platform: Literal["fb", "olx"], page):
        self.name = name
        self.platform = platform
        self.page = page
        self.active = True
        self.current_city = None

    def set_city(self, city: str):
        self.current_city = city

    def run_once(self):
        if not self.active:
            return
        # TODO: yahan FB/OLX scraping + AI calls integrate honge
        print(f"[{self.platform.upper()}][{self.name}] running in city={self.current_city}")

    def loop(self, interval_sec: int = 30):
        while True:
            self.run_once()
            time.sleep(interval_sec)
