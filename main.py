import requests
from bs4 import BeautifulSoup
import csv

# url = "https://health-diet.ru/base_of_food/food_24507/"
# response = requests.get(url)
# # print(response)
# # print(dir(response))
# html_txt = response.text
# print(html_txt)
# # Сохраняем код
# # создать и открыть файл для записи кода HTML
# with open("index.html", "w") as file:
#     file.write(html_txt)

with open("index.html") as file:
    html_txt = file.read()
print(html_txt)
soup = BeautifulSoup(html_txt, "lxml")
