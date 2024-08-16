from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def setup(page:Page):
    page.goto("https://www.google.com/")
    yield page