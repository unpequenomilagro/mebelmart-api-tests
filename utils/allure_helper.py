import allure
import json

class AllureHelper:
    """Хелпер для работы с Allure"""
    
    @staticmethod
    def attach_request(method: str, url: str, body: dict = None, params: dict = None):
        """Прикрепить информацию о запросе к отчету"""
        request_info = f"{method.upper()} {url}\n"
        if params:
            request_info += f"Params: {json.dumps(params, indent=2, ensure_ascii=False)}\n"
        if body:
            request_info += f"Body:\n{json.dumps(body, indent=2, ensure_ascii=False)}"
        allure.attach(request_info, name=f"Request", attachment_type=allure.attachment_type.TEXT)
    
    @staticmethod
    def attach_response(status_code: int, body: dict = None):
        """Прикрепить информацию об ответе к отчету"""
        response_info = f"Status Code: {status_code}\n"
        if body:
            response_info += f"Body:\n{json.dumps(body, indent=2, ensure_ascii=False)}"
        allure.attach(response_info, name=f"Response", attachment_type=allure.attachment_type.TEXT)