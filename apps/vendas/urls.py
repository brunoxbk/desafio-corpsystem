from django.urls import path
from apps.vendas import views

app_name = 'vendas'

urlpatterns = [
    path('vendedores/', views.VendedorListCreate.as_view(), name='vendedor-list-create'),
    path('vendedores/<int:pk>/', views.VendedorDetail.as_view(), name='vendedor-detail'),
    path('', views.VendaListCreate.as_view(), name='venda-list-create'),
    path('<int:pk>/', views.VendaDetail.as_view(), name='venda-detail')
]
