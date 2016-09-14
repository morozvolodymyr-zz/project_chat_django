import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from chat_app.models import Credential, BlackList


@api_view(['GET'])
def get_all_users(request):
    if request.session.get('user_login') is not None and request.session.get('is_admin') is not None:
        all_users = Credential.objects.all()
        json_users = {'users': []}
        for user in all_users:
            temp = {}
            b = BlackList.objects.filter(id_user=user).first()
            temp['user'] = user.login
            if b is not None:
                temp['blacklist'] = 'Y'
            else:
                temp['blacklist'] = 'N'
            json_users['users'].append(temp)
        return HttpResponse(json.dumps(json_users), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET', 'POST'])
def add_user_to_bl(request):
    if request.session.get('user_login') is not None and request.session.get('is_admin') is not None:
        json_data = JSONParser().parse(request)
        name = json_data['user']
        c = Credential.objects.filter(login=name).first()
        b = BlackList(id_user=c)
        b.save()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['DELETE'])
def del_user_from_bl(request, name):
    if request.session.get('user_login') is not None and request.session.get('is_admin') is not None:
        # c = Credential.objects.filter(login=name).first()
        b = BlackList.objects.filter(id_user__login=name).first()
        b.delete()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)