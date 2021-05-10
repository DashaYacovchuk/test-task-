# Daria Yakovchuk test task

import requests  # Module to process the URL
from bs4 import BeautifulSoup  # Module for working with HTML
import time  # Module to stop the program for a while


class Currency:
    # Link to the page that check dollar exchange rate
    Dollar_UA = 'https://www.google.com/search?q=usd+to+uah&sxsrf=ALeKk02xU6hF1Z-Npsd0b5dwVzrbFxDFbQ%3A1620635317036&ei=te6YYLraAcOGwPAPp5SvqAE&oq=USD+to+UAH&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQywEyBQgAEMsBMgIIADIFCAAQywEyBQgAEMsBMgIIADICCAAyBQgAEMsBMgUIABDLATIFCAAQywE6BwgjELADECc6BwgAEEcQsANQzrIDWM6yA2DgvgNoAnACeACAAaMBiAHwAZIBAzEuMZgBAKABAqABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz'
    # Headers to be passed along with the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    current_dollar = 0

    def init(self):
        # Setting the dollar exchange rate when creating an object
        self.current_dollar = float(self.get_dollar_rate().replace(",", "."))

    # Method for obtaining the currency rate
    def get_dollar_rate(self):
        full_page = requests.get(self.Dollar_UA, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    # Checking dollar exchange rate change
    def check_dollar_rate(self):
        dollar = float(self.get_dollar_rate().replace(",", "."))
        if dollar != self.current_dollar:
            body = 'Dollar exchange rate has been changed!'+'\n'+" 1 dollar = " + str(dollar)
            self.telegram_bot_sendtext(body)
        print("Сейчас курс: 1 доллар = " + str(dollar))
        self.current_dollar = dollar
        time.sleep(60)  # Sleep program for 1 minute
        self.check_dollar_rate()

    # send message to telegram channel called currency rate https://t.me/currancy_test_task
    def telegram_bot_sendtext(self, bot_message):
        bot_token = ''   # your bot token
        bot_chatID = ''  # your bot chat id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

# Object creation and method call
currency = Currency()
currency.check_dollar_rate()
