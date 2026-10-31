from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Pokemon, Entrenador, Gimnasio


def home(request):
    contexto = {
        'pokemons': Pokemon.objects.select_related('entrenador'),
        'entrenadores': Entrenador.objects.all(),
        'gimnasios': Gimnasio.objects.select_related('lider_del_gym'),
    }
    return render(request, 'visual/index.html', contexto)


class FormularioMixin:
    template_name = 'visual/form.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class EliminarMixin:
    template_name = 'visual/confirmar_eliminar.html'
    success_url = reverse_lazy('home')


class PokemonCrear(FormularioMixin, CreateView):
    model = Pokemon
    extra_context = {'titulo': 'Nuevo Pokémon'}

class PokemonEditar(FormularioMixin, UpdateView):
    model = Pokemon
    extra_context = {'titulo': 'Editar Pokémon'}

class PokemonEliminar(EliminarMixin, DeleteView):
    model = Pokemon



class EntrenadorCrear(FormularioMixin, CreateView):
    model = Entrenador
    extra_context = {'titulo': 'Nuevo Entrenador'}

class EntrenadorEditar(FormularioMixin, UpdateView):
    model = Entrenador
    extra_context = {'titulo': 'Editar Entrenador'}

class EntrenadorEliminar(EliminarMixin, DeleteView):
    model = Entrenador


class GimnasioCrear(FormularioMixin, CreateView):
    model = Gimnasio
    extra_context = {'titulo': 'Nuevo Gimnasio'}

class GimnasioEditar(FormularioMixin, UpdateView):
    model = Gimnasio
    extra_context = {'titulo': 'Editar Gimnasio'}

class GimnasioEliminar(EliminarMixin, DeleteView):
    model = Gimnasio