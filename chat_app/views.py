from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from chat_app.forms import LoginForm, RegistrationForm
from chat_app.models import Credential


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_name = registration_form.cleaned_data['name']
            user_surname = registration_form.cleaned_data['surname']
            user_login = registration_form.cleaned_data['login']
            user_password = registration_form.cleaned_data['password']
            try:
                if user_name is not None and len(user_name) <= Credential.max_len_users:
                    if user_surname is not None and len(user_surname) <= Credential.max_len_users:
                        if user_login is not None and len(user_login) <= Credential.max_len_cred:
                            if user_password is not None and len(user_password) <= Credential.max_len_cred:
                                credential = Credential(name=user_name, surname=user_surname, login=user_login, password=user_password, is_admin=False)
                                credential.save()
                                return render(request, 'index.html', {})
            except Exception:
                pass

            return render(request, 'registration.html', {'error': 'error in registration', 'form': RegistrationForm})


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
