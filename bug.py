import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract titles and paragraphs
    titles = soup.find_all('h1')
    paragraphs = soup.find_all('p')
    data = {
        'titles': [title.get_text() for title in titles],
        'paragraphs': [para.get_text() for para in paragraphs]
    }
    return data

def main():
    url = 'https://example.com'  # Replace with the target URL
    html = fetch_data(url)
    if html:
        data = parse_data(html)
        print("Titles:")
        for title in data['titles']:
            print(title)
        print("\nParagraphs:")
        for para in data['paragraphs']:
            print(para)

if __name__ == "__main__":
    main()
