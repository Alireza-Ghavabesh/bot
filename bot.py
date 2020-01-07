from selenium import webdriver
# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from telegram.ext import Updater , dispatcher,Filters , MessageHandler
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH") , chrome_options=chrome_options)


driver.get("https://www.google.com")

print(driver.page_source)
# def music_searcher(music_name):
#
#     driver.implicitly_wait(5)
#     wait = WebDriverWait(driver, 10)
#
#     driver.minimize_window()
#     # baz kardan link asli
#     driver.get("https://myfreemp3c.com/")
#     # peyda kardan makan baraye neveshtan esm ahng dar an
#     driver.find_element_by_xpath('//*[@id="query"]').send_keys(music_name)
#     # peyda kardan dokme SEARCH dar safe va click kardan bar roye an
#     driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/span/button').click()
#     # injaro bayad check konam alan yadam nmiay chekar kardam
#     element = wait.until(EC.element_to_be_clickable((By.XPATH , r'//*[@id="result"]/div[2]/li[1]/div/a[3]')))
#     element.click()
#
#     # tarif list baraye gharar dadan ahng ha da an
#     links_of_mp3 = []
#     # tarif list movaghat ke baad har 2 nam ro dron 1 khane az list asli gharar bedam
#     temp_names = []
#     # tarif list asli baraye gharar dadn nam ha be sorat ===>(( temp_names[0] - temp_names[1] )))
#     main_names = []
#     data = driver.page_source
#     soup = BeautifulSoup(data , 'html.parser')
#     for div in soup.findAll('div'):
#         for a in div.find_all('a' , {'class' : 'name' , 'title':'Download'}):
#             links_of_mp3.append(a['href'])
#     # bedast ovordan nam ha
#     for div in soup.findAll('div'):
#         for name in div.find_all('a' , {'id' : 'navi'}):
#             temp_names.append(name)
#     # gozashtan nam ha dar yek khat
#     i = 0
#     while i < len(temp_names)/2:
#         XnameX = "{} - {}".format(temp_names[i].text,temp_names[i+1].text)
#         main_names.append(XnameX)
#         i+=2
#     #gozashtan name va music dar yek list be esm MusicANDname
#     num = 0
#     MusicANDname = []
#     while num < len(main_names):
#         String_name_music = "{} : {}".format(main_names[num] , links_of_mp3[num])
#         MusicANDname.append(String_name_music)
#         num+=1
#     driver.quit()
#     return MusicANDname
#
#
#
#
#
#
#
# updater = Updater("1027586380:AAEs7H3KwQcvXbCgtsDL5Gk_4bGnPB49o6Q" , use_context=True)
#
#
#
# def start(update,context):
#     chat_id = update.message.chat_id
#     text = update.message.text
#     user_id = update.message.from_user.id
#     context.bot.sendMessage(chat_id=chat_id , text="Please wait...")
#     i = 0
#     links = music_searcher(text)
#     while i < 10:
#         context.bot.sendMessage(chat_id=chat_id,text=links[i])
#         i += 1
#
#
# music_handler = MessageHandler(Filters.text , start)
# updater.dispatcher.add_handler(music_handler)
# updater.start_polling()
# print("bot started...")

