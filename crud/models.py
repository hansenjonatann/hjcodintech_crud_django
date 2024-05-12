from django.db import models

# Create your models here.
class BahasaPemograman(models.Model):
  nama_bahasa = models.CharField(max_length=200)
  tahun_rilis = models.CharField(max_length=200)

class Sintaks(models.Model):
  nama_sintaks = models.CharField(max_length=200)

class Variabel(models.Model):
  nama_variabel = models.CharField(max_length=200)

class Program(models.Model):
  nama_program = models.CharField(max_length=200)
  bahasa = models.ForeignKey(BahasaPemograman , on_delete=models.CASCADE)
  sintaks = models.ForeignKey(Sintaks , on_delete=models.CASCADE)
  variabel = models.ForeignKey(Variabel , on_delete=models.CASCADE)

