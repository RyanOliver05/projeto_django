from django.urls import path
from app_cad_funcionarios import views

urlpatterns = [
    # Rota, View responsavel, nome de referencia
    # resgistroponto.com
    path('', views.home, name= 'home'),
    # resgistroponto.com/funcionarios
    path('funcionarios/', views.funcionarios, name='listagem_funcionarios')
]
