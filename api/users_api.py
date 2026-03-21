from api.base_api import BaseAPI
import allure

class UsersAPI(BaseAPI):
    """API для работы с пользователями"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/users"  # без префикса /api
    
    @allure.step("Получить список всех пользователей")
    def get_all_users(self, params: dict = None):
        """GET /users - получить всех пользователей"""
        return self.get(self.endpoint, params=params)
    
    @allure.step("Получить пользователя по ID: {user_id}")
    def get_user_by_id(self, user_id: int):
        """GET /users/:id - получить пользователя по ID"""
        return self.get(f"{self.endpoint}/{user_id}")
    
    @allure.step("Создать нового пользователя")
    def create_user(self, user_data: dict):
        """POST /users - создать пользователя"""
        return self.post(self.endpoint, json=user_data)
    
    @allure.step("Обновить пользователя (полностью) по ID: {user_id}")
    def update_user(self, user_id: int, user_data: dict):
        """PUT /users/:id - полностью обновить пользователя"""
        return self.put(f"{self.endpoint}/{user_id}", json=user_data)
    
    @allure.step("Частично обновить пользователя по ID: {user_id}")
    def partial_update_user(self, user_id: int, user_data: dict):
        """PATCH /users/:id - частично обновить пользователя"""
        return self.patch(f"{self.endpoint}/{user_id}", json=user_data)
    
    @allure.step("Удалить пользователя по ID: {user_id}")
    def delete_user(self, user_id: int):
        """DELETE /users/:id - удалить пользователя"""
        return self.delete(f"{self.endpoint}/{user_id}")