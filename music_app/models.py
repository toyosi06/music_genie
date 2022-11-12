from django.db import models

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    nationality = models.CharField(max_length=200, null=False)
    website = models.CharField(max_length=100, null=False)
    height = models.CharField(max_length=100, null=False)
    label = models.CharField(max_length=200, null=False)
    image_url = models.CharField(max_length=200, null=False)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=60, null=False)
    title = models.CharField(max_length=100, null=False)
    release_date = models.DateField(null=True, auto_now=False)
    album = models.CharField(max_length=80, null=True)
    artist= models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

@property 
def artistName(self): 
    return self.artist.name 

@property 
def artistId(self):
    return self.artist.id