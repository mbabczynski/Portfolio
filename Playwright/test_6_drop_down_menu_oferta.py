from playwright.sync_api import Page, expect


# Test checks visibility of links when hovering above 'oferta' field, urls after clicking links, and style changes
# when hovering above links in drop down 'oferta' menu.


def locators(page: Page):  # returns dictionary with link buttons locators as key and endpoint as a value
    links_oferta = {page.get_by_role("link", name="Psychodietetyka"): "/oferta/psychodietetyka",
                    page.get_by_role("link", name="Indywidualne wkładki ortopedyczne"): "/oferta/indywidualne-wkladki-ortopedyczne",
                    page.get_by_role("link", name="Terapia manualna"): "/oferta/terapia-manualna",
                    page.get_by_role("link", name="Pijawki lekarskie"): "/oferta/pijawki-lekarskie",
                    page.get_by_role("link", name="Pinoterapia"): "/oferta/pinoterapia",
                    page.get_by_role("link", name="Psychoterapia"): "/oferta/psychoterapia",
                    page.get_by_role("link", name="Terapia wisceralna"): "/oferta/terapia-wisceralna",
                    page.get_by_role("link", name="Akupunktura"): "/oferta/akupunktura",
                    page.get_by_role("link", name="Refleksoterapia"): "/oferta/refleksoterapia",
                    page.get_by_role("link", name="Masaż Kobido"): "/oferta/kobido",
                    page.get_by_role("link", name="Misy tybetanskie"): "/oferta/misy-tybetanskie",
                    page.get_by_role("link", name="Chiropraktyka"): "/oferta/chiropraktyka",
                    page.get_by_role("link", name="Joga"): "/oferta/joga",
                    page.get_by_role("link", name="Masaż leczniczy"): "/oferta/masaz-leczniczy",
                    page.get_by_role("link", name="Fizjoterapia stomatologiczna"): "/oferta/fizjoterapia-stomatologiczna"}
    return links_oferta


def test_is_drop_down_menu_content_visible_when_hover(page: Page):
    page.goto("/")
    links_oferta = locators(page)
    while page.locator("app-nav").get_by_role("link", name="Oferta").hover():
        for key in links_oferta:
            expect(key).to_be_visible()


def test_is_drop_down_menu_content_not_visible_without_hover(page: Page):
    page.goto("/")
    links_oferta = locators(page)
    for key in links_oferta:
        expect(key).not_to_be_visible()


def test_is_drop_down_menu_content_change_color_when_hover(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    count = page.get_by_role("link").filter(has=page.locator("small")).count()

    for i in range(count - 1):
        page.locator("app-nav").get_by_role("link", name="Oferta").hover()
        row = page.get_by_role("link").filter(has=page.locator("small")).nth(i)
        page.locator("app-nav").get_by_role("link", name="Oferta").hover()
        row.hover()
        expect(row).to_have_css(name="background-color", value="rgb(133, 178, 75)")


def test_clicking_drop_down_menu_content(page: Page):
    page.goto("/")
    links_oferta = locators(page)
    for key, value in links_oferta.items():
        page.locator("app-nav").get_by_role("link", name="Oferta").hover()
        key.click()
        expect(page).to_have_url(value)
