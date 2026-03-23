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
    
    def _make_request(self, method: str, endpoint: str, **kwargs):
        """Выполнить HTTP запрос"""
        url = f"{self.base_url}{endpoint}"
        
        # Формируем URL с параметрами для отображения в логах
        params = kwargs.get('params', {})
        param_str = f"?{params}" if params else ""
        logger.info(f"{method.upper()} {url}{param_str}")
        
        # Прикрепляем запрос к Allure
        AllureHelper.attach_request(method, url, kwargs.get('json'), params)
        
        response = requests.request(method, url, **kwargs)
        
        logger.info(f"Response: {response.status_code}")
        
        # Прикрепляем ответ к Allure
        try:
            response_body = response.json() if response.text else None
        except:
            response_body = response.text
        AllureHelper.attach_response(response.status_code, response_body)
        
        return response
    
    def get(self, endpoint: str, params: dict = None):
        return self._make_request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, json: dict = None):
        return self._make_request('POST', endpoint, json=json)
    
    def put(self, endpoint: str, json: dict = None):
        return self._make_request('PUT', endpoint, json=json)
    
    def patch(self, endpoint: str, json: dict = None):
        return self._make_request('PATCH', endpoint, json=json)
    
    def delete(self, endpoint: str):
        return self._make_request('DELETE', endpoint)