from loader import config, logger
import requests
import datetime


class ApiParser:
    
    @staticmethod
    def parse(end_time):
        api_url = config.api.url
        params = {'client': config.api.client,
          'client_key': config.api.client_key,
          'start': (end_time - datetime.timedelta(minutes=config.api.interval)).strftime('%Y-%m-%d %H:%M:%S'),
          'end': end_time.strftime('%Y-%m-%d %H:%M:%S')}
        logger.info("Запрос данных с сервера")
        r = requests.get(api_url, params=params)
        
        if r.status_code != 200:
            logger.error(f"Ошибка доступа к серверу с кодом {r.status_code}")
            return dict()
        logger.info("Данные с сервера получены")
        return r.json()
