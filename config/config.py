class Config:
    """Конфигурация для API тестов"""
    
    # Используем JSONPlaceholder - стабильный тестовый API
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # Таймауты
    REQUEST_TIMEOUT = 30
    
    # Тестовые данные
    TEST_USER = {
        "name": "Test User",
        "email": "test@example.com",
        "username": "testuser"
    }
    
    TEST_POST = {
        "title": "Test Post",
        "body": "This is a test post content",
        "userId": 1
    }
    
    TEST_TODO = {
        "title": "Test Todo",
        "completed": False,
        "userId": 1
    }
    
    TEST_COMMENT = {
        "name": "Test Comment",
        "body": "This is a test comment",
        "email": "commenter@example.com",
        "postId": 1
    }