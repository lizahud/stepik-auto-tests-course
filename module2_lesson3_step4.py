# # задание:
# # Открыть страницу http://suninjuly.github.io/alert_accept.html
# # Нажать на кнопку
# # Принять confirm
# # На новой странице решить капчу для роботов, чтобы получить число с ответом
# from selenium import webdriver
# import time
# import math
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/alert_accept.html")
#
#     browser.find_element_by_css_selector("button.btn").click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
# #действия на второй странице:
#
#     input = browser.find_element_by_css_selector("#input_value").text
#     itogo = calc(input)
#
#     input1 = browser.find_element_by_css_selector("#answer").send_keys(itogo)
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 10 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла



#крутой код чувака со степика
# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import os
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_class_name('btn-primary').click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    answer = alert_text[-1]

    browser.get('https://stepik.org/catalog?auth=login&language=ru')
    time.sleep(5)

    browser.find_element_by_id('id_login_email').send_keys('elizavetakhudainatova@yandex.ru')# здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('Anzorro8$')# здесь вводится пароль

    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(3)

    answer_input = browser.find_element_by_css_selector("#ember482")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    #button1 = browser.find_element_by_class_name('submit-submission').click()
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #time.sleep(1)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()