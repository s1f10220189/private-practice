from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # 保存後に一覧画面にリダイレクト
    else:
        form = ExpenseForm()
    return render(request, 'budget/add_expense.html')

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'budget/expense_list.html', {'expenses': expenses})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'budget/edit_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'budget/expense_confirm_delete.html', {'expense': expense})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense_list')  # サインアップ後、支出一覧にリダイレクト
    else:
        form = UserCreationForm()
    
    return render(request, 'budget/signup.html', {'form': form})

# ログイン後に表示する支出一覧画面
@login_required
def expense_list(request):
    # 支出一覧を取得して表示
    expenses = Expense.objects.all()
    return render(request, 'budget/expense_list.html', {'expenses': expenses})