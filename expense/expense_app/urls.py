from django.urls import path
from . import views
app_name = 'expense_app'

urlpatterns = [
    path('', views.AddExpense, name = 'expense'),
    path('cat/', views.AddExpCat, name = 'expensecat'),
    path('daily/', views.DailyExpenseReport, name = 'dailyexpenseanalysis'),
    path('monthly/', views.MonthlyExpenseReport, name = 'monthlyexpenseanalysis'),
    path('daterange/', views.ExpenseReportDateRange, name = 'daterangeexpenseanalysis'),
    path('weekly/', views.WeeklyExpenseReport, name = 'weeklyexpenseanalysis'),
    path('report/', views.PerformanceReport, name = 'performancereport'),
    path('delcat/', views.DelExpenseCat, name = 'deletecat'),
    path('editdelexp/', views.EditDelExpensedata, name = 'editdeleteexp'),
    path('editdelexp/delete/<int:pk>/', views.DeleteExpense, name = 'delete'),
    path('editdelexp/edit/<int:pk>/', views.EditExpense, name = 'edit'),
    path('chart/', views.Chart, name = 'chart'),
]
