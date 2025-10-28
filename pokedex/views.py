from django.http import HttpResponse
from django.template import loader
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all ()
    pokemons = ['charmander', 'pikachu', 'squirtle']
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))