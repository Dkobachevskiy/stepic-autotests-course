import time, math, pytest
from selenium import webdriver

bot_message = ''

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print(bot_message)
    browser.quit()

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])
def test_try_find_message(browser, link):
    browser.get(link)
    area = browser.find_element_by_css_selector('textarea')
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))
    button = browser.find_element_by_class_name('submit-submission')
    button.click()
    message = browser.find_element_by_class_name('smart-hints__hint')
    global bot_message
    if message.text != 'Correct!':
        bot_message += str(message.text)
    assert message.text == 'Correct!', f'получено в ответ сообщение {message.text}, должно быть Correct!'
