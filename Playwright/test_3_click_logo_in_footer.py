from time import sleep
from playwright.sync_api import Page, expect

# Test checks page url (homepage) after clicking logo in footer

def test_click_logo_in_footer(page: Page) -> None:
    page.goto("/")
    page.locator("app-footer").get_by_role("link",
    name="fizjoterapia medycyna manualna szczecin Marika Kopaczyk").click()
    sleep(2)
    expect(page).to_have_url("/home")


