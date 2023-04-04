from django.shortcuts import render
from django.http import HttpResponse

# TODO: Serializacja danych, hashowanie haseł


def users(request):
    return HttpResponse("Tu będą użytkownicy")
