from bs4 import BeautifulSoup
import requests

import settings

NAME_CLASS = "d_mx d_mE"
TEMPERATURE_CLASS = "d_mz"
CONTAINER_CLASS = "d_mC"


class Weather:
    @staticmethod
    def _parse_result(html):
        soup = BeautifulSoup(html, "html.parser")
        items = soup.findAll("div", {"class": CONTAINER_CLASS})

        data = []
        for item in items:
            name = item.find("span", {"class": NAME_CLASS}).text
            temperature = item.find("span", {"class": TEMPERATURE_CLASS}).text
            svg = item.find("svg", {"class": "atm-icon d_mA atm-icon d_mA"})

            data.append({
                'name': name,
                'temperature': temperature,
                'svg': svg
            })

        return {
            'data': data
        }

    def get(self):
        response = requests.get(settings.FEED_URL)
        if response.status_code != 200:
            return {
                'error': 'Oops! Some error from feed source'
            }

        # Parsing process start
        return self._parse_result(response.content)
