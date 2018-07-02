from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import FarmModel, AnimalWeigthModel
from .forms import AnimalWeigthForm


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):

    template_name = 'home.html'

    def get_queryset(self):
        return FarmModel.objects.filter(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class ListAnimalWeigth(ListView):
    template_name = 'list_animals.html'

    def get_queryset(self):
        return AnimalWeigthModel.objects.filter(farm__token=self.kwargs['farm'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'farm': self.kwargs['farm']})
        return context


@method_decorator(login_required, name='dispatch')
class CreateAnimalWeigth(CreateView):
    template_name = 'create_animals.html'
    form_class = AnimalWeigthForm
    success_url = reverse_lazy('animal_weigth:home')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)

        if form.is_valid():
            self.object = form.save(commit=False)
            farm = FarmModel.objects.get(token=self.kwargs['farm'])
            self.object.farm = farm
            self.object.save()

            return self.form_valid(form)

        return self.form_invalid(form)


@method_decorator(login_required, name='dispatch')
class UpdateAnimalWeigth(UpdateView):
    template_name = 'create_animals.html'
    model = AnimalWeigthModel
    success_url = reverse_lazy('animal_weigth:home')
    fields = ['type_animal', 'weigth', 'earring_number']
