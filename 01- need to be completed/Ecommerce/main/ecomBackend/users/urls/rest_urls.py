from django.contrib import admin
from django.urls import path, include
from users.views import users_list, create_user, users, users_short_info
from users.routes import ROUTES

urlpatterns = [
    path(f"{ROUTES['user_rest_short_info']}<uuid:id>/", users_short_info),
    path(f"{ROUTES['user_rest_info']}<uuid:id>/", users),
    path(ROUTES["create_user"], create_user),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
]