from playwright.sync_api import Page, expect


def test_content_of_sub_pages_change_after_click(page: Page):
    # This test counts number of therapy titles, and after clicking on each title
    # checks is content of page changing.

    page.goto("/zespol")
    title_number = page.locator('.role-item--title').count()
    old_text = page.locator('.ql-editor.ng-star-inserted').inner_text()

    for t in range(title_number):
        page.locator('.role-item--title').nth(t).click()

        if t > 0:
            new_text = page.locator('.ql-editor.ng-star-inserted').inner_text()
            assert new_text != old_text
        old_text = page.locator('.ql-editor.ng-star-inserted').inner_text()


def test_visibility_of_names_and_photos(page: Page):
    # This test counts number of therapy titles, and after clicking on each title
    # checks visibility of all therapist's name and photo.

    page.goto("/zespol")
    title_number = page.locator('.role-item--title').count()

    for t in range(title_number):
        page.locator('.role-item--title').nth(t).click()
        person_number = page.locator(".person").count()
        for i in range(person_number):
            expect(page.locator(".person--photo").nth(i)).to_be_visible()
            expect(page.locator(".person--name").nth(i)).to_be_visible()

