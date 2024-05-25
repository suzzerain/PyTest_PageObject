import pytest
from pages.web import HeroesPage
from selenium.webdriver import Chrome
# Реализация фикстуры
@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
#Функция по проверке осуществления перехода на страницу с вариантом
def test_heroes_page(browser):
    heroes_page = HeroesPage(browser)
    heroes_page.load()
    heroes_page.find_variant()
    # Реализация проверок с помощью PyTest
    assert heroes_page.heroes_elements_count() > 0
    assert heroes_page.iron_elements_count() > 0
    assert heroes_page.thor_elements_count() > 0
    assert heroes_page.blackwidow_elements_count() > 0
    assert heroes_page.heading_images_count() > 0
    assert heroes_page.title_elements_count() > 0
    assert heroes_page.superman_elements_count() > 0

