import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "https://www.revue-technique-auto.fr"


def get_brands():
    url = "https://www.revue-technique-auto.fr/codes-defauts-obd"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    brands = []
    brand_list = soup.find('ul', class_='brandList')
    for li in brand_list.find_all('li', class_='product_list_element'):
        brand_name = li.find('h3').text.strip()
        brand_url = li.find('a')['href']
        brands.append((brand_name, brand_url))

    return brands


def get_categories(brand_url):
    response = requests.get(brand_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    categories = []
    obd_list = soup.find('div', class_='obdListCode')
    if obd_list:
        for li in obd_list.find_all('li'):
            category_name = li.text.strip()
            category_url = li.find('a')['href']
            categories.append((category_name, category_url))

    return categories


def get_codes(category_url):
    codes = []
    page = 1
    while True:
        paginated_url = f"{category_url}?p={page}" if page > 1 else category_url
        response = requests.get(paginated_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract codes from current page
        table = soup.find('table', class_='tableObd')
        if table:
            for row in table.find_all('tr')[1:]:  # Skip header row
                cols = row.find_all('td')
                if len(cols) == 2:
                    code = cols[0].text.strip()
                    description = cols[1].text.strip()
                    codes.append((code, description))

        # Check for pagination
        pagination = soup.find('div', class_='paginationObd')
        if not pagination:
            break

        # Check if there's a next page
        current_page_span = pagination.find('span', string=lambda text: 'Page' in str(text))
        if not current_page_span:
            break

        current_page_text = current_page_span.text.strip()
        current_page, total_pages = map(int, current_page_text.replace('Page', '').replace(' ', '').split('/'))

        if page >= total_pages:
            break

        page += 1

    return codes


def main():
    with open('obd_codes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Brand', 'Category', 'Code', 'Description'])

        brands = get_brands()
        for brand_name, brand_url in brands:
            print(f"Processing brand: {brand_name}")

            categories = get_categories(brand_url)
            for category_name, category_url in categories:
                print(f"  Processing category: {category_name}")

                codes = get_codes(category_url)
                for code, description in codes:
                    writer.writerow([brand_name, category_name, code, description])

    print("Scraping completed. Data saved to obd_codes.csv")


if __name__ == "__main__":
    main()