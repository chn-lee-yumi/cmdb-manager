# tools/middleware.py

from django.utils.deprecation import MiddlewareMixin

class CloseCsrfMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.csrf_processing_done = True  
# class DisableCSRF(object):
#     def process_request(self, request):
#         setattr(request, '_dont_enforce_csrf_checks', True)
