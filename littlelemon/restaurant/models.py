from django.db import models

class BookingTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_item(self):
        return f'{self.name} : {str(self.no_of_guests)}'

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.BooleanField()

    def __str__(self):
        return self.title
