from django.shortcuts import render, redirect

# Create your views here.
from core.common import get_profile
from expense_tracker.expenses.models import Expense
from expense_tracker.profiles.forms import CreateProfile, EditProfile, DeleteProfile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfile()
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def profile_detail(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'budget_left': budget_left
    }

    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfile(request.POST, instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home')
    else:
        form = DeleteProfile(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'profile-delete.html', context)