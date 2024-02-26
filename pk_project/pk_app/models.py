from django.db import models

class Currency (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name
    
