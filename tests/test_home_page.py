
import re
import time
from src.base.web_base import WebBase
from playwright.sync_api import expect


class TestSuite(WebBase):
    def test_playwright_page_url(self, page):
        expect(page).to_have_title(re.compile("Google"))

    def test_enter_text(self,page):
        page.locator("#APjFqb").click()
        page.locator("#APjFqb").fill("Hello")
        expect( page.locator("#APjFqb")).to_have_value("Hello")


