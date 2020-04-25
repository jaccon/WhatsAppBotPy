# -*- coding: utf-8 -*-

from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.message = "this is a test"
        self.senders = ["#BrazilianSiliconValley"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver', chrome_options=options)

    def sendMessages(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for sender in self.senders:
            senderField = self.driver.find_element_by_xpath(
                f"//span[@title='{sender}']")
            time.sleep(3)
            senderField.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.sendMessages()
