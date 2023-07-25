from playwright.sync_api import Page, expect

# Test checks visibility of links when hovering above 'oferta' field, urls after clicking links, and style changes
# when hovering above links in drop down 'oferta' menu.


def locators(page: Page):
    links_oferta = [page.get_by_role("link", name="Psychodietetyka"),
                    page.get_by_role("link", name="Indywidualne wkładki ortopedyczne"),
                    page.get_by_role("link", name="Terapia manualna"),
                    page.get_by_role("link", name="Pijawki lekarskie"),
                    page.get_by_role("link", name="Pinoterapia"),
                    page.get_by_role("link", name="Psychoterapia"),
                    page.get_by_role("link", name="Terapia wisceralna"),
                    page.get_by_role("link", name="Akupunktura"),
                    page.get_by_role("link", name="Refleksoterapia"),
                    page.get_by_role("link", name="Masaż Kobido"),
                    page.get_by_role("link", name="Misy tybetanskie"),
                    page.get_by_role("link", name="Chiropraktyka"),
                    page.get_by_role("link", name="Joga"),
                    page.get_by_role("link", name="Masaż leczniczy"),
                    page.get_by_role("link", name="Fizjoterapia stomatologiczna")]
    return links_oferta


def test_is_drop_down_menu_content_visible_when_hover(page: Page):
    page.goto("/")
    links_oferta = locators(page)
    while page.locator("app-nav").get_by_role("link", name="Oferta").hover():
        for link in links_oferta:
            expect(link).to_be_visible()


def test_is_drop_down_menu_content_change_color_when_hover(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    count = page.get_by_role("link").filter(has=page.locator("small")).count()

    for i in range(count-1):
        page.locator("app-nav").get_by_role("link", name="Oferta").hover()
        row = page.get_by_role("link").filter(has=page.locator("small")).nth(i)
        page.locator("app-nav").get_by_role("link", name="Oferta").hover()
        row.hover()
        expect(row).to_have_css(name="background-color", value="rgb(133, 178, 75)")


def test_is_drop_down_menu_content_not_visible_without_hover(page: Page):
    page.goto("/")
    links_oferta = locators(page)
    for link in links_oferta:
        expect(link).not_to_be_visible()


def test_clicking_drop_down_menu_content_psychodietetyka(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Psychodietetyka").click()
    expect(page).to_have_url("/oferta/psychodietetyka")


def test_clicking_drop_down_menu_content_indywidualne_wkladki(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Indywidualne wkładki ortopedyczne").click()
    expect(page).to_have_url("/oferta/indywidualne-wkladki-ortopedyczne")


def test_clicking_drop_down_menu_content_terapia_manualna(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Terapia manualna").click()
    expect(page).to_have_url("/oferta/terapia-manualna")


def test_clicking_drop_down_menu_content_pijawki_lekarskie(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Pijawki lekarskie").click()
    expect(page).to_have_url("/oferta/pijawki-lekarskie")


def test_clicking_drop_down_menu_content_pinoterapia(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Pinoterapia").click()
    expect(page).to_have_url("/oferta/pinoterapia")


def test_clicking_drop_down_menu_content_psychoterapia(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Psychoterapia").click()
    expect(page).to_have_url("/oferta/psychoterapia")


def test_clicking_drop_down_menu_content_terapia_wisceralna(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Terapia wisceralna").click()
    expect(page).to_have_url("/oferta/terapia-wisceralna")


def test_clicking_drop_down_menu_content_akupunktura(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Akupunktura").click()
    expect(page).to_have_url("/oferta/akupunktura")


def test_clicking_drop_down_menu_content_refleksoterapia(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Refleksoterapia").click()
    expect(page).to_have_url("/oferta/refleksoterapia")


def test_clicking_drop_down_menu_content_kobido(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Masaż Kobido").click()
    expect(page).to_have_url("/oferta/kobido")


def test_clicking_drop_down_menu_content_misy_tybetanskie(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Misy tybetanskie").click()
    expect(page).to_have_url("/oferta/misy-tybetanskie")


def test_clicking_drop_down_menu_content_chiropraktyka(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Chiropraktyka").click()
    expect(page).to_have_url("/oferta/chiropraktyka")


def test_clicking_drop_down_menu_content_joga(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Joga").click()
    expect(page).to_have_url("/oferta/joga")


def test_clicking_drop_down_menu_content_masaz_leczniczy(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Masaż leczniczy").click()
    expect(page).to_have_url("/oferta/masaz-leczniczy")


def test_clicking_drop_down_menu_content_fizjoterapia_stomatologiczna(page: Page):
    page.goto("/")
    page.locator("app-nav").get_by_role("link", name="Oferta").hover()
    page.get_by_role("link", name="Fizjoterapia stomatologiczna").click()
    expect(page).to_have_url("/oferta/fizjoterapia-stomatologiczna")
