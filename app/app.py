from flask import Flask, render_template, request
import scraping


app = Flask(__name__)


@app.route('/cotizacion', methods=['GET'])
def datos():
    response_scrapping = scraping.obtener_cotizacion()
    if request.method == 'GET':
        return response_scrapping
    else:
        return 'chau xD'


if __name__ == '__main__':
    app.run(debug=True, port=5005)
