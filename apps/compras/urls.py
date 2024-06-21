from django.urls import path
from apps.compras import views

app_name = 'compras'

urlpatterns = [
    path('', views.CompraListCreate.as_view(), name='compra-list-create'),
    path('<int:pk>/', views.CompraDetail.as_view(), name='compra-detail'),
    path('compradores/', views.CompradorListCreate.as_view(), name='comprador-list-create'),
    path('compradores/<int:pk>/', views.CompradorDetail.as_view(), name='comprador-detail')
]
