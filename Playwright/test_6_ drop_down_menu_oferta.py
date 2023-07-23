from playwright.sync_api import Page, expect


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


def test_is_drop_down_menu_content_visible_when_hover(page: Page):
    page.goto("/")
    while page.locator("app-nav").get_by_role("link", name="Oferta").hover():
        expect(page.get_by_role("link", name="Psychodietetyka")).to_be_visible()
        expect(page.get_by_role("link", name="Indywidualne wkładki ortopedyczne")).to_be_visible()
        expect(page.get_by_role("link", name="Terapia manualna")).to_be_visible()
        expect(page.get_by_role("link", name="Pijawki lekarskie")).to_be_visible()
        expect(page.get_by_role("link", name="Pinoterapia")).to_be_visible()
        expect(page.get_by_role("link", name="Psychoterapia")).to_be_visible()
        expect(page.get_by_role("link", name="Terapia wisceralna")).to_be_visible()
        expect(page.get_by_role("link", name="Akupunktura")).to_be_visible()
        expect(page.get_by_role("link", name="Refleksoterapia")).to_be_visible()
        expect(page.get_by_role("link", name="Masaż Kobido")).to_be_visible()
        expect(page.get_by_role("link", name="Misy tybetanskie")).to_be_visible()
        expect(page.get_by_role("link", name="Chiropraktyka")).to_be_visible()
        expect(page.get_by_role("link", name="Joga")).to_be_visible()
        expect(page.get_by_role("link", name="Masaż leczniczy")).to_be_visible()
        expect(page.get_by_role("link", name="Fizjoterapia stomatologiczna")).to_be_visible()

def test_is_drop_down_menu_content_not_visible_without_hover(page: Page):
    page.goto("/")
    expect(page.get_by_role("link", name="Psychodietetyka")).not_to_be_visible()
    expect(page.get_by_role("link", name="Indywidualne wkładki ortopedyczne")).not_to_be_visible()
    expect(page.get_by_role("link", name="Terapia manualna")).not_to_be_visible()
    expect(page.get_by_role("link", name="Pijawki lekarskie")).not_to_be_visible()
    expect(page.get_by_role("link", name="Pinoterapia")).not_to_be_visible()
    expect(page.get_by_role("link", name="Psychoterapia")).not_to_be_visible()
    expect(page.get_by_role("link", name="Terapia wisceralna")).not_to_be_visible()
    expect(page.get_by_role("link", name="Akupunktura")).not_to_be_visible()
    expect(page.get_by_role("link", name="Refleksoterapia")).not_to_be_visible()
    expect(page.get_by_role("link", name="Masaż Kobido")).not_to_be_visible()
    expect(page.get_by_role("link", name="Misy tybetanskie")).not_to_be_visible()
    expect(page.get_by_role("link", name="Chiropraktyka")).not_to_be_visible()
    expect(page.get_by_role("link", name="Joga")).not_to_be_visible()
    expect(page.get_by_role("link", name="Masaż leczniczy")).not_to_be_visible()
    expect(page.get_by_role("link", name="Fizjoterapia stomatologiczna")).not_to_be_visible()


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
