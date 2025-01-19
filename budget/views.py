from django.shortcuts import render
from .models import Budget, Expense, Revenue
from django.http import HttpResponse
from django.conf import settings
import os
from groq import Groq

def dashboard(request):
    budgets = Budget.objects.all()
    expenses = Expense.objects.all()
    revenues = Revenue.objects.all()

    # Calculer les totaux
    total_budget = sum(budget.total_budget for budget in budgets)
    total_expenses = sum(expense.amount for expense in expenses)
    total_revenues = sum(revenue.amount for revenue in revenues)

    context = {
        'budgets': budgets,
        'expenses': expenses,
        'revenues': revenues,
        'total_budget': total_budget,
        'total_expenses': total_expenses,
        'total_revenues': total_revenues,
    }
    return render(request, 'dashboard.html', context)

def index(request):
    return render(request, 'index.html')



# Initialize Groq client
client = Groq(api_key="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")

def call_groq_api(prompt):
    """Call the Groq API with a given prompt."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",  # Use the specific model you want
    )
    return chat_completion.choices[0].message.content

def chatbot(request):
    """Handle user queries and display the response."""
    result = ""
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if query:
            prompt = f"Question: {query}\nAnswer:"
            try:
                result = call_groq_api(prompt)
            except Exception as e:
                result = f"An error occurred: {e}"
    
    return render(request, 'chatbot.html', {'result': result})