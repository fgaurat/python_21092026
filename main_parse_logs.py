from pprint import pprint
import requests
from bs4 import BeautifulSoup
import os


def main():
    os.makedirs('log_files', exist_ok=True)
    url = "https://logs.eolem.com"
    response = requests.get(url, verify=False)
    print(response.text)
    page = response.text

    soup = BeautifulSoup(page, "html.parser")

    all_a = soup.find_all('a')
    all_files = []
    for a in all_a:
        if a['href'].endswith('.log'):
            all_files.append(a['href'])

    for f in all_files:
        # "https://logs.eolem.com + apache_logs_01.log
        response = requests.get(f"{url}/{f}", verify=False)
        with open(f"log_files/{f}", "w") as log_file:
            log_file.write(response.text)


if __name__ == '__main__':
    main()
