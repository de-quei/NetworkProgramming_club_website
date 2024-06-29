from django.urls import path

from ACH import views

app_name = 'ACH'

urlpatterns = [
    path('', views.show_index_html, name='index'),
    path('ai_info/', views.show_ai_info_html, name='ai_info'),
    path('board/', views.BoardListView.as_view(), name='board_list'),
    path('create/', views.BoardCreateView.as_view(), name='board_create')
]