import requests
from bs4 import BeautifulSoup

url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
page = requests.get(url) # Выполняет GET-запрос к веб-странице и возвращает ответ сервера, который сохраняется в переменной
print(page.status_code) # Выводит HTTP-статус код ответа сервера на консоль.

soup = BeautifulSoup(page.text, 'html.parser') # Создает объект класса BeautifulSoup,# который используется для парсинга содержимого страницы
departments = soup.find('div', class_='main__content').findAll('a') # Находит все ссылки на странице

file = open('departments.txt', 'w')
i = 1
for item in departments: #  Начинает цикл, который перебирает все ссылки, сохраненные в переменной departments.
    file.write(str(i) + '. ' + item.text + '\n')
    i += 1
