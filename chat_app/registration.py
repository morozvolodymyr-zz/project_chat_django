from django.shortcuts import render
from chat_app import models


# def req_handler(request):
#     response = None
#     if request.session.get('uname') is not None and request.session.get('ulogin') is not None and request.session.get(
#             'upassword') is not None:
#         user_name = request.session.get('uname')
#         user_login = request.session.get('ulogin')
#         user_password = request.session.get('upassword')
#         response = render(request, 'temp.html', {'username': user_name, 'userlogin': user_login, 'userpassword': user_password})
#     else:
#         user_name = request.POST['name']
#         user_login = request.POST['login']
#         user_password = request.POST['password']
#         request.session['uname'] = user_name
#         request.session['ulogin'] = user_login
#         request.session['upassword'] = user_password
#         response = render(request, 'temp.html', {'username': user_name, 'userlogin': user_login, 'userpassword': user_password})

# def req_handler(request):
#     response = None
#     if request.COOKIES.get('uname') is not None and request.COOKIES.get('ulogin') is not None and request.COOKIES.get(
#             'upassword') is not None:
#         user_name = request.COOKIES.get('uname')
#         user_login = request.COOKIES.get('ulogin')
#         user_password = request.COOKIES.get('upassword')
#         response = render(request, 'temp.html', {'username': user_name, 'userlogin': user_login, 'userpassword': user_password})
#     else:
#         user_name = request.POST['name']
#         user_login = request.POST['login']
#         user_password = request.POST['password']
#         response = render(request, 'temp.html', {'username': user_name, 'userlogin': user_login, 'userpassword': user_password})
#         response.set_cookie('uname', user_name, 1000)
#         response.set_cookie('ulogin', user_login, 1000)
#         response.set_cookie('upassword', user_password, 1000)

# return response

def req_handler(request):
    # if request.session.get('uname') is not None and request.session.get('ulogin') is not None and request.session.get(
    #         'upassword') is not None:
    #     pass
    # else:
        user_name = request.POST['name']
        user_surname = request.POST['surname']
        user_login = request.POST['login']
        user_password = request.POST['password']
        user = models.Users(name=user_name, surname=user_surname)
        credential = models.Credential(login=user_login, password=user_password, is_admin=False)
        user.save()
        credential.save()
        request.session['uname'] = user_name
        request.session['suruname'] = user_surname
        request.session['ulogin'] = user_login
        request.session['upassword'] = user_password
