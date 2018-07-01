from django.http import HttpResponse

# Create your views here.


def its_alive_view(request):
    return HttpResponse('<h1> Its Alive<h1>')
