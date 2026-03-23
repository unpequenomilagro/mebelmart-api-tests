from api.base_api import BaseAPI
import allure

class UsersAPI(BaseAPI):
    """API для работы с пользователями"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/users"
    
    @allure.step("GET /users - получить всех пользователей")
    def get_all(self):
        return self._make_request('GET', self.endpoint)
    
    @allure.step("GET /users/{user_id} - получить пользователя по ID")
    def get_by_id(self, user_id: int):
        return self._make_request('GET', f"{self.endpoint}/{user_id}")
    
    @allure.step("POST /users - создать пользователя")
    def create(self, data: dict):
        return self._make_request('POST', self.endpoint, json=data)
    
    @allure.step("PUT /users/{user_id} - обновить пользователя")
    def update(self, user_id: int, data: dict):
        return self._make_request('PUT', f"{self.endpoint}/{user_id}", json=data)
    
    @allure.step("PATCH /users/{user_id} - частично обновить пользователя")
    def partial_update(self, user_id: int, data: dict):
        return self._make_request('PATCH', f"{self.endpoint}/{user_id}", json=data)
    
    @allure.step("DELETE /users/{user_id} - удалить пользователя")
    def delete(self, user_id: int):
        return self._make_request('DELETE', f"{self.endpoint}/{user_id}")