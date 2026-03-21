from api.base_api import BaseAPI
import allure

class PostsAPI(BaseAPI):
    """API для работы с постами"""
    
    def __init__(self):
        super().__init__()
        self.endpoint = "/posts"
    
    @allure.step("Получить список всех постов")
    def get_all_posts(self, params: dict = None):
        """GET /posts - получить все посты"""
        return self.get(self.endpoint, params=params)
    
    @allure.step("Получить пост по ID: {post_id}")
    def get_post_by_id(self, post_id: int):
        """GET /posts/:id - получить пост по ID"""
        return self.get(f"{self.endpoint}/{post_id}")
    
    @allure.step("Создать новый пост")
    def create_post(self, post_data: dict):
        """POST /posts - создать пост"""
        return self.post(self.endpoint, json=post_data)
    
    @allure.step("Обновить пост (полностью) по ID: {post_id}")
    def update_post(self, post_id: int, post_data: dict):
        """PUT /posts/:id - полностью обновить пост"""
        return self.put(f"{self.endpoint}/{post_id}", json=post_data)
    
    @allure.step("Частично обновить пост по ID: {post_id}")
    def partial_update_post(self, post_id: int, post_data: dict):
        """PATCH /posts/:id - частично обновить пост"""
        return self.patch(f"{self.endpoint}/{post_id}", json=post_data)
    
    @allure.step("Удалить пост по ID: {post_id}")
    def delete_post(self, post_id: int):
        """DELETE /posts/:id - удалить пост"""
        return self.delete(f"{self.endpoint}/{post_id}")
    
    @allure.step("Поиск постов по запросу: {query}")
    def search_posts(self, query: str):
        """GET /posts?q=... - поиск постов (в JSONPlaceholder нет поиска, просто фильтр)"""
        return self.get(self.endpoint, params={"title_like": query})
    
    @allure.step("Получить комментарии поста по ID: {post_id}")
    def get_post_comments(self, post_id: int):
        """GET /posts/:id/comments - получить комментарии к посту"""
        return self.get(f"{self.endpoint}/{post_id}/comments")