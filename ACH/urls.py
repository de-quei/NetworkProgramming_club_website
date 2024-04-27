from django.urls import path

from ACH import views

app_name = 'ACH'

urlpatterns = [
    path('index/', views.show_index_html, name='index')
]