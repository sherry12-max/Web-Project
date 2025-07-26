from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse


def logout_and_signup(request):
    """
    Custom view to logout the current user and redirect to signup page.
    This ensures that when users click "Create New Account" from the logout page,
    they are properly logged out before being redirected to signup.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect('account_signup')
