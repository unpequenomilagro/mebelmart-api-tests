from api.base_api import BaseAPI
import allure

class TodosAPI(BaseAPI):
    """API для работы с задачами"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/todos"
    
    @allure.step("GET /todos - получить все задачи")
    def get_all(self):
        return self._make_request('GET', self.endpoint)
    
    @allure.step("GET /todos/{todo_id} - получить задачу по ID")
    def get_by_id(self, todo_id: int):
        return self._make_request('GET', f"{self.endpoint}/{todo_id}")
    
    @allure.step("POST /todos - создать задачу")
    def create(self, data: dict):
        return self._make_request('POST', self.endpoint, json=data)
    
    @allure.step("PATCH /todos/{todo_id} - обновить задачу")
    def update(self, todo_id: int, data: dict):
        return self._make_request('PATCH', f"{self.endpoint}/{todo_id}", json=data)
    
    @allure.step("DELETE /todos/{todo_id} - удалить задачу")
    def delete(self, todo_id: int):
        return self._make_request('DELETE', f"{self.endpoint}/{todo_id}")