from django.urls import path
from .views import LoginTemplateView, CadastroTemplateView

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('cadastro/', CadastroTemplateView.as_view(), name='cadastro'),
]