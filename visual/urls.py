from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pokemons/nuevo/', views.PokemonCrear.as_view(), name='pokemon_crear'),
    path('pokemons/<int:pk>/editar/', views.PokemonEditar.as_view(), name='pokemon_editar'),
    path('pokemons/<int:pk>/eliminar/', views.PokemonEliminar.as_view(), name='pokemon_eliminar'),
    path('entrenadores/nuevo/', views.EntrenadorCrear.as_view(), name='entrenador_crear'),
    path('entrenadores/<int:pk>/editar/', views.EntrenadorEditar.as_view(), name='entrenador_editar'),
    path('entrenadores/<int:pk>/eliminar/', views.EntrenadorEliminar.as_view(), name='entrenador_eliminar'),
    path('gimnasios/nuevo/', views.GimnasioCrear.as_view(), name='gimnasio_crear'),
    path('gimnasios/<int:pk>/editar/', views.GimnasioEditar.as_view(), name='gimnasio_editar'),
    path('gimnasios/<int:pk>/eliminar/', views.GimnasioEliminar.as_view(), name='gimnasio_eliminar'),
    path('mapa-gimnasios/', views.home, name='mapa.html'),
    path('buscar/', views.buscar, name='buscar'),
]