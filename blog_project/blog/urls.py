"""blog_project URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), # https:localhost:8000/media/blog/
    path('create/', views.create, name = 'create'), # https:localhost:8000/media/create/
    path('delete/<int:id>/', views.delete, name = 'delete'), # https:localhost:8000/media/delete/<id>/
    path('update/<int:id>/', views.update, name = 'update'), # https:localhost:8000/media/update/<id>/
]

# id가 3인 데이터 삭제 => # https:localhost:8000/media/delete/3/
# id가 5인 데이터 수정 => # https:localhost:8000/media/update/5/