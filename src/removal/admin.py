from django.contrib import admin
from .models import Removal
# Register your models here.
class RemovalModelAdmin(admin.ModelAdmin):
    list_display = ["id", "remove_order_id","finale_id", "fn_sku", "ser_tag",
                    "sku", "product", "qty", "asin", "notes",
                    "notes", "condition_id", "updated", "timestamp"]
    class Meta:
        model = Removal


admin.site.register(Removal, RemovalModelAdmin)