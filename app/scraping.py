import json
from selenium import webdriver
import time
import unicodedata


def obtener_cotizacion():
    json_ = '{}'
    json_response = json.loads(json_)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_path = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(chrome_path, options=chrome_options)
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    page = driver.get('https://www.brou.com.uy/cotizaciones')
    time.sleep(3)

    cant_monedas = len(driver.find_elements_by_xpath(
        '//*[@id="p_p_id_cotizacionfull_WAR_broutmfportlet_INSTANCE_otHfewh1klyS_"]/div/div/div/table/tbody/tr'))
    print(cant_monedas)

    for index in range(1, int(cant_monedas)+1):
        print(index)

        conjunto_de_datos = driver.find_element_by_xpath(
            f'//*[@id="p_p_id_cotizacionfull_WAR_broutmfportlet_INSTANCE_otHfewh1klyS_"]/div/div/div/table/tbody/tr[{str(index)}]').text
        arreglo_de_datos = conjunto_de_datos.split('\n')

        moneda = arreglo_de_datos[0]
        moneda = unicodedata.normalize("NFD", str(moneda))
        moneda = moneda.encode("utf8").decode("ascii", "ignore")

        compra = arreglo_de_datos[1].strip('   ')
        venta = arreglo_de_datos[2]

        json_response[moneda] = {
            'Compra': compra,
            'Venta': venta
        }

    return json_response
