import allure
import json

class AllureHelper:
    """Хелпер для работы с Allure в API тестах"""
    
    @staticmethod
    def attach_request(method: str, url: str, headers: dict = None, body: dict = None):
        """Прикрепить информацию о запросе к отчету"""
        request_info = f"{method.upper()} {url}\n\n"
        if headers:
            request_info += f"Headers:\n{json.dumps(headers, indent=2, ensure_ascii=False)}\n\n"
        if body:
            request_info += f"Body:\n{json.dumps(body, indent=2, ensure_ascii=False)}"
        
        allure.attach(
            request_info,
            name=f"Request: {method} {url}",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @staticmethod
    def attach_response(status_code: int, body: dict = None, headers: dict = None):
        """Прикрепить информацию об ответе к отчету"""
        response_info = f"Status Code: {status_code}\n\n"
        if headers:
            response_info += f"Headers:\n{json.dumps(headers, indent=2, ensure_ascii=False)}\n\n"
        if body:
            response_info += f"Body:\n{json.dumps(body, indent=2, ensure_ascii=False)}"
        
        allure.attach(
            response_info,
            name=f"Response: {status_code}",
            attachment_type=allure.attachment_type.TEXT
        )