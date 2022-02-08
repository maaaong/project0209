from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.sendEmail, name='send')
    # http://127.0.0.1:8000/sendEmail/send/ 호출시 매칭
    # http://127.0.0.1:8000/send/ 이 호출은 매칭되지 않음
]