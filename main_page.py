from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BasePage
from config import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    ACTIONS = (By.XPATH, "//a[@href = '/highlight/globalpromo/' and @class = 'a4 c0v']")
    BRENDS = (By.XPATH, "//a[@href = '/brand/' and @class = 'a4 c0v']")
    BUTTON_SELECT_CITY = (By.XPATH, '//span[@class = "ui-b5 ui-d8" and @style = "border-radius:8px;"]')
    CART = (By.XPATH, "//a[@href = '/cart']")
    CATALOG = (By.CSS_SELECTOR, "div[data-widget ='catalogMenu'] div button")
    CHAPTER_OF_CLOTHES_AND_SHOES = (By.XPATH, "//a[@class = 'nav-main-title' and contains (text(), 'Женщинам')]")
    CLOTHES_AND_SHOES = (By.XPATH, "//a[@href = '/category/zhenskaya-odezhda-7501/' and contains (text(), 'Одежда и обувь')]")
    COMMERCE = (By.XPATH, '//div[@class="a7ad" and @data-widget="advBanner"]')
    DROP_DOWN_ELEMENT = (By.XPATH, "//span[@class = 'cs4' and contains (text(), 'Электроника')]")
    ELECTRONICA_MAIN = (By.XPATH, "//a[@href = '/category/elektronika-15500/' and contains (text(), 'Электроника')]")
    ELECTRONICA_SUB = (By.XPATH, "//a[@class = 'a3p5 g5s4 g5s6 g5t' and @href = '/category/elektronika-15500/']")
    ELEM_OF_WINDOW_OZON_TRAVEL = (By.XPATH, "//h1[@class = 'ba1t' and contains (text(), 'Поиск дешёвых авиабилетов')]")
    ENTRANCE = (By.XPATH, "//*[@id = 'stickyHeader']/div[4]/div[1]")
    ENTRANCE_WINDOW = (By.XPATH, "//div[@class = 'w0ba' and @data-widget = 'ozonIdIframe']")
    EVERYWHERE_LIST = (By.XPATH, '//*[@id = "stickyHeader"]/div[3]/div/form/div[1]')
    FAVORITES = (By.XPATH, "//a[@href = '/my/favorites']")
    HEAD_OF_PAGE_BRENDS = (By.XPATH, "//h1[@class = 'zj2 tsHeadXL' and contains (text(), 'Все бренды')]")
    HEAD_OF_PAGE_ELECTRONICA_MAIN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    HEAD_OF_PAGE_ELECTRONICA_SUB = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    HEAD_OF_PAGE_FAVORITES = (By.XPATH, "//div[@class = 'a4' and contains (text(), 'Товары и списки')]")
    HEAD_OF_PAGE_HOUSE_AND_GARDEN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Дом и сад')]")
    HEAD_OF_PAGE_KIDS_GOODS = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Детские товары')]")
    HEAD_OF_PAGE_EXPRS = (By.XPATH, "//span[@class = 'aaj' and contains (text(), 'Товары с экспресс-доставкой')]")
    HEAD_OF_PAGE_SERTIFICATE = (By.XPATH, "//h1[@class = 'z5m' and contains (text(), 'Электронный подарочный сертификат Миллион подарков (3000) ozon')]")
    HEAD_OF_WINDOW_SELECT_CITY = (By.XPATH, '//span[@class = "v2d v5d tsBodyL p3"]')
    HOUSE_AND_GARDEN = (By.XPATH, "//a[@href = '/category/dom-i-sad-14500/' and contains (text(), 'Дом и сад')]")
    INPUT_FIELD_CITY = (By.XPATH, "//input[@class = 'ui-g ui-g2' and @type = 'text']")
    INSTALLEMENT = (By.XPATH, "//a[@href = '/section/limit/' and @class = 'a4 c0v']")
    IN_WINDOW_ENTRANCE = (By.XPATH, "//div[@class = 'w5ab' and @xmlns = 'http://www.w3.org/2000/svg']")
    KIDS_GOODS = (By.XPATH, "//a[@href = '/category/detskie-tovary-7000/' and contains (text(), 'Детские товары')]")
    LIST_EVERYWHERE = (By.XPATH, '//div[@class = "ha5a" and @data-widget = "searchContextPopup"]')
    LIST_OF_SUITABLE_CITIES = (By.XPATH, "//ul[@class = 'a3i7']")
    LOGIN_BUTTOM = (By.XPATH, '//*[@id = "avt-gtm-script"]')
    MAIN_LOGO = (By.CSS_SELECTOR, "#stickyHeader div")
    ORDERS = (By.CSS_SELECTOR, "div[data-widget = 'orderInfo']")
    ORDERS_WINDOW = (By.XPATH, "//div[@class = 'ye8' and contains (text(), 'Вы не авторизованы')]")
    OZON_BANK = (By.XPATH, "//a[@href = 'https://finance.ozon.ru/' and @class = 'a4 c0v']")
    OZON_TRAVEL = (By.XPATH, "//a[@href = 'https://www.ozon.ru/travel/?perehod=ozon_menu_header' and @class = 'a4 c0v']")
    POPUP_WINDOW_ENTRANCE = (By.XPATH, "//div[@class = 'ui-m2']")
    Premium = (By.XPATH, "//a[@href = '/highlight/premium/' and @class = 'a4 c0v']")
    REFERALS = (By.XPATH, "//a[@href = 'https://www.ozon.ru/b2bref' and @class = 'a4 c0v']")
    SEARCH_WHERE = (By.CSS_SELECTOR, "div[data-widget = 'searchBarDesktop'] form div span")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder = 'Искать на Ozon']")
    EXPRS = (By.XPATH, "//a[@href = '/highlight/express/' and @class = 'a4 c0v']")
    SERTIFICATE = (By.XPATH, '//a[@href = "/context/detail/id/135382627/?perehod=menu" and @class = "a4 c0v"]')
    SUBMIT_SEARCH = (By.XPATH, "//button[@class = 'jaa0']")
    PROMO = (By.XPATH, '//input[@type="text" and @class="ui-g4 ui-g6"]')
    PROMO_PAGE = (By.XPATH, '//div[@class="ye8" and contains (text(), "Вы не авторизованы")]')
    PROMO_BUTTOM = (By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[2]/button')
    BUTTON_THING = (By.XPATH, '//*[@id="layoutPage"]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]')
    IN_BUSKET_THING = (By.XPATH, '//*[@id="stickyHeader"]/div[4]/a[2]/span[1]')
    FOOTER = (By.XPATH, '//footer[@class="ct6" and data-widget="footer"]')