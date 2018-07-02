from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME, forms, login as auth_login
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


def its_alive_view(request):
    return HttpResponse('<h1> Its Alive<h1>')





class AuthenticationForm(forms.AuthenticationForm):
    def clean_username(self):
        return self.cleaned_data['username'].lower()


@csrf_protect
def login(request, template_name='login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):


    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        user = User.objects.filter(email=request.POST.get('username', '')).first()
        if user:
            user = User.objects.get(email=request.POST.get('username', ''))

            
            if form.is_valid():
                if user.is_active:
                    auth_login(request, form.get_user())
                    return HttpResponseRedirect(request.GET.get('next','/'))

            elif not user.is_active:
                if authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', '')):
                    auth_login(request, form.get_user())

                    return HttpResponseRedirect(request.GET.get('next','/'))
                else:
                    messages.error(request, 'Usuário e/ou senha inválidos.')

            else:
                messages.error(request, 'Usuário e/ou senha inválidos.')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos.')

    else:
        form = authentication_form(request)


    context = {
        'form': form,
        redirect_field_name: redirect_field_name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context)