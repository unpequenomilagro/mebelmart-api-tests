import allure
import pytest
from config.config import Config

@allure.feature("Todos API")
class TestTodosAPI:
    
    @allure.title("GET /todos - получение всех задач")
    def test_get_all_todos(self, api_client):
        response = api_client.todos.get_all()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
    
    @allure.title("GET /todos/:id - получение задачи по ID")
    def test_get_todo_by_id(self, api_client):
        response = api_client.todos.get_by_id(1)
        assert response.status_code == 200
        assert response.json()['id'] == 1
    
    @allure.title("GET /todos/:id - задача не найдена (404)")
    def test_get_todo_not_found(self, api_client):
        response = api_client.todos.get_by_id(999999)
        assert response.status_code == 404
    
    @allure.title("POST /todos - создание задачи")
    def test_create_todo(self, api_client):
        todo_data = Config.TEST_TODO.copy()
        response = api_client.todos.create(todo_data)
        assert response.status_code == 201
        data = response.json()
        assert 'id' in data
        assert data['title'] == todo_data['title']
        assert data['completed'] == todo_data['completed']
    
    @allure.title("PATCH /todos/:id - обновление статуса задачи")
    def test_update_todo_status(self, api_client):
        todo_data = Config.TEST_TODO.copy()
        create_resp = api_client.todos.create(todo_data)
        todo_id = create_resp.json()['id']
        
        response = api_client.todos.update(todo_id, {"completed": True})
        assert response.status_code == 200
        assert response.json()['completed'] == True
    
    @allure.title("DELETE /todos/:id - удаление задачи")
    def test_delete_todo(self, api_client):
        todo_data = Config.TEST_TODO.copy()
        create_resp = api_client.todos.create(todo_data)
        todo_id = create_resp.json()['id']
        
        response = api_client.todos.delete(todo_id)
        assert response.status_code in [200, 204]
        
        get_resp = api_client.todos.get_by_id(todo_id)
        assert get_resp.status_code == 404