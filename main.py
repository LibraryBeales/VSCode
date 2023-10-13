from playwright.sync_api import sync_playwright
import time
from rich import print

def scroll_me():
    def check_json(response):
        if "products" in response.url:
            print({"url": response.url, "body":response.json()})

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(
            {"width": 1280, "height": 1080}
            )
        page.on("response", lambda response:print(response.url))
        page.goto("https://www.nike.com/gb/w/mens-shoes-nik1zy7ok")
        time.sleep(2)
        #page.click("#hf_cookie_text_cookieAccept")
        page.wait_for_load_state("networkidle")
        #scroll down
        for x in range(1,10):
            page.mouse.wheel(0, 15000)
            print("scrolling key press, x")
            time.sleep(1)
            #await page.locator('button:text("Show More")').click();
        browser.close

def main():
    scroll_me()


if __name__ == "__main__":
    main()







'''with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://google.com")
'''