
from playwright.sync_api import Page, expect

# Tests asserting URL, title and focus on proper button after clicking on each link in top navigation bar


def test_top_navigation_bar_home(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Strona główna").click()
    expect(page).to_have_url("/")
    expect(page).to_have_title("Fizjoterapia i rehabilitacja w Szczecinie – centrum FizjoNature")
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Zespół")).not_to_be_focused()


def test_top_navigation_bar_zespol(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Zespół").click()
    expect(page).to_have_url("/zespol")
    expect(page).to_have_title("Poznaj zespół centrum  fizjoterapii i rehabilitacji w Szczecinie")
    expect(page.locator("app-nav").get_by_role("link", name="Zespół")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()


def test_top_navigation_bar_oferta(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").click()
    expect(page).to_have_url("/oferta")
    expect(page).to_have_title("Zabiegi manualne – zabiegi fizjoterapii i rehabilitacji")
    expect(page.locator("app-nav").get_by_role("link", name="Oferta")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()


def test_top_navigation_bar_cennik(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Cennik").click()
    expect(page).to_have_url("/cennik")
    expect(page).to_have_title("Cennik centrum medycyny manualnej w Szczecinie – ceny zabiegów")
    expect(page.locator("app-nav").get_by_role("link", name="Cennik")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()


def test_top_navigation_bar_blog(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Blog").click()
    expect(page).to_have_url("/blog")
    expect(page).to_have_title("Blog centrum fizjoterapii i rehabilitacji w Szczecinie")
    expect(page.locator("app-nav").get_by_role("link", name="Blog")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()


def test_top_navigation_bar_faq(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="FAQ").click()
    expect(page).to_have_url("/faq")
    expect(page).to_have_title("FAQ centrum medycyny manualnej – najczęstsze pytania pacjentów")
    expect(page.locator("app-nav").get_by_role("link", name="FAQ")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()


def test_top_navigation_bar_kontakt(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Kontakt").click()
    expect(page).to_have_url("/kontakt")
    expect(page).to_have_title("Kontakt z centrum medycyny manualnej FizjoNature w Szczecinie")
    expect(page.locator("app-nav").get_by_role("link", name="Kontakt")).to_be_focused()
    expect(page.locator("app-nav").get_by_role("link", name="Strona główna")).not_to_be_focused()




