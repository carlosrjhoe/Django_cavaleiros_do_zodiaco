# language:pt

Funcionalidade: Login
"""Fazer login com sucesso"""

Cenário: Efetuar login com sucesso
    Dado que esteja na pagina "http://127.0.0.1:8000/"
    Quando inserir o "nome" "Admin"
    E inserir "senha" "Admin"
    Então clicar no botão "logar"
