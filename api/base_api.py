import requests
import allure
from loguru import logger
from config.config import Config
from utils.allure_helper import AllureHelper

class BaseAPI:
    """Базовый класс для работы с API"""
    
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.REQUEST_TIMEOUT
        # Отключаем проверку SSL для тестового API
        self.session = requests.Session()
        self.session.verify = False
        # Подавляем предупреждения о небезопасном соединении
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def _make_request(self, method: str, endpoint: str, **kwargs):
        """Выполнить HTTP запрос"""
        url = f"{self.base_url}{endpoint}"
        
        # Логируем запрос
        logger.info(f"Request: {method.upper()} {url}")
        
        # Добавляем таймаут по умолчанию
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout
        
        try:
            # Прикрепляем информацию о запросе к Allure
            AllureHelper.attach_request(method, url, kwargs.get('headers'), kwargs.get('json') or kwargs.get('data'))
            
            # Выполняем запрос через сессию с отключенной проверкой SSL
            response = self.session.request(method, url, **kwargs)
            
            # Логируем ответ
            logger.info(f"Response: {response.status_code}")
            
            # Прикрепляем информацию об ответе к Allure
            try:
                response_body = response.json() if response.text else None
            except:
                response_body = response.text
            
            AllureHelper.attach_response(response.status_code, response_body, dict(response.headers))
            
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        """GET запрос"""
        return self._make_request('GET', endpoint, params=params, headers=headers)
    
    def post(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        """POST запрос"""
        return self._make_request('POST', endpoint, data=data, json=json, headers=headers)
    
    def put(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        """PUT запрос"""
        return self._make_request('PUT', endpoint, data=data, json=json, headers=headers)
    
    def patch(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        """PATCH запрос"""
        return self._make_request('PATCH', endpoint, data=data, json=json, headers=headers)
    
    def delete(self, endpoint: str, headers: dict = None):
        """DELETE запрос"""
        return self._make_request('DELETE', endpoint, headers=headers)