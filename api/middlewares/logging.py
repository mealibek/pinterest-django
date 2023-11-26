import logging


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user_agent = request.META.get('HTTP_USER_AGENT')
        logging.info(f"User Agent: {user_agent}")
        return response
