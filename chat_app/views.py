from django.shortcuts import render

from chat_app.registration import req_handler


def registration_handler(request):
    return req_handler(request)
