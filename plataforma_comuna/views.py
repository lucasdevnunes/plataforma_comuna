from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à plataforma da Comunidade da Graça em Ubatuba!")