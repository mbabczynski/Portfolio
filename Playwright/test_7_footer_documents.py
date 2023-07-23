from playwright.sync_api import Page, expect
import re


def test_footer_rodo(page: Page):
    page.goto("/")
    page.get_by_text("Rodo").click()
    expect(page.frame_locator("app-document-preview iframe").get_by_text(re.compile("OBOWIĄZEK INFORMACYJNY", re.IGNORECASE))).to_be_visible()
    page.locator("app-document-preview").get_by_role("img").click()
    expect(page.frame_locator("app-document-preview iframe").get_by_text(re.compile("OBOWIĄZEK INFORMACYJNY", re.IGNORECASE))).not_to_be_visible()


def test_footer_regulamin(page: Page):
    page.goto("/")
    page.get_by_text("Regulamin").click()
    expect(page.frame_locator("app-document-preview iframe").get_by_text(re.compile("REGULAMIN UDZIELANIA ŚWIADCZEŃ ZDROWOTNYCH", re.IGNORECASE))).to_be_visible()
    page.locator("app-document-preview").get_by_role("img").click()
    expect(page.frame_locator("app-document-preview iframe").get_by_text(re.compile("REGULAMIN UDZIELANIA ŚWIADCZEŃ ZDROWOTNYCH", re.IGNORECASE))).not_to_be_visible()
