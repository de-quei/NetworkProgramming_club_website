from django.urls import path

from ACH import views

app_name = 'ACH'

urlpatterns = [
    path('index/', views.show_index_html, name='index'),
    path('ai_info/', views.show_ai_info_html, name='ai_info')
]