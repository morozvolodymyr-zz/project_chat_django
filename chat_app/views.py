from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from chat_app.forms import LoginForm
from chat_app.models import Credential


class RegistrationView(View):
    def post(self, request, *args, **kwargs):
        user_name = request.POST['name']
        user_surname = request.POST['surname']
        user_login = request.POST['login']
        user_password = request.POST['password']
        try:
            if user_name is not None and len(user_name) <= 30:
                if user_surname is not None and len(user_surname) <= 30:
                    if user_login is not None and len(user_login) <= 20:
                        if user_password is not None and len(user_password) <= 20:
                            credential = Credential(name=user_name, surname=user_surname, login=user_login, password=user_password, is_admin=False)
                            credential.save()
                            return render(request, 'index.html', {})
        except Exception:
            pass

        return render(request, 'registration.html', {'error':'error in registration'})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.session.get('user_login') is not None:
            return render(request, 'chat.html', {'user':request.session.get('user_login')})
        else:
            form = self.get_form(LoginView.form_class)
            return render(request, LoginView.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_login = login_form.cleaned_data['login']
            user_password = login_form.cleaned_data['password']
            c = Credential.objects.filter(login=user_login, password=user_password).first()
            if c is not None:
                request.session['user_login'] = user_login
                if c.is_admin:
                    return render(request, 'admin.html', {'user':user_login})
                else:
                    return render(request, 'chat.html', {'user':user_login})
            else:
                return render(request, 'login.html', {'error':'login incorrect', 'form':LoginForm})
