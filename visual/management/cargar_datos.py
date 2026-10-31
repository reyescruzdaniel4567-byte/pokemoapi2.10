from django.core.management.base import BaseCommand
from django.db import models, transaction

from visual.models import Entrenador, Gimnasio, Pokemon

# (id_documento, nombre, apellido, medallas)
ENTRENADORES = [
    ("1011223341", "Santiago",  "Ramírez",  3),
    ("1022334452", "Valentina", "Gómez",    5),
    ("1033445563", "Mateo",     "Rodríguez", 2),
    ("1044556674", "Camila",    "Torres",   8),
    ("1055667785", "Sebastián", "Herrera",  4),
    ("1066778896", "Isabella",  "Vargas",   6),
    ("1077889907", "Andrés",    "Rocha",    8),
    ("1088990018", "Mariana",   "Castillo", 1),
    ("1099001129", "Julián",    "Moreno",   7),
    ("1100112230", "Daniela",   "Ortiz",    8),
    ("1111223341", "Felipe",    "Cárdenas", 0),
    ("1122334452", "Laura",     "Mejía",    5),
    ("1133445563", "Nicolás",   "Pardo",    3),
    ("1144556674", "Sofía",     "Navarro",  8),
    ("1155667785", "Esteban",   "Quintero", 2),
]

# (nombre, naturaleza, peso_kg, habilidades, descripcion, posicion_del_entrenador o None)
POKEMONS = [
    ("Bulbasaur",  "PL",   6.9, "Látigo Cepa, Drenadoras",        "Lleva una semilla en el lomo que crece junto a él.", 1),
    ("Charmander", "FU",   8.5, "Ascuas, Arañazo",                "La llama de su cola se aviva cuando está contento.", 0),
    ("Squirtle",   "AG",   9.0, "Pistola Agua, Burbuja",          "Se esconde en su caparazón y lanza chorros de agua.", 3),
    ("Pikachu",    "EL",   6.0, "Impactrueno, Cola Férrea",       "Acumula electricidad en sus mejillas y la libera en combate.", 2),
    ("Eevee",      "NO",   6.5, "Placaje, Látigo",                "Su cuerpo inestable le permite evolucionar de muchas formas.", 5),
    ("Abra",       "PS",  19.5, "Teletransporte, Psíquico",       "Duerme casi todo el día y se teletransporta al sentir peligro.", 4),
    ("Machop",     "LU",  19.5, "Golpe Kárate, Sumisión",         "Entrena a diario levantando rocas enormes.", 6),
    ("Koffing",    "VE",   1.0, "Bomba Lodo, Gas Venenoso",       "Flota gracias a los gases tóxicos que guarda en su interior.", 7),
    ("Diglett",    "TI",   0.8, "Excavar, Terremoto",             "Vive bajo tierra y solo asoma la cabeza.", 8),
    ("Pidgey",     "VO",   1.8, "Tornado, Ataque Ala",            "Vuela bajo y levanta polvo para despistar a sus rivales.", 9),
    ("Geodude",    "RO",  20.0, "Lanzarrocas, Autodestrucción",   "Se camufla entre las piedras del camino.", 10),
    ("Caterpie",   "BI",   2.9, "Disparo Demora, Placaje",        "Devora hojas sin parar para crecer rápido.", 11),
    ("Gastly",     "FA",   0.1, "Lengüetazo, Bola Sombra",        "Un ser de gas que aparece en lugares oscuros.", 12),
    ("Dratini",    "DR",   3.3, "Envoltura, Furia Dragón",        "Muda de piel varias veces a medida que crece.", 13),
    ("Snorlax",    "NO", 460.0, "Golpe Cuerpo, Descanso",         "Duerme casi todo el día y come montañas de comida.", None),
]

GIMNASIOS = [
    ("RO", "Roca",      "Medalla Roca",     6),
    ("AG", "Agua",      "Medalla Cascada",  3),
    ("EL", "Eléctrico", "Medalla Trueno",   9),
    ("PL", "Planta",    "Medalla Arcoíris", 1),
    ("VE", "Veneno",    "Medalla Alma",     13),
    ("PS", "Psíquico",  "Medalla Pantano",  5),
    ("FU", "Fuego",     "Medalla Volcán",   0),
    ("TI", "Tierra",    "Medalla Tierra",   8),
    ("VO", "Volador",   "Medalla Pluma",    4),
    ("LU", "Lucha",     "Medalla Puño",     2),
    ("FA", "Fantasma",  "Medalla Sombra",   7),
    ("DR", "Dragón",    "Medalla Colmillo", 10),
    ("BI", "Bicho",     "Medalla Capullo",  11),
    ("NO", "Normal",    "Medalla Llanura",  12),
    ("FU", "Fuego",     "Medalla Ceniza",   14),
]


class Command(BaseCommand):
    help = "Carga 15 entrenadores, 15 Pokémon y 15 gimnasios de ejemplo (no duplica si ya existen)."

    @transaction.atomic
    def handle(self, *args, **options):
        
        usa_codigos = bool(Gimnasio._meta.get_field("naturaleza_del_gym").choices)
       
        medalla_es_texto = isinstance(
            Gimnasio._meta.get_field("medallas"), (models.CharField, models.TextField)
        )

        entrenadores = []
        nuevos_e = 0
        for doc, nombre, apellido, medallas in ENTRENADORES:
            obj, creado = Entrenador.objects.get_or_create(
                id_documento=doc,
                defaults={"nombre": nombre, "apellido": apellido, "medallas": medallas},
            )
            entrenadores.append(obj)
            nuevos_e += creado

        nuevos_p = 0
        for nombre, naturaleza, peso, habilidades, descripcion, pos in POKEMONS:
            _, creado = Pokemon.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "naturaleza": naturaleza,
                    "peso": peso,
                    "habilidades": habilidades,
                    "descripcion": descripcion,
                    "entrenador": entrenadores[pos] if pos is not None else None,
                },
            )
            nuevos_p += creado

        nuevos_g = 0
        for codigo, tipo, medalla, pos in GIMNASIOS:
            _, creado = Gimnasio.objects.get_or_create(
                lider_del_gym=entrenadores[pos],
                defaults={
                    "naturaleza_del_gym": codigo if usa_codigos else tipo,
                    "medallas": medalla if medalla_es_texto else 1,
                },
            )
            nuevos_g += creado

        self.stdout.write(self.style.SUCCESS(
            f"Listo: {nuevos_e} entrenadores, {nuevos_p} Pokémon y {nuevos_g} gimnasios nuevos."
        ))
