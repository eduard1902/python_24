import os
from PIL import Image
# Удаление метаданных файла изображения

url = "./example.jpg"
def clear_all_metadata(imgname):
    # Открываем файл изображения
    img = Image.open(imgname)
    # Читаем данные изображения, исключая метаданные
    data = list(img.getdata())
    # Создаём новое изображение с теми же режимом и размером, но без метаданных
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    # Сохраняем новое изображение поверх исходного файла, эффективно удаляя метаданные
    img_without_metadata.save('./newfile.jpg')
    # Получаем размер файлов в байтах и преобразуем килобайты
    image_size = os.path.getsize('./example.jpg')
    new_image_size = os.path.getsize('./newfile.jpg')
    value = ((image_size - new_image_size) / 1000)
    print(f'Метаданные фотографии {imgname} удалены')
    print(f'Размер изображения уменьшился на {round(value, 1)} кБ')

clear_all_metadata(url)


# Получаем прогноз погоды на Python с помощью библиотеки Requests
import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Параметры запроса для Гулькевичи Краснодарского края
params = {
    "latitude": 45.3538300,  # широта Гулькевичи
    "longitude": 40.6946500,  # долгота Гулькевичи
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
    # минимальная и максимальная температура, сумма осадков
    "timezone": "Europe/Moscow"  # временная зона для Гулькевичи
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    # Поскольку индекс 0 представляет собой данные на текущий день, индекс 1 будет представлять данные на завтра
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]

    print(f"Прогноз погоды в Гулькевичи на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
else:
    print(f"Ошибка {response.status_code}: {response.text}")



# Чтение табличных данных и вывод суммы продаж
import pandas as pd

# Чтение данных из ODS
sales_data = pd.read_excel("output.ods", engine="odf")

# # Получение общей суммы продаж
total_sales = sales_data['Sales'].sum()
print(f"Общий объем продаж: {total_sales}")
#
# # Средняя сумма продаж по регионам
average_sales_by_region = sales_data.groupby(['Region']).agg('mean')
print(average_sales_by_region)

