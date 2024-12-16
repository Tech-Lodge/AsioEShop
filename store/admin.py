# from django.contrib import admin
# import models
#
#
# # Register your models here.
# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     ...
#
#
# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = {'title', 'price', 'description'}

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Collection


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["title", "price", "description", "inventory_status", "collection"]
    list_per_page = 10
    list_editable = ["price", "description"]
    search_fields = ['title']

    @admin.display(ordering='-inventory')
    def inventory_status(self, product: Product):
        if product.inventory <= 20:
            return "Low Inventory"
        return 'Ok'


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["id", "title", "product_count"]
    list_per_page = 10
    # list_editable = ["id", "title"]
    search_fields = ['title']

    @admin.display(ordering='-title')
    def product_count(self, collection: Collection):
        return collection.product_set.count()
