import os
import requests
from dotenv import load_dotenv

# Вставьте API ключ напрямую или через .env файл
API_KEY = 'fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI='


# Функция для выполнения запроса к API Foursquare
def search_places(query, latitude, longitude, radius):
    url = 'https://api.foursquare.com/v3/places/search'
    headers = {
        'Authorization': API_KEY
    }
    params = {
        'query': query,
        'll': f'{latitude},{longitude}',
        'radius': radius,
        'limit': 10  # Максимальное количество результатов
    }

    response = requests.get(url, headers=headers, params=params)

    # Проверка статуса запроса
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении данных: {response.status_code}, {response.text}")
        return None


# Функция для обработки и вывода информации о заведениях
def print_places_info(places):
    if places and 'results' in places:
        for place in places['results']:
            name = place.get('name')
            location = place.get('location', {})
            address = location.get('formatted_address', 'Адрес не указан')
            rating = place.get('rating', 'Нет рейтинга')

            print(f"Название: {name}")
            print(f"Адрес: {address}")
            print(f"Рейтинг: {rating}\n")
    else:
        print("Заведения не найдены")


# Основная функция
def main():
    # Запрос данных у пользователя
    query = input("Введите категорию (например, кофейни, музеи, парки): ")
    latitude = input("Введите широту места поиска (например, 55.7558 для Москвы): ")
    longitude = input("Введите долготу места поиска (например, 37.6173 для Москвы): ")
    radius = input("Введите радиус поиска в метрах (например, 1000): ")

    # Выполнение поиска
    places = search_places(query, latitude, longitude, radius)

    # Вывод информации о заведениях
    print_places_info(places)


if __name__ == '__main__':
    main()
