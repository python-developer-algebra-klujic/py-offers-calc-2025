from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('users/<int:pk>/password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('users', UserListView.as_view(), name='users'),
    path('users/add/', UserCreateView.as_view(), name='users_add'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),
]
