from playwright.sync_api import Page, expect

# Test counting FAQ content and make sure that every hidden box in FAQ page showing after clicking proper arrow, and hiding after second click.


def test_faq_content_expanding(page: Page):

    page.goto("/faq")
    count = page.get_by_text("▼").count()

    for i in range(count):
        arrow = page.get_by_text("▼").nth(i)
        expect(page.locator('.hidden-box').nth(i)).not_to_be_visible()
        arrow.click()
        expect(page.locator('.hidden-box').nth(i)).to_be_visible()
        arrow.click()
        expect(page.locator('.hidden-box').nth(i)).not_to_be_visible()

