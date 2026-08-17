from app.services.web_fetcher import WebFetchError, fetch_page


def main():
    url = input("Enter a public webpage URL: ").strip()

    if not url:
        print("\nError: The webpage URL cannot be empty.")
        return

    try:
        html = fetch_page(url)

    except WebFetchError as error:
        print(f"\nError: {error}")
        return

    print(f"\nDownloaded {len(html)} characters.")
    print("\nFirst 300 characters of the webpage:\n")
    print(html[:300])


if __name__ == "__main__":
    main()
