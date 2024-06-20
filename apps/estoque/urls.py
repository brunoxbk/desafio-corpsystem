from django.urls import path
from apps.estoque import views

app_name = 'estoque'

urlpatterns = [
    
    path('produtos/', views.ProdutoListCreate.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view(), name='produto-detail'),
    path('estoque/', views.EstoqueListCreate.as_view(), name='estoque-list-create'),
    path('estoque/<int:pk>/', views.EstoqueDetail.as_view(), name='estoque-detail')
]
