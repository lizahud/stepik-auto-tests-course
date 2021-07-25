#Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = browser.get("http://suninjuly.github.io/redirect_accept.html")

    knopka = browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #first_window = browser.window_handles[0]

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()