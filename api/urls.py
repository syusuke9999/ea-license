from django.urls import path
from .views import Login, AuthAPI
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('login/', csrf_exempt(Login.post), name='login'),  # ここでスラッシュを追加
    path('authAPI/', AuthAPI.as_view()),  # こちらも同様にスラッシュを追加
]