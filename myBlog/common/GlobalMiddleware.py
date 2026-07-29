# myapp/middleware.py
import logging

from django.shortcuts import render
from requests.exceptions import ConnectionError, Timeout  # If using the 'requests' library

logger = logging.getLogger(__name__)

class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view is called
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """
        This method is called when a view raises an unhandled exception.
        It returns an HttpResponse or None.
        """
        # 1. Handle External Network / API failures
        if isinstance(exception, (ConnectionError, Timeout)):
            logger.error(f"Network error encountered: {exception}", exc_info=True)
            return render(
                request,
                'errors/network_error.html',
                {'message': 'We are having trouble connecting to our backend services. Please try again shortly.'},
                status=503
            )

        # 2. Handle specific database connectivity issues
        # if isinstance(exception, OperationalError):
        #     return render(request, 'errors/db_error.html', status=500)

        # 3. Log everything else, but let Django's default 500 handler pick it up
        logger.error(f"Unhandled exception: {exception}", exc_info=True)
        return None