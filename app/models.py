from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    chai_type_choices=[
        ('ML','Masala Chai'),
        ('GR','Ginger Chai'),
        ('CC','Cardamom Chai'),
        ('TC','Tulsi Chai'),
        ('ElaiC','Elaichi Chai'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chai_images/')
    date_added=models.DateTimeField(default=timezone.now)
    description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    type=models.CharField(max_length=5,choices=chai_type_choices,default='ML')
