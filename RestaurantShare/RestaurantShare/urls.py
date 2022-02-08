"""RestaurantShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('shareRes.urls')), # shareRes app은 기본 요청부터 기본 요청으로 시작하는 url 처리한다. 단, 아래 url은 제외(가장 높은 우선순위->맨 위에 설정)
    path('sendEmail/',include('sendEmail.urls')), # sendEmail app은 http://127.0.0.1:8000/sendEmail/ 요청을 처리한다.
    path('admin/', admin.site.urls),
]
# shareRes app은 기본 요청부터 처리한다.
