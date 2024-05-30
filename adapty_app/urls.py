from django.urls import path

from adapty_app.infrastructure.ports.http.views import UserView

urlpatterns = [
    path('user/', UserView.as_view(), name='user-device'),
]
