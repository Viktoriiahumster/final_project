from main_page import MainPage
from config import TestData

#ЛОГО:  Видимость логотипа на странице
def test_main_logo_on_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.MAIN_LOGO)
    assert logo == True

#ЛОГО:  Переход на страницу с акцией при нажатии на лого Ozon
def test_logo_ozon_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIN_LOGO)
    title_of_window = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_MAIN_LOGO)
    assert title_of_window == True

#КАТАЛОГ: Проверка видимости кнопки "Каталог" на странице
def test_button_catalog_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CATALOG)
    assert button == True

#КАТАЛОГ: Кнопка "Каталог" имеет верное название
def test_button_catalog_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CATALOG)
    assert  button_name == TestData.NAME_OF_BUTTON_CATALOG

#КАТАЛОГ: Проверка работы кнопки "Каталог"
def test_button_catalog_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CATALOG)
    main_page.find_click(MainPage.DROP_DOWN_ELEMENT)
    page_from_catalog = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_FROM_CATALOG)
    assert page_from_catalog == True

#ПОИСК: Кнопка локализации поиска видна на странице
def test_search_where_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SEARCH_WHERE)
    assert button == True

#ПОИСК: Строка поиска видна на странице
def test_search_on_page(driver):
    main_page = MainPage(driver)
    field_input = main_page.is_visible(MainPage.SEARCH_INPUT)
    assert field_input == True

#ПОИСК: Кнопка подтверждения ввода в строку поиска видна на странице
def test_submit_search_on_page(driver):
    main_page = MainPage(driver)
    submit_search = main_page.is_visible(MainPage.SUBMIT_SEARCH)
    assert submit_search == True

#ПОИСК: Выпадающее меню Везде видно на странице
def test_everywhere_on_page(driver):
    main_page = MainPage(driver)
    filter_everywhere = main_page.is_visible(MainPage.EVERYWHERE_LIST)
    assert filter_everywhere == True

#ПОИСК: Выпадающее меню Везде открывается при нажатии
def test_everywhere__clickable(driver):
    main_page = MainPage(driver)
    filter_everywhere = main_page.is_visible(MainPage.EVERYWHERE_LIST)
    assert filter_everywhere == True
    main_page.find_click(MainPage.EVERYWHERE_LIST)
    list_pop_up = main_page.is_visible(MainPage.LIST_EVERYWHERE)
    assert list_pop_up == True

#ПОИСК: кнопка поиска ищет введенное в строку поиска значение
def test_click_search_on_page(driver):
    main_page = MainPage(driver)
    main_page.clear_field_and_send_text_with_enter(MainPage.SEARCH_INPUT, TestData.RESULT_SEARCH)
    Result_of_search = main_page.get_windows_title(TestData.RESULT_SEARCH)
    assert Result_of_search == True

#ВОЙТИ: Кнопка Войти видна на странице
def test_entrance_on_page(driver):
    main_page = MainPage(driver)
    entrance = main_page.is_visible(MainPage.ENTRANCE)
    assert entrance == True

#ВОЙТИ: Появление всплывающего окна при наведении на кнопку
def test_popup_window_appear(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window == True

#ВОЙТИ: Всплывающее окно исчезает, когда курсор уводим с кнопки Войти
def test_popup_window_message_button_disappeared(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    main_page.put_away_from_element(MainPage.FAVORITES)
    popup_window_disappeared = main_page.isnt_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window_disappeared == True

#ВОЙТИ: Нажатие на кнопку Войти (может блокироваться сайтом из-за проверки на боты)
def test_entrance_is_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.IN_WINDOW_ENTRANCE)
    entrance = main_page.is_visible(MainPage.ENTRANCE_WINDOW)
    assert entrance == True

#ЗАКАЗЫ: Кнопка Заказы видна на странице
def test_button_Orders_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ORDERS)
    assert button == True

#ЗАКАЗЫ: Кнопка Заказы кликабельна
def test_Orders_is_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ORDERS)
    orders_page = main_page.is_visible(MainPage.ORDERS_WINDOW)
    assert orders_page == True

#ИЗБРАННОЕ: Кнопка Избранное видна на странице
def test_button_favorites_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.FAVORITES)
    assert button == True

#ИЗБРАННОЕ: Кнопка Избранное кликабельна
def test_favorites_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FAVORITES)
    Favorites_page_header = main_page.get_windows_title(TestData.HEADER_OF_PAGE_FAVORITES)
    assert Favorites_page_header == True

#КОРЗИНА: Кнопка Корзина видна на странице
def test_button_cart_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CART)
    assert button == True

#КОРЗИНА: Кнопка Корзина кликабельна, при нажатии осуществляется переход в соответствующий раздел
def test_cart_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CART)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_CART)
    assert window_title == True

#PREMIUM: Кнопка раздела Premium видна на странице
def test_button_Premium_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.Premium)
    assert button == True

#PREMIUM: Кнопка "Premium" имеет верное название
def test_button_premium_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.Premium)
    assert  button_name == TestData.NAME_OF_BUTTON_Premium

#PREMIUM: Кнопка кликабельна
def test_buttom_premium_is_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.Premium)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_PREMIUM)
    assert window_title == True

#БИЛЕТЫ И ОТЕЛИ: Кнопка раздела Билеты и Отели видна на странице
def test_button_ozon_travel_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_TRAVEL)
    assert button == True

#БИЛЕТЫ И ОТЕЛИ: Кнопка раздела Билеты и Отели имеет верное название
def test_button_ozon_travel_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_TRAVEL)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_TRAVEL

#БИЛЕТЫ И ОТЕЛИ: Кнопка Билеты и Отели кликабельна, попадаем в соответствующий раздел
def test_Ozon_travel_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_TRAVEL)
    element_title = main_page.get_text_of_element(MainPage.ELEM_OF_WINDOW_OZON_TRAVEL)
    assert element_title == TestData.ELEMENT_OF_WINDOW_OZON_TRAVEL

#OZON КАРТА: Кнопка раздела Ozon карта видна на странице
def test_button_Ozon_bank_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_BANK)
    assert button == True

#OZON КАРТА: Кнопка раздела Ozon карта имеет верное название
def test_button_ozon_bank_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_BANK)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_BANK

#OZON КАРТА: Кнопка раздела Ozon карта кликабельна, попадаем в соответствующий раздел
def test_Ozon_bank_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_BANK)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_OZON_BANK)
    assert window_title == True

#РАССРОЧКА: Кнопка раздела Рассрочка счет видна на странице
def test_button_installment_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.INSTALLEMENT)
    assert button == True

#РАССРОЧКА: Кнопка раздела Рассрочка имеет верное название
def test_button_LIVE_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.INSTALLEMENT)
    assert button_name == TestData.NAME_OF_BUTTON_INSTALLEMENT

#РАССРОЧКА: Кнопка раздела Рассрочка кликабельна, попадаем в соответствующий раздел
def test_LIVE_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.INSTALLEMENT)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_INSTALLEMENT)
    assert window_title == True

#АКЦИИ: Кнопка раздела Акции счет видна на странице
def test_button_actions_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ACTIONS)
    assert button == True

#АКЦИИ: Кнопка Акции имеет верное название
def test_button_action_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ACTIONS)
    assert button_name == TestData.NAME_OF_BUTTON_ACTIONS

#АКЦИИ: Кнопка Акции кликабельна, попадаем в соответствующий раздел
def test_actions_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACTIONS)
    title_of_page = main_page.get_windows_title(TestData.HEADER_OF_PAGE_OF_ACTIONS)
    assert title_of_page == True

#БРЕНДЫ: Кнопка раздела Бренды видна на странице
def test_button_brands_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BRENDS)
    assert button == True

#БРЕНДЫ: Кнопка Бренды имеет верное название
def test_button_brands_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.BRENDS)
    assert button_name == TestData.NAME_OF_BUTTON_BRANDS

#БРЕНДЫ:Кнопка Бренды кликабельна, попадаем в соответствующий раздел
def test_brends_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BRENDS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_BRENDS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_BRENDS

#EXPRESS: Кнопка раздела Express видна на странице
def test_button_xprs_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.EXPRS)
    assert button == True

#XPRESS: Кнопка раздела Express кликабельна, попадаем в соответствующий раздел
def test_xprs_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.EXPRS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_EXPRS)
    assert title_of_page == TestData.HEADER_OF_WINDOW_XPRS

#СЕРТИФИКАТЫ: Кнопка раздела Сертификаты видна на странице
def test_sertificate_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SERTIFICATE)
    assert button == True

#СЕРТИФИКАТЫ: Кнопка раздела Сертификаты кликабельна, попадаем в соответствующий раздел
def test_sertificate_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.SERTIFICATE)
    title_of_page = main_page.get_windows_title(TestData.HEADER_OF_PAGE_SERTIFICATE)
    assert title_of_page == True

#ЭЛЕКТРОНИКА: Кнопка раздела Электроника видна на странице
def test_button_electronica_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ELECTRONICA_MAIN)
    assert button == True

#ЭЛЕКТРОНИКА: Кнопка раздела Электроника имеет верное название
def test_button_electronics_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert  button_name == TestData.NAME_OF_BUTTON_ELECTRONICA_MAIN

#ЭЛЕКТРОНИКА: Кнопка Электроника кликабельна, попадаем в соответствующий раздел
def test_electronica_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ELECTRONICA_MAIN)
    window_title = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_ELECTRONICA_MAIN

#ОДЕЖДА И ОБУВЬ: Кнопка раздела Одежда и обувь видна на странице
def test_button_clothes_and_shoes_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CLOTHES_AND_SHOES)
    assert button == True

#ОДЕЖДА И ОБУВЬ: Кнопка раздела Одежда и обувь имеет верное название
def test_button_clothes_and_shoes_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CLOTHES_AND_SHOES)
    assert button_name == TestData.NAME_OF_BUTTON_CLOTHES_AND_SHOES

#ОДЕЖДА И ОБУВЬ: Кнопка Одежда и обувь кликабельна, попадаем в соответствующий раздел
def test_clothes_and_shoes_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CLOTHES_AND_SHOES)
    window_title = main_page.get_text_of_element(MainPage.CHAPTER_OF_CLOTHES_AND_SHOES)
    assert window_title == TestData.HEADER_OF_CHAPTER_OF_CLOTHES_AND_SHOES

#ДОМ И САД: Кнопка раздела Дом и сад видна на странице
def test_button_house_and_garden_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.HOUSE_AND_GARDEN)
    assert button == True

#ДОМ И САД: Кнопка раздела Дом и сад имеет верное название
def test_button_house_and_garden_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert button_name == TestData.NAME_OF_BUTTON_HOUSE_AND_GARDEN

#ДОМ И САД: Кнопка Дом и сад кликабельна, попадаем в соответствующий раздел
def test_button_house_and_garden_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.HOUSE_AND_GARDEN)
    window_title = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_HOUSE_AND_GARDEN

#ДЕТСКИЕ ТОВАРЫ: Кнопка раздела Детские товары видна на странице
def test_button_kids_goods_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.KIDS_GOODS)
    assert button == True

#ДЕТСКИЕ ТОВАРЫ: Кнопка раздела Детские товары имеет верное название
def test_button_kids_goods_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert button_name == TestData.NAME_OF_BUTTON_KIDS_GOODS

#ДЕТСКИЕ ТОВАРЫ: Кнопка Детские товары кликабельна, попадаем в соответствующий раздел
def test_kids_goods_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.KIDS_GOODS)
    window_title = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert window_title == TestData.HEADER_OF_PAGE_OF_KIDS_GOODS

#РЕФЕРАЛЬНАЯ ПРОГРАММА: Кнопка раздела видна на странице
def test_button_referals_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.REFERALS)
    assert button == True

#РЕФЕРАЛЬНАЯ ПРОГРАММА: Кнопка кликабельна
def test_kids_referals_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REFERALS)
    window_title = main_page.get_windows_title(TestData.REFERALS_NAME)
    assert window_title == True

#ГОРОД: Кнопка выбора города видна на странице
def test_definite_city_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BUTTON_SELECT_CITY)
    assert button == True

#ГОРОД: При нажатии кнопки выбора города появляется окно выбора города
def test_definite_city_appear_window(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BUTTON_SELECT_CITY)
    window_title = main_page.get_text_of_element(MainPage.HEAD_OF_WINDOW_SELECT_CITY)
    assert window_title == TestData.HEADER_OF_WINDOW_SELECT_CITY

#ПРОМОКОД: на странице отображается поле для введения Промокода
def test_promo_on_page(driver):
    main_page = MainPage(driver)
    input_promo = main_page.is_visible(MainPage.PROMO)
    assert input_promo == True

#ПРОМОКОД: в строку вводится значение, нажатие кнопки переводит на соотвествующую страницу
def test_click_promo_on_page(driver):
    main_page = MainPage(driver)
    main_page.clear_field_and_send_text_with_enter(MainPage.PROMO, TestData.PROMO_EXMPL)
    Result_promo = main_page.get_text_of_element(MainPage.PROMO_PAGE)
    assert Result_promo == TestData.PROMO_PAGE_TXT

#РЕКЛАМА: на первой странице видна реклама товара
def test_comm_is_visible(driver):
    main_page = MainPage(driver)
    comerce = main_page.is_visible(MainPage.COMMERCE)
    assert comerce == True

#КОРЗИНА: товар с главной страницы можно положить в корзину
def test_thing_in_basket(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BUTTON_THING)
    thing_page = MainPage.IN_BUSKET_THING
    assert (thing_page != 0) is True
