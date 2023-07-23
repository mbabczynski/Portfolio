from playwright.sync_api import Page, expect


def test_email_invalid(page: Page):
    page.goto("/kontakt")
    expect(page.get_by_text("Nieprawidłowy adres e-mail")).not_to_be_visible()
    page.get_by_placeholder("e-mail..").click()
    page.get_by_placeholder("e-mail..").fill("abcabc.com")
    expect(page.get_by_text("Nieprawidłowy adres e-mail")).to_be_visible()


def test_email_valid(page: Page):
    page.goto("/kontakt")
    expect(page.get_by_text("Nieprawidłowy adres e-mail")).not_to_be_visible()
    page.get_by_placeholder("e-mail..").click()
    page.get_by_placeholder("e-mail..").fill("abc@abc.com")
    expect(page.get_by_text("Nieprawidłowy adres e-mail")).not_to_be_visible()


def test_name_invalid(page: Page):
    page.goto("/kontakt")
    expect(page.get_by_text("Pole imię jest wymagane")).not_to_be_visible()
    page.get_by_placeholder("Imię..").click()
    page.get_by_placeholder("Nazwisko..").click()
    expect(page.get_by_text("Pole imię jest wymagane")).to_be_visible()


def test_name_valid(page: Page):
    page.goto("/kontakt")
    expect(page.get_by_text("Pole imię jest wymagane")).not_to_be_visible()
    page.get_by_placeholder("Imię..").click()
    page.get_by_placeholder("Imię..").fill("Jan")
    page.get_by_placeholder("Nazwisko..").click()
    expect(page.get_by_text("Pole imię jest wymagane")).not_to_be_visible()

