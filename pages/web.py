from selenium.webdriver.common.by import By
class HeroesPage:
    URL = 'https://qa-test-selectors.netlify.app'
    VARIANT = 4
    HEADING = "Халк"
    TITLE_TEXT = "Капитан Америка"
    def __init__(self, browser):
        self.browser = browser
    def load(self):
        self.browser.get(self.URL)
    def find_variant(self):
    # Выбор кнопки с 20 вариантом, как 19 элемента из списка всехкнопок страницы
    # button = self.browser.find_elements(By.TAG_NAME,'button')[self.VARIANT-1]
    # Выбор кнопки с 20 вариантом, по XPATH
    # button = self.browser.find_element(By.XPATH, f'//button[@class="variant__btn"][text()="{self.VARIANT}"]')
    # Выбор кнопки с 20 вариантом, по CSS-селектору
        button = self.browser.find_element(By.CSS_SELECTOR, f'.variant__btn:nth-child({self.VARIANT})')
    # Нажатие на кнопку с вариантом
        button.click()

    def heroes_elements_count(self):

    # Поиск элементов с data-type="heroes"
        heroes_elements = self.browser.find_elements(By.XPATH, '//*[@data-type="heroes"]')
        return len(heroes_elements)

    def iron_elements_count(self):

    # Поиск элементов с id="iron"
        iron_elements = self.browser.find_elements(By.ID, 'iron')
        return len(iron_elements)

    def thor_elements_count(self):

        # Поиск элементов с class="thorOdinSon"
        thor_elements = self.browser.find_elements(By.CLASS_NAME, 'thorOdinSon')
        return len(thor_elements)
    def superman_elements_count(self):

        # Поиск элементов с img src='./assets/variants/4/superman.jpg'
        superman_elements = self.browser.find_elements(By.CSS_SELECTOR, "img.superMan[src*='./assets/variants/4/superman.jpg']")

        #Вариант поиска с помощью XPATH:
        #superman_elements = self.browser.find_elements(By.XPATH, "//img[@class='superMan' and contains (@src, './assets/variants/4/superman.jpg')]")

        return len(superman_elements)
    def blackwidow_elements_count(self):

        # Поиск элементов с name="black-widow"
        blackwidow_elements = self.browser.find_elements(By.NAME, 'black-widow')
        return len(blackwidow_elements)

    def heading_images_count(self):

        # Поиск изображений с heading="Халк"
        heading_images = self.browser.find_elements(By.XPATH,f'//img[@heading="{self.HEADING}"]')
        return len(heading_images)

    def title_elements_count(self):

        # Поиск элементов с name="Капитан Америка"
        title_elements = self.browser.find_elements(By.XPATH,f'//h1[text()="{self.TITLE_TEXT}"]')
        return len(title_elements)