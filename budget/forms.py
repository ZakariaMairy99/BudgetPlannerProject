from django import forms
from .models import Budget, Expense, Revenue

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'total_budget', 'start_date', 'end_date']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'category', 'budget']

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['name', 'amount', 'date', 'budget']