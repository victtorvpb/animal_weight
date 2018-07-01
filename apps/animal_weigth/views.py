from django.views.generic import ListView


from .models import FarmModel


class HomeView(ListView):

    template_name = 'home.html'

    def get_queryset(self):
        return FarmModel.objects.filter(owner=self.request.user)
