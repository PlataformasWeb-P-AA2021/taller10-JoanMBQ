from django.db import models

class Parroquia(models.Model):
    tipo_parroquia = (
        ('Urbana', 'Urbana '),
        ('Rural', 'Rural'))
    nombre = models.CharField("Nombre Parroquia",max_length=50)
    tipo_parroquia = models.CharField("Ubicación de Parroquia",max_length=30, \
            choices=tipo_parroquia) 


    def __str__(self):
        return "Parroquia: %s \n|| Tipo parroquia: %s" % (
                self.nombre,
                self.tipo_parroquia)


class Barrio(models.Model):
    num_parques = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'))

    nombre = models.CharField("Nombre Barrio",max_length=50)
    num_viviendas = models.IntegerField("Número de viviendas")
    num_edificios = models.IntegerField("Número de edificios")
    num_parques = models.IntegerField("Numero de Parques", \
            choices= num_parques)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, \
    related_name="barrios")


    def __str__(self):
        return "Nombre: %s - Número Viviendas: %d - Número Edificios: %d - Número parques: %d " % (self.nombre, 
                self. num_viviendas,
                self.num_edificios,
                self.num_parques)