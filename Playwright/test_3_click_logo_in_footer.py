from time import sleep
from playwright.sync_api import Page, expect


# Test checks page url (homepage) after clicking logo in footer


def test_click_logo_in_footer(page: Page) -> None:
    page.goto("/zespol")
    page.locator("app-footer").get_by_role("link",
                                           name="fizjoterapia medycyna manualna szczecin").click()
    page.wait_for_load_state('load')
    sleep(3)
    expect(page).to_have_url("/")


