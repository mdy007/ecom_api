from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Missing query parameter "q"'}), 400

    url = f'https://www.amazon.in/s?k={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', {'class': 's-result-item'})

    results = []
    for product in products:
        name_element = product.find('h2', {'class': 'a-size-mini'})
        if not name_element:
            continue
        name = name_element.text.strip()

        image_element = product.find('img', {'class': 's-image'})
        if not image_element:
            continue
        image = image_element['src']

        price_element = product.find('span', {'class': 'a-price-whole'})
        if not price_element:
            continue
        price = price_element.text.strip()

        results.append({
            'name': name,
            'image': image,
            'price': price
        })
        break # stop after first product found

    if results:
        return jsonify({'results': {'amazon': results[0]}})
    else:
        return jsonify({'error': 'No results found'}), 404

if __name__ == '__main__':
    app.run()
