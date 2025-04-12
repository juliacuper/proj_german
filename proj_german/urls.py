"""proj_german URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    3. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('terms/', views.terms_list, name='terms_list'),  # Список терминов
    path('add-term/', views.add_term, name='add_term'),  # Форма для добавления термина
    path('send-term/', views.send_term, name='send_term'),  # Обработка отправки термина
    path('stats/', views.show_stats, name='show_stats'),  # Статистика по терминам
]
