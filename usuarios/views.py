from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_login = form['nome_login'].value()
            senha = form['senha'].value()

            # Authenticate the user
            usuario = auth.authenticate(
                request,
                username=nome_login, 
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario) 
                messages.success(request, f'{nome_login} Logado com sucesso!')
                return redirect('index')
            else: # Log the user in
                messages.error(request, f'erro ao efeituar o login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    # If the user is already authenticated, redirect to login
    # Handle form submission
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            # Check if the username already exists
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuario já existe.')
                return redirect('cadastro')
            
            # Create the user
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CadastroForms()  # Reinitialize the form for GET requests    
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')  # Redirect to login after logout