from django.shortcuts import render
from django.views import View

from chat_app.registration import req_handler


class RegistrationView(View):

    def post(self, request, *args, **kwargs):
        return req_handler(request)
