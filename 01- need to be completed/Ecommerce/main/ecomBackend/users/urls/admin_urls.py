from django.contrib import admin
from django.urls import path, include
from users.views import users_list, create_user
from users.routes import ROUTES

urlpatterns = [
    path(ROUTES["user_list"], users_list),
    # path(ROUTES["create_user"], create_user),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
]
