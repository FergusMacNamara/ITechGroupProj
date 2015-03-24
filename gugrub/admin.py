from django.contrib import admin
from gugrub.models import Eatery, Review

class EateryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Eatery, EateryAdmin)
admin.site.register(Review)
