from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Avvia il browser (headless=False per vedere l'azione)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Naviga verso un sito di test
        page.goto("https://example.com")

        # Interagisci con la pagina
        print("Titolo della pagina:", page.title())
        
        # Esempio di compilazione form
        # page.fill("#username", "my_username")
        # page.fill("#password", "my_password")
        # page.click("button[type='submit']")

        # Attendi qualche secondo per osservare
        page.wait_for_timeout(3000)

        browser.close()

if __name__ == "__main__":
    main()
