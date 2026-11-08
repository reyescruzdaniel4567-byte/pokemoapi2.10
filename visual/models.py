from django.db import models

class Entrenador(models.Model):
    id_documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)  
    apellido = models.CharField(max_length=100) 
    medallas = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id_documento} {self.nombre} {self.apellido} {self.medallas}'

class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100, default="Gimnasio Pokémon") 
    lider_del_gym = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='gimnasios')
    naturaleza_del_gym = models.CharField(max_length=30)
    medallas = models.CharField(max_length=30)
    latitud = models.FloatField(default=4.5981)   
    longitud = models.FloatField(default=-74.1297) 

    def __str__(self):
        return f'{self.nombre} - {self.lider_del_gym} ({self.medallas})'

class Pokemon(models.Model):
    tipo_naturaleza = [
        ('PL', 'Planta'),
        ('FU', 'Fuego'),
        ('AG', 'Agua'),
        ('EL', 'Eléctrico'),
        ('NO', 'Normal'),
        ('PS', 'Psíquico'),
        ('LU', 'Lucha'),
        ('VE', 'Veneno'),
        ('TI', 'Tierra'),
        ('VO', 'Volador'),
        ('RO', 'Roca'),
        ('BI', 'Bicho'),
        ('FA', 'Fantasma'),
        ('DR', 'Dragón'),
    ]
    
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True, related_name='pokemons')
    nombre = models.CharField(max_length=30)
    peso = models.DecimalField(max_digits=6, decimal_places=2) 
    imagen = models.ImageField(blank=True, null=True)
    habilidades = models.CharField(max_length=30)
    naturaleza = models.CharField(max_length=2, choices=tipo_naturaleza)
    descripcion = models.TextField() 
    def __str__(self):
        return f'{self.entrenador} {self.nombre} {self.peso} {self.imagen} {self.habilidades}'