from django.db import models


# Create your models here.
class Removal(models.Model):
    id = models.AutoField(primary_key=True)
    remove_order_id = models.CharField(blank=True,max_length=120)
    finale_id = models.CharField(blank=True, max_length=120)
    fn_sku = models.CharField(blank=True, max_length=120)
    ser_tag = models.CharField(blank=True, max_length=120)
    sku = models.CharField(blank=True, max_length=120)
    product = models.CharField(blank=True, max_length=220)
    qty = models.IntegerField(blank=True)
    asin = models.CharField(blank=True,max_length=120)
    notes = models.TextField(blank=True)
    condition_id = models.IntegerField(blank=True, default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.remove_order_id
    def __str__(self):
        return self.remove_order_id

class Condition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)