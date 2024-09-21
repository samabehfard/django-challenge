from django.urls import path

from user.api.controller.sign_in_controller import SignInView
from user.api.controller.signup_controller import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]
