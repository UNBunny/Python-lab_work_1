import requests
from bs4 import BeautifulSoup
def parser(url):
    page = requests.get(url) # Выполняет GET-запрос к веб-странице и возвращает ответ сервера, который сохраняется в переменной
    print(page.status_code) # Выводит HTTP-статус код ответа сервера на консоль.

    soup = BeautifulSoup(page.text, 'html.parser') # Создает объект класса BeautifulSoup,который используется для парсинга содержимого страницы
    departments = soup.find('div', class_='main__content').findAll('a') # Находит все ссылки на странице
    file = open('departments.txt', 'w')
    for item in departments: #  Начинает цикл, который перебирает все ссылки, сохраненные в переменной departments.
        file.write(item.text.strip() + '\n')

if __name__ == "__main__":
    URL = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    parser(URL)
