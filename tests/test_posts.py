import allure
import pytest
from config.config import Config

@allure.feature("Posts API")
class TestPostsAPI:
    
    @allure.title("GET /posts - получение всех постов")
    def test_get_all_posts(self, api_client):
        response = api_client.posts.get_all()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
    
    @allure.title("GET /posts/:id - получение поста по ID")
    def test_get_post_by_id(self, api_client):
        response = api_client.posts.get_by_id(1)
        assert response.status_code == 200
        assert response.json()['id'] == 1
    
    @allure.title("GET /posts/:id - пост не найден (404)")
    def test_get_post_not_found(self, api_client):
        response = api_client.posts.get_by_id(999999)
        assert response.status_code == 404
    
    @allure.title("POST /posts - создание поста")
    def test_create_post(self, api_client):
        post_data = Config.TEST_POST.copy()
        response = api_client.posts.create(post_data)
        assert response.status_code == 201
        data = response.json()
        assert 'id' in data
        assert data['title'] == post_data['title']
        assert data['body'] == post_data['body']
    
    @allure.title("PATCH /posts/:id - обновление поста")
    def test_partial_update_post(self, api_client):
        post_data = Config.TEST_POST.copy()
        create_resp = api_client.posts.create(post_data)
        post_id = create_resp.json()['id']
        
        response = api_client.posts.partial_update(post_id, {"title": "New Title"})
        assert response.status_code == 200
        assert response.json()['title'] == "New Title"
    
    @allure.title("DELETE /posts/:id - удаление поста")
    def test_delete_post(self, api_client):
        post_data = Config.TEST_POST.copy()
        create_resp = api_client.posts.create(post_data)
        post_id = create_resp.json()['id']
        
        response = api_client.posts.delete(post_id)
        assert response.status_code in [200, 204]
        
        get_resp = api_client.posts.get_by_id(post_id)
        assert get_resp.status_code == 404