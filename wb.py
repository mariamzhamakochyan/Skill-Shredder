import requests

def fetch_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None

if __name__ == "__main__":
    url = "https://www.example.com"  # Replace this with the URL of the webpage you want to fetch
    webpage_content = fetch_webpage(url)

    if webpage_content:
        print(webpage_content)

