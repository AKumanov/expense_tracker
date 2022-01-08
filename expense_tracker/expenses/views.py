from django.shortcuts import render, redirect

from core.common import get_profile
from expense_tracker.expenses.forms import ExpenseForm, CreateExpense, EditExpense, DeleteExpense
from expense_tracker.expenses.models import Expense


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)
    context = {
        'expenses': expenses,
        'budget': budget,
        'budget_left': budget_left
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpense(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpense()
        context = {
            'form': form,
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpense(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditExpense(instance=expense)
        context = {
            'form': form,
            'expense': expense,
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('home')
    else:
        form = DeleteExpense(instance=expense)
        context = {
            'form': form,
            'expense': expense
        }
        return render(request, 'expense-delete.html', context)