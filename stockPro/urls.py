from django.urls import path
from . import views
app_name = 'stockPro' 

urlpatterns = [
    path('', views.stock_data, name='stock_data'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    
]
