import allure
import pytest
from config.config import Config

@allure.feature("Users API")
class TestUsersAPI:
    
    @allure.title("GET /users - получение всех пользователей")
    def test_get_all_users(self, api_client):
        response = api_client.users.get_all()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
    
    @allure.title("GET /users/:id - получение пользователя по ID")
    def test_get_user_by_id(self, api_client):
        response = api_client.users.get_by_id(1)
        assert response.status_code == 200
        assert response.json()['id'] == 1
    
    @allure.title("GET /users/:id - пользователь не найден (404)")
    def test_get_user_not_found(self, api_client):
        response = api_client.users.get_by_id(999999)
        assert response.status_code == 404
    
    @allure.title("POST /users - создание пользователя")
    def test_create_user(self, api_client):
        user_data = Config.TEST_USER.copy()
        response = api_client.users.create(user_data)
        assert response.status_code == 201
        data = response.json()
        assert 'id' in data
        assert data['name'] == user_data['name']
    
    @allure.title("PATCH /users/:id - обновление пользователя")
    def test_partial_update_user(self, api_client):
        user_data = Config.TEST_USER.copy()
        create_resp = api_client.users.create(user_data)
        user_id = create_resp.json()['id']
        
        response = api_client.users.partial_update(user_id, {"name": "Updated Name"})
        assert response.status_code == 200
        assert response.json()['name'] == "Updated Name"
    
    @allure.title("DELETE /users/:id - удаление пользователя")
    def test_delete_user(self, api_client):
        user_data = Config.TEST_USER.copy()
        create_resp = api_client.users.create(user_data)
        user_id = create_resp.json()['id']
        
        response = api_client.users.delete(user_id)
        assert response.status_code in [200, 204]
        
        get_resp = api_client.users.get_by_id(user_id)
        assert get_resp.status_code == 404