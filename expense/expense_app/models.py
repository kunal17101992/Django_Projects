from django.db import models

# Create your models here.
class expense_cat(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class expense(models.Model):
    Expense_category = models.ForeignKey(expense_cat, on_delete=models.CASCADE)
    Expense_name = models.CharField(max_length = 200)
    Expense_description = models.TextField(null=True,blank=True)
    Amount = models.PositiveIntegerField()
    Expense_date = models.DateField()

    def __str__(self):
        return self.Expense_name
