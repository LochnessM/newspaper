from django.db import models


class artikulli(models.Model):
    zgjedhje_e_kategorise = [('Aktualitet', 'Aktualitet'),
                            ('Politike', 'Politike'),
                            ('Ekonomi', 'Ekonomi'), 
                            ('Opinion', 'Opinion'),
                            ('Sporti', 'Sporti'),
                            ('Kulture', 'Kulture')]
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    description = models.TextField()
    kategoria = models.CharField(max_length=10, choices=zgjedhje_e_kategorise, blank=True) 
    data = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='artikulli/images/', blank=True)
