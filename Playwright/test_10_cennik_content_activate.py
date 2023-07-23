from playwright.sync_api import Page, expect

# This test counting rows in Cennik page and check is every row change color after hovering mouse above.

css_name = 'background'
css_value = 'linear-gradient(135deg, rgb(121, 183, 67), rgb(88, 178, 141)) repeat scroll 0% 0% / auto padding-box border-box, rgb(133, 178, 75) none repeat scroll 0% 0% / auto padding-box border-box'


def test_blog_search(page: Page):
    page.goto("/cennik")
    count = page.get_by_role("row").count()
    for i in range(count-1):
        page.get_by_role("row").nth(i+1).hover()
        expect(page.get_by_role("row").nth(i+1)).to_have_css(name= css_name, value= css_value)



