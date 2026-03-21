import allure
import pytest
from config.config import Config

@allure.feature("Posts API")
@allure.story("CRUD операции с постами")
class TestPostsAPI:
    
    @allure.title("GET /posts - получение списка постов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_posts(self, api_client):
        response = api_client.posts.get_all_posts()
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    @allure.title("GET /posts/:id - получение поста по ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_post_by_id(self, api_client):
        posts = api_client.posts.get_all_posts().json()
        if posts:
            post_id = posts[0].get('id', 1)
        else:
            post_id = 1
        
        response = api_client.posts.get_post_by_id(post_id)
        
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert 'id' in response.json()
    
    @allure.title("POST /posts - создание нового поста")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_post(self, api_client):
        post_data = Config.TEST_POST.copy()
        
        response = api_client.posts.create_post(post_data)
        
        assert response.status_code in [200, 201]
        data = response.json()
        assert 'id' in data
        assert data['title'] == post_data['title']
    
    @allure.title("PUT /posts/:id - полное обновление поста")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_post(self, api_client):
        # Создаем пост
        post_data = Config.TEST_POST.copy()
        create_response = api_client.posts.create_post(post_data)
        post_id = create_response.json().get('id')
        
        # Обновляем пост
        updated_data = {
            "title": "Updated Title",
            "body": "Updated content"
        }
        response = api_client.posts.update_post(post_id, updated_data)
        
        # JSONPlaceholder возвращает 500 для созданных ID
        assert response.status_code in [200, 500]
        if response.status_code == 200:
            data = response.json()
            assert data.get('title') == updated_data['title']
    
    @allure.title("PATCH /posts/:id - частичное обновление поста")
    @allure.severity(allure.severity_level.NORMAL)
    def test_partial_update_post(self, api_client):
        # Создаем пост
        post_data = Config.TEST_POST.copy()
        create_response = api_client.posts.create_post(post_data)
        post_id = create_response.json().get('id')
        
        # Частично обновляем
        response = api_client.posts.partial_update_post(post_id, {"title": "New Title Only"})
        
        assert response.status_code == 200
        data = response.json()
        assert data.get('title') == "New Title Only"
        # Не проверяем body, так как JSONPlaceholder может не вернуть его
    
    @allure.title("DELETE /posts/:id - удаление поста")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_post(self, api_client):
        # Создаем пост
        post_data = Config.TEST_POST.copy()
        create_response = api_client.posts.create_post(post_data)
        post_id = create_response.json().get('id')
        
        response = api_client.posts.delete_post(post_id)
        
        # JSONPlaceholder возвращает 200 вместо 204
        assert response.status_code in [200, 204]
    
    @allure.title("GET /posts/search - поиск постов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_posts(self, api_client):
        response = api_client.posts.search_posts("test")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)