from django import forms

from expense_tracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class CreateExpense(ExpenseForm):
    pass


class EditExpense(ExpenseForm):
    pass


class DeleteExpense(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
