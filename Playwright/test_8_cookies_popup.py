from playwright.sync_api import Page, expect
import re

#Test checks visibility of cookies pop-up, closing after clicking 'accept', and redirecting to privacy policy page after 'clicking read more...'

def test_cookies_prompt(page: Page):
    page.goto("/")
    expect(page.locator('id=policy-popup')).to_be_visible()


def test_cookies_accept(page: Page):
    page.goto("/")
    page.get_by_role("button", name=re.compile("akceptuj", re.IGNORECASE)).click()
    expect(page.locator('id=policy-popup')).not_to_be_visible()


def test_cookies_read_more(page: Page):
    page.goto("/")
    page.get_by_role("link", name=re.compile("czytaj więcej...", re.IGNORECASE)).click()
    expect(page).to_have_url("https://fizjonature.pl/polityka-prywatnosci")
