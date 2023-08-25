from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, selector):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(selector))
    element.click()

# Инициализация веб-драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Открытие страницы объявления
    driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

    # Клик по кнопке "Добавить в избранное"
    wait_and_click(driver, (By.CSS_SELECTOR, "div.style-header-add-favorite-M7nA2"))

    # Подтверждение добавления в избранное
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.desktop-p6xjn6")))
    print("Добавлено в избранное")

    # Переход в раздел "Избранное"
    wait_and_click(driver, (By.CSS_SELECTOR, "div.desktop-1rdftp2"))

    # Проверка, что объявление отображается в разделе "Избранное"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.item-snippet-root-d2wFO")))
    print("Объявление в избранном")

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # Закрытие веб-драйвера
    driver.quit()