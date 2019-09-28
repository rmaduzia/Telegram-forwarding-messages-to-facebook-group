import telebot  # importing pyTelegramBotAPI library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler


def facebook_post(msgg,address_email ,password , url):
    browser = webdriver.Firefox()
    browser.get(url)
    email = browser.find_element_by_id("m_login_email")
    email.send_keys(address_email)
    pwd = browser.find_element_by_name("pass")
    pwd.send_keys(password)
    pwd.send_keys(Keys.RETURN)
    msg = browser.find_element_by_id("u_0_0")
    msg.send_keys(msgg)
    browser.find_element_by_name("view_post").click()
    browser.quit()


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    msg_send = update.message.text
    facebook_post(msg_send, address_email, password, url_facebook_group)


if __name__ == '__main__':
    updater = Updater(token='')  # telegram bot api token
    address_email = ""  # email to login facebook account
    password = ""  # password to login facebook account
    url_facebook_group = ""

    dispatcher = updater.dispatcher
    start_handler = MessageHandler(Filters.text, start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()