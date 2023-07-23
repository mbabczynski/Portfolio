from playwright.sync_api import Page, expect
import re


def test_blog_search(page: Page):
    page.goto("/blog")
    page.get_by_placeholder("Szukaj").fill("stopa")
    page.get_by_placeholder("Szukaj").press("Enter")
    expect(page.get_by_role("link", name=re.compile("Czym może grozić nadmierna pronacja stopy?", re.IGNORECASE))).to_be_visible()

