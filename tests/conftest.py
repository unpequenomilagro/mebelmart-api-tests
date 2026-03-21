import pytest
from loguru import logger
import allure
from utils.allure_helper import AllureHelper
import time

@pytest.fixture(scope="function")
def api_client():
    """Фикстура для API клиента"""
    logger.info("Инициализация API клиента")
    
    # Импортируем здесь, чтобы избежать циклических импортов
    from api.users_api import UsersAPI
    from api.posts_api import PostsAPI
    from api.todos_api import TodosAPI
    from api.comments_api import CommentsAPI
    
    class APIClient:
        def __init__(self):
            self.users = UsersAPI()
            self.posts = PostsAPI()
            self.todos = TodosAPI()
            self.comments = CommentsAPI()
    
    yield APIClient()
    
    logger.info("API клиент закрыт")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для получения результата теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    
    # Если тест упал, делаем скриншот логов
    if rep.when == "call" and rep.failed:
        logger.error(f"Тест {item.name} упал")