from django.db import models

class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True)

class Languages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True)

class LaanuageAndCountries(models.Model):
    id = models.IntegerField(primary_key=True)
    country_id = models.ForeignKey('Countries')
    language_id = models.ForeignKey('Languages')


