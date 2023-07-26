import pytest
from playwright.sync_api import Page, expect
# Test checks work of hamburger menu in mobile view, asserts url, title, and focus on valid button in hamburger menu.


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["Galaxy S8"]}


def locators(page: Page):   # list of dictionaries of links in top navigation bar containing button(locator) ,
                            # url, and title of each link.
    top_navigation_bar = [{'button': page.locator("app-nav").get_by_role("link", name="Strona główna"),
                           'url': "/",
                           'title': "Fizjoterapia i rehabilitacja w Szczecinie – centrum FizjoNature"},
                          {'button': page.locator("app-nav").get_by_role("link", name="Zespół"),
                           'url': "/zespol",
                           'title': "Poznaj zespół centrum  fizjoterapii i rehabilitacji w Szczecinie"},
                          {'button': page.locator("app-nav").get_by_role("link", name="Oferta"),
                           'url': "/oferta",
                           'title': "Zabiegi manualne – zabiegi fizjoterapii i rehabilitacji"},
                          {'button': page.locator("app-nav").get_by_role("link", name="Cennik"),
                           'url': "/cennik",
                           'title': "Cennik centrum medycyny manualnej w Szczecinie – ceny zabiegów"},
                          {'button': page.locator("app-nav").get_by_role("link", name="Blog"),
                           'url': "/blog",
                           'title': "Blog centrum fizjoterapii i rehabilitacji w Szczecinie"},
                          {'button': page.locator("app-nav").get_by_role("link", name="FAQ"),
                           'url': "/faq",
                           'title': "FAQ centrum medycyny manualnej – najczęstsze pytania pacjentów"},
                          {'button': page.locator("app-nav").get_by_role("link", name="Kontakt"),
                           'url': "/kontakt",
                           'title': "Kontakt z centrum medycyny manualnej FizjoNature w Szczecinie"}
                          ]
    return top_navigation_bar


def test_top_navigation_bar_mobile(page: Page):
    page.goto("/")
    page.get_by_role('button', name="Akceptuj").click()
    page.locator('id=nav-icon4').click()
    subpages = locators(page)
    for subpage in subpages:
        subpage['button'].click()
        page.wait_for_load_state('load')
        expect(page).to_have_url(subpage['url'])
        expect(page).to_have_title(subpage['title'])
        page.locator('id=nav-icon4').click()
        expect(subpage['button']).to_be_focused()
        for i in subpages:
            if i != subpage:
                expect(i['button']).not_to_be_focused()


