from django import forms
from .models import expense, expense_cat

class DateInput(forms.DateInput):
    input_type = 'date'

class expenseForm(forms.ModelForm):

    class Meta:
        model = expense
        fields = '__all__'
        widgets = {'Expense_date':DateInput()}

class expenseCatForm(forms.ModelForm):

    class Meta:
        model = expense_cat
        fields = '__all__'


class DateRangeForm(forms.Form):
    Start_Date = forms.DateField(widget = DateInput())
    End_Date = forms.DateField(widget = DateInput())


    def clean(self):
        cleaned_data = super().clean()
        std = cleaned_data['Start_Date']
        etd = cleaned_data['End_Date']

        if std > etd:
            raise forms.ValidationError("Start date cannot be greater than end date")

class DelCatForm(forms.Form):
    Category = forms.ModelChoiceField(queryset=expense_cat.objects.all())
