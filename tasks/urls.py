from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Tasks
    path('tasks/', views.task_list, name='task_list'),  # ✅ This shows all tasks

    path('tasks/add/', views.add_task, name='add_task'),
   # path('tasks/<int:pk>/', views.edit_task, name='task_detail'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),

    # Comments
    path('comment/<int:task_id>/', views.add_comment, name='add_comment'),

    # Team
    #path('team/', views.team_view, name='team'),  # this 'name' must match
    path('teams/', views.team_list, name='team_list'),

    path('team/', views.team_management, name='team_management'),
    path('team/add/', views.team_create, name='team_create'),

    # Admin-only
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('users/', views.user_list, name='user_list'),
]
