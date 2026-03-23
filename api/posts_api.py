from api.base_api import BaseAPI
import allure

class PostsAPI(BaseAPI):
    """API для работы с постами"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/posts"
    
    @allure.step("GET /posts - получить все посты")
    def get_all(self):
        return self._make_request('GET', self.endpoint)
    
    @allure.step("GET /posts/{post_id} - получить пост по ID")
    def get_by_id(self, post_id: int):
        return self._make_request('GET', f"{self.endpoint}/{post_id}")
    
    @allure.step("POST /posts - создать пост")
    def create(self, data: dict):
        return self._make_request('POST', self.endpoint, json=data)
    
    @allure.step("PUT /posts/{post_id} - обновить пост")
    def update(self, post_id: int, data: dict):
        return self._make_request('PUT', f"{self.endpoint}/{post_id}", json=data)
    
    @allure.step("PATCH /posts/{post_id} - частично обновить пост")
    def partial_update(self, post_id: int, data: dict):
        return self._make_request('PATCH', f"{self.endpoint}/{post_id}", json=data)
    
    @allure.step("DELETE /posts/{post_id} - удалить пост")
    def delete(self, post_id: int):
        return self._make_request('DELETE', f"{self.endpoint}/{post_id}")