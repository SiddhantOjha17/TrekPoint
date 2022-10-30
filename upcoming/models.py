from django.db import models
# Create your models here.


class Treks(models.Model):
    name = models.CharField(max_length= 50)
    price = models.IntegerField()
    short_description = models.CharField(max_length= 250)
    long_description = models.CharField(max_length= 100000, default=False)
    day1 = models.CharField(max_length=2500,default=False, null=True, blank=True)
    day2 = models.CharField(max_length=2500, default=False,null=True, blank=True)
    day3 = models.CharField(max_length=2500, null=True, default=False,blank=True)
    day4 = models.CharField(max_length=2500, null=True, default=False,blank=True)
    day5 = models.CharField(max_length=2500, null=True, default=False,blank=True)
    day6 = models.CharField(max_length=2500, null=True, default=False,blank=True)
    pdf = models.FileField(null=True, blank= True)
    altitude = models.IntegerField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    gallery1 = models.ImageField(null = True, blank= True)
    gallery2 = models.ImageField(null = True, blank= True)
    gallery3 = models.ImageField(null = True, blank= True)

    image = models.ImageField(null= True,blank= True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Treks"
