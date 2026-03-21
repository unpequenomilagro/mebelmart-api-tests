import allure
import pytest
from config.config import Config

@allure.feature("Todos API")
@allure.story("CRUD операции с задачами")
class TestTodosAPI:
    
    @allure.title("GET /todos - получение списка задач")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_todos(self, api_client):
        response = api_client.todos.get_all_todos()
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    @allure.title("GET /todos/:id - получение задачи по ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_todo_by_id(self, api_client):
        todos = api_client.todos.get_all_todos().json()
        if todos:
            todo_id = todos[0].get('id', 1)
        else:
            todo_id = 1
        
        response = api_client.todos.get_todo_by_id(todo_id)
        
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert 'id' in response.json()
    
    @allure.title("POST /todos - создание новой задачи")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_todo(self, api_client):
        todo_data = Config.TEST_TODO.copy()
        
        response = api_client.todos.create_todo(todo_data)
        
        assert response.status_code in [200, 201]
        data = response.json()
        assert 'id' in data
        assert data['title'] == todo_data['title']
    
    @allure.title("GET /todos?completed=true - фильтрация по статусу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_todos_by_completed_status(self, api_client):
        response = api_client.todos.get_todos_by_completed_status(True)
        
        assert response.status_code == 200
        todos = response.json()
        assert isinstance(todos, list)
    
    @allure.title("PATCH /todos/:id - изменение статуса задачи")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_todo_status(self, api_client):
        # Создаем задачу
        todo_data = Config.TEST_TODO.copy()
        create_response = api_client.todos.create_todo(todo_data)
        todo_id = create_response.json().get('id')
        
        # Обновляем статус
        response = api_client.todos.partial_update_todo(todo_id, {"completed": True})
        
        assert response.status_code == 200
        data = response.json()
        assert data.get('completed') == True
    
    @allure.title("DELETE /todos/:id - удаление задачи")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_todo(self, api_client):
        # Создаем задачу
        todo_data = Config.TEST_TODO.copy()
        create_response = api_client.todos.create_todo(todo_data)
        todo_id = create_response.json().get('id')
        
        response = api_client.todos.delete_todo(todo_id)
        
        # JSONPlaceholder возвращает 200 вместо 204
        assert response.status_code in [200, 204]