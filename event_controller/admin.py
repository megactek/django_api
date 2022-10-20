from django.contrib import admin
from .models import EventMain, EvenFeature, EventAttender, Dog
# Register your models here.


admin.site.register((EventMain, EvenFeature, EventAttender, Dog))