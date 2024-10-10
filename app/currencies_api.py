import requests

# Ваш API-ключ от Open Exchange Rates (замените на ваш ключ)
API_KEY = "8ad772efe8d44dd6961a3128110e169c"

def get_exchange_rate(base_currency, target_currency):
    # URL для получения актуальных курсов от Open Exchange Rates
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base=USD"
    
    try:
        # Выполняем запрос к API
        response = requests.get(url)
        
        # Логируем статус код и ответ от API для диагностики
        print(f"Статус код: {response.status_code}")
        print(f"Ответ от API: {response.text}")

        # Преобразуем ответ в JSON
        data = response.json()
        
        if response.status_code == 200:
            # Проверяем, есть ли курсы валют в ответе
            if base_currency == "USD":
                if "rates" in data:
                    rate = data["rates"].get(target_currency)
                    if rate:
                        return rate
                    else:
                        return f"Не удалось найти курс для валюты {target_currency}"
                else:
                    return "Ошибка: данные о курсах не найдены в ответе API."
            else:
                if "rates" in data:
                    rateUSD = data["rates"].get(base_currency)
                    rate = data["rates"].get(target_currency) / rateUSD
                    if rate:
                        return rate
                    else:
                        return f"Не удалось найти курс для валюты {target_currency}"
                else:
                    return "Ошибка: данные о курсах не найдены в ответе API."
        else:
            return f"Ошибка: {data.get('error', 'Неизвестная ошибка')}"

    except Exception as e:
        return f"Ошибка при попытке получить данные: {str(e)}"
        

