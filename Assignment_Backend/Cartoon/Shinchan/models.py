from django.db import models

class ShinchanMovies(models.Model):
    Title=models.CharField(max_length=200)
    Year=models.DateField(default=0)
    IMDB=models.FloatField()
    Cover=models.ImageField(upload_to="CoverPages")
    Duration=models.IntegerField(default=0)

    def __str__(self):
        return self.Title

class SchinchanSeries(models.Model):
    Season=models.IntegerField(default=0)
    Episodes=models.IntegerField(default=0)
    Relise_Year=models.IntegerField(default=0)

    def __str__(self):
        return "Season"+" "+str(self.Season)
