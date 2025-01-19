from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ex: Marketing, Salaires
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=100)  # Ex: Budget 2023
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)  # Budget total
    start_date = models.DateField()  # Date de début du budget
    end_date = models.DateField()  # Date de fin du budget

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)  # Ex: Achat de matériel
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la dépense
    date = models.DateField()  # Date de la dépense
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Catégorie de la dépense
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)  # Budget associé

    def __str__(self):
        return f"{self.name} - {self.amount}"

class Revenue(models.Model):
    name = models.CharField(max_length=100)  # Ex: Vente de produits
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Montant du revenu
    date = models.DateField()  # Date du revenu
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)  # Budget associé

    def __str__(self):
        return f"{self.name} - {self.amount}"