from api.base_api import BaseAPI
import allure

class TodosAPI(BaseAPI):
    """API для работы с задачами (todos)"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/todos"
    
    @allure.step("Получить список всех задач")
    def get_all_todos(self, params: dict = None):
        """GET /todos - получить все задачи"""
        return self.get(self.endpoint, params=params)
    
    @allure.step("Получить задачу по ID: {todo_id}")
    def get_todo_by_id(self, todo_id: int):
        """GET /todos/:id - получить задачу по ID"""
        return self.get(f"{self.endpoint}/{todo_id}")
    
    @allure.step("Создать новую задачу")
    def create_todo(self, todo_data: dict):
        """POST /todos - создать задачу"""
        return self.post(self.endpoint, json=todo_data)
    
    @allure.step("Обновить задачу (полностью) по ID: {todo_id}")
    def update_todo(self, todo_id: int, todo_data: dict):
        """PUT /todos/:id - полностью обновить задачу"""
        return self.put(f"{self.endpoint}/{todo_id}", json=todo_data)
    
    @allure.step("Частично обновить задачу по ID: {todo_id}")
    def partial_update_todo(self, todo_id: int, todo_data: dict):
        """PATCH /todos/:id - частично обновить задачу"""
        return self.patch(f"{self.endpoint}/{todo_id}", json=todo_data)
    
    @allure.step("Удалить задачу по ID: {todo_id}")
    def delete_todo(self, todo_id: int):
        """DELETE /todos/:id - удалить задачу"""
        return self.delete(f"{self.endpoint}/{todo_id}")
    
    @allure.step("Получить задачи с фильтрацией по статусу выполнения")
    def get_todos_by_completed_status(self, completed: bool):
        """GET /todos?completed=true/false - фильтрация по статусу"""
        return self.get(self.endpoint, params={"completed": str(completed).lower()})