import allure
import pytest
from config.config import Config
from loguru import logger

@allure.feature("Comments API")
class TestCommentsAPI:
    
    @allure.title("GET /comments - получение списка комментариев")
    def test_get_all_comments(self, api_client):
        # Получаем только первые 50 комментариев для ускорения
        response = api_client.comments.get_all(params={"_limit": 50})
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        logger.info(f"Получено комментариев: {len(data)}")
        assert len(data) > 0, "Нет комментариев"
    
    @allure.title("GET /comments/:id - получение комментария по ID")
    def test_get_comment_by_id(self, api_client):
        response = api_client.comments.get_by_id(1)
        assert response.status_code == 200
        assert response.json()['id'] == 1
    
    @allure.title("GET /comments/:id - комментарий не найден (404)")
    def test_get_comment_not_found(self, api_client):
        response = api_client.comments.get_by_id(999999)
        assert response.status_code == 404
    
    @allure.title("POST /comments - создание комментария")
    def test_create_comment(self, api_client):
        comment_data = Config.TEST_COMMENT.copy()
        response = api_client.comments.create(comment_data)
        assert response.status_code == 201
        data = response.json()
        assert 'id' in data
        assert data['name'] == comment_data['name']
        assert data['body'] == comment_data['body']
    
    @allure.title("DELETE /comments/:id - удаление комментария")
    def test_delete_comment(self, api_client):
        comment_data = Config.TEST_COMMENT.copy()
        create_resp = api_client.comments.create(comment_data)
        comment_id = create_resp.json()['id']
        
        response = api_client.comments.delete(comment_id)
        assert response.status_code in [200, 204]
        
        get_resp = api_client.comments.get_by_id(comment_id)
        assert get_resp.status_code == 404