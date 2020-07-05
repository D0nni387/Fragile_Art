from django.db import models
from django.db.models import Sum
from django.conf import settings 

from store.models import Product

import uuid

# Create your models here.


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    telephone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=128, null=False, blank=False)
    street_address2 = models.CharField(max_length=128, null=False, blank=False)
    county_state = models.CharField(max_length=64, null=True, blank=True)
    postcode_zip = models.CharField(max_length=12, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_charge = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def _order_number_generation(self):
        """
        Generates a random order number ( Private method )
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        If the order number has not been set, override the original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def total_update(self):
        """
        Updates the grand total as a new line is added and accounts for delivery cost to suit
        """
        self.total_order = self.lineitems.aggregate(Sum('line_total'))['line_total__sum']
        self.delivery_charge = self.order_total * settings.DELIVERY_PERCENTAGE / 100
        self.grand_total = self.total_order + self.delivery_charge
        self.save()
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)