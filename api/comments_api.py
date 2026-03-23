from api.base_api import BaseAPI
import allure

class CommentsAPI(BaseAPI):
    """API для работы с комментариями"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/comments"
    
    @allure.step("GET /comments - получить комментарии")
    def get_all(self, params: dict = None):
        """Получить комментарии с возможностью фильтрации (_limit, _page и т.д.)"""
        return self._make_request('GET', self.endpoint, params=params)
    
    @allure.step("GET /comments/{comment_id} - получить комментарий по ID")
    def get_by_id(self, comment_id: int):
        return self._make_request('GET', f"{self.endpoint}/{comment_id}")
    
    @allure.step("POST /comments - создать комментарий")
    def create(self, data: dict):
        return self._make_request('POST', self.endpoint, json=data)
    
    @allure.step("DELETE /comments/{comment_id} - удалить комментарий")
    def delete(self, comment_id: int):
        return self._make_request('DELETE', f"{self.endpoint}/{comment_id}")