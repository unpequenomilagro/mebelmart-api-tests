from api.base_api import BaseAPI
import allure

class CommentsAPI(BaseAPI):
    """API для работы с комментариями"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/comments"
    
    @allure.step("Получить список всех комментариев")
    def get_all_comments(self, params: dict = None):
        """GET /comments - получить все комментарии"""
        return self.get(self.endpoint, params=params)
    
    @allure.step("Получить комментарий по ID: {comment_id}")
    def get_comment_by_id(self, comment_id: int):
        """GET /comments/:id - получить комментарий по ID"""
        return self.get(f"{self.endpoint}/{comment_id}")
    
    @allure.step("Создать новый комментарий")
    def create_comment(self, comment_data: dict):
        """POST /comments - создать комментарий"""
        return self.post(self.endpoint, json=comment_data)
    
    @allure.step("Обновить комментарий (полностью) по ID: {comment_id}")
    def update_comment(self, comment_id: int, comment_data: dict):
        """PUT /comments/:id - полностью обновить комментарий"""
        return self.put(f"{self.endpoint}/{comment_id}", json=comment_data)
    
    @allure.step("Частично обновить комментарий по ID: {comment_id}")
    def partial_update_comment(self, comment_id: int, comment_data: dict):
        """PATCH /comments/:id - частично обновить комментарий"""
        return self.patch(f"{self.endpoint}/{comment_id}", json=comment_data)
    
    @allure.step("Удалить комментарий по ID: {comment_id}")
    def delete_comment(self, comment_id: int):
        """DELETE /comments/:id - удалить комментарий"""
        return self.delete(f"{self.endpoint}/{comment_id}")
    
    @allure.step("Получить комментарии для поста: {post_id}")
    def get_comments_by_post(self, post_id: int):
        """GET /comments?postId=... - фильтрация по посту"""
        return self.get(self.endpoint, params={"postId": post_id})