from app.services.web_fetcher import fetch_page


def main():
    url = input("Enter a public webpage URL: ").strip()

    html = fetch_page(url)

    print(f"\nDownloaded {len(html)} characters.")
    print("\nFirst 300 characters of the webpage:\n")
    print(html[:300])

if __name__ == "__main__":
    main()

