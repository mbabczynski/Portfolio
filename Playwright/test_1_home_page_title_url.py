from playwright.sync_api import Page, expect

# Test checks are page url and title are correct

def test_homepage_title_and_url(page: Page):
    page.goto('/')
    expect(page).to_have_title("Fizjoterapia i rehabilitacja w Szczecinie – centrum FizjoNature")
    expect(page).to_have_url('/')



