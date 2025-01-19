from django.contrib import admin
from .models import Budget, Expense, Revenue, Category

# Enregistrez les modèles ici
admin.site.register(Budget)
admin.site.register(Expense)
admin.site.register(Revenue)
admin.site.register(Category)