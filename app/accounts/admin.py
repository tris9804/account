from django.contrib import admin

from .models import AccountBook, Category, Consume, Proportion


admin.site.register(AccountBook)
admin.site.register(Category)
admin.site.register(Consume)
admin.site.register(Proportion)