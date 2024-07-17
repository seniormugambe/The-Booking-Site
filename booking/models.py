from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} - {self.item} - {self.quantity}'
