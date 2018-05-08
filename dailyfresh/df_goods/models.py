from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.tname.encode('utf-8')

class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gimage = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=10, decimal_places=2)
    gunit = models.CharField(max_length=20, default='500g')
    gclick = models.IntegerField()
    gbrief_introduction = models.CharField(max_length=200)
    ginventory = models.IntegerField()
    gdetailed_introduction = HTMLField()
    gtype = models.ForeignKey(TypeInfo)
    isDeleted = models.BooleanField(default=False)

