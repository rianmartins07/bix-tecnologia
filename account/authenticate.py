from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

from django.middleware.csrf import CsrfViewMiddleware
from django.middleware.csrf import get_token

from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions

def enforce_csrf(request):
    """
    Enforce CSRF validation.
    """
    if not request.META.get("CSRF_COOKIE"):
        get_token(request)

    middleware = CsrfViewMiddleware()
    middleware.process_request(request)
    reason = middleware.process_view(request, None, (), {})
    if reason:
        # CSRF failed, bail with explicit error message
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

class CustomAuthentication(JWTAuthentication):
    
    def authenticate(self, request):
        header = self.get_header(request)
        
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token