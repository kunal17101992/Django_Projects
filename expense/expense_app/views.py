from django.shortcuts import render,redirect
from .models import expense, expense_cat
from .forms import expenseForm, expenseCatForm, DateRangeForm, DelCatForm
from django.views.generic import CreateView
import datetime
from django.db.models import Sum


def month_last_day(dateinput):
    fsd = datetime.date(dateinput.year, dateinput.month, 1)
    tt = fsd + datetime.timedelta(days=32)
    tt1 = datetime.date(tt.year,tt.month, 1)
    lsd = tt1 - datetime.timedelta(days=1)

    return lsd


def index(request):
    td = datetime.date.today()
    msd = datetime.date(td.year,td.month,1)
    exp1 = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).values('Expense_date').annotate(daily_amount=Sum('Amount'))
    exp_sum = []
    a = {}
    for i in expense_cat.objects.all():
        b = i.expense_set.aggregate(Sum('Amount'))
        b['cat'] = i.name
        exp_sum.append(b)

    for y in exp_sum:
        if y['Amount__sum'] is None:
            y['Amount__sum'] = 0

    td = datetime.date.today()
    fd = datetime.date(td.year,td.month,1)
    ld = month_last_day(td)
    exp = []
    while fd <= td:
        find = False
        x = exp1.filter(Expense_date = fd)
        for i in x:
            exp.append(i)
            find = True
        if not find:
            exp.append({'Expense_date':fd,'daily_amount':0})
        fd = fd + datetime.timedelta(days=1)

    currmonth = []
    fd = datetime.date(td.year,td.month,1)
    while fd <= ld:
        currmonth.append(fd)
        fd = fd + datetime.timedelta(days=1)

    return render(request, 'expense_app/index.html', {'exp':exp,'exp_sum':exp_sum,'currmonth':currmonth})


def AddExpense(request):
    msg = ''
    if request.method == 'POST':
        form = expenseForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Expense added Successfully'
    form = expenseForm()
    return render(request, 'expense_app/expense.html', {'form':form, 'msg':msg})

def AddExpCat(request):
    msg = ''
    if request.method == 'POST':
        form = expenseCatForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Expense category added Successfully'
    form = expenseCatForm()
    return render(request, 'expense_app/expensecat.html', {'form':form, 'msg':msg})

def ExpenseReportDateRange(request):
    status = "Total"
    form = DateRangeForm()
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        sd = request.POST.get('Start_Date')
        ed = request.POST.get('End_Date')
        if form.is_valid():
            exp = expense.objects.filter(Expense_date__gte = sd, Expense_date__lte = ed).order_by('-Expense_date')
            exp_sum = expense.objects.filter(Expense_date__gte = sd, Expense_date__lte = ed).values('Expense_category__name').annotate(Sum('Amount'))
            sum = exp.aggregate(Sum('Amount'))
            return render(request, 'expense_app/daterange.html', {'exp':exp,'sum':sum, 'form':form,'status':status,'exp_sum':exp_sum})

    return render(request, 'expense_app/daterange.html', {'form':form})



def DailyExpenseReport(request):

    status = "Today's"
    exp = expense.objects.filter(Expense_date = datetime.date.today())
    exp_sum = exp.values('Expense_category__name').annotate(Sum('Amount'))

    sum = exp.aggregate(Sum('Amount'))
    return render(request, 'expense_app/daily.html', {'exp':exp,'sum':sum,'exp_sum':exp_sum,'status':status})


def MonthlyExpenseReport(request):

    status = 'Monthly'
    td = datetime.date.today()
    msd = datetime.date(td.year,td.month,1)
    exp = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).order_by('-Expense_date')
    exp_sum = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).values('Expense_category__name').annotate(Sum('Amount'))
    sum = exp.aggregate(Sum('Amount'))
    return render(request, 'expense_app/daily.html', {'exp':exp,'sum':sum,'exp_sum':exp_sum,'status':status})

def WeeklyExpenseReport(request):

    status = 'Weekly'
    td = datetime.date.today()
    n = td.weekday()
    print(n)
    msd = td - datetime.timedelta(days=n)
    print(msd)
    exp = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).order_by('-Expense_date')
    exp_sum = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).values('Expense_category__name').annotate(Sum('Amount'))

    sum = exp.aggregate(Sum('Amount'))
    return render(request, 'expense_app/daily.html', {'exp':exp,'sum':sum,'exp_sum':exp_sum,'status':status})

def PerformanceReport(request):
    exp1 = expense.objects.values('Expense_date__year','Expense_date__month').annotate(month_amt = Sum('Amount'))
    exp2 = expense.objects.values('Expense_category__name').annotate(cat_amt = Sum('Amount'))
    n = len(exp1)
    if n>5:
        n = 5
    exp = exp1.order_by('-month_amt')[:n]
    exp_cat = exp2.order_by('-cat_amt')[:7]

    a1 = expense.objects.values('Expense_category__name','Expense_date__year','Expense_date__month').annotate(Sum('Amount'))
    a = a1.order_by('Expense_date__year','Expense_date__month')
    b = expense.objects.order_by().values('Expense_date__year','Expense_date__month').distinct()
    print(a)
    print(b)
    return render(request, 'expense_app/performance.html', {'exp':exp,'exp_cat':exp_cat, 'a':a, 'b':b})


def DelExpenseCat(request):
    msg = ''
    if request.method == 'POST':
        form = DelCatForm(request.POST)
        val = request.POST.get('Category')
        if form.is_valid():
            a = expense_cat.objects.filter(id = val)
            a.delete()
            msg = 'success'

    form = DelCatForm()
    return render(request, 'expense_app/delcat.html', {'form':form,'msg':msg})


def EditDelExpensedata(request):
    status = 'Monthly'
    td = datetime.date.today()
    msd = datetime.date(td.year,td.month,1)
    exp = expense.objects.filter(Expense_date__gte = msd, Expense_date__lte = td).order_by('-Expense_date')
    sum = exp.aggregate(Sum('Amount'))
    return render(request, 'expense_app/delexp.html', {'exp':exp,'sum':sum,'status':status})


def DeleteExpense(request,pk):
    a = expense.objects.get(pk=pk)
    a.delete()
    return redirect('expense_app:editdeleteexp')

def EditExpense(request,pk):
    msg =''
    a = expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = expenseForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            msg = 'Expense updated Successfully!!'
    else:
        form = expenseForm(instance=a)
    return render(request,'expense_app/update.html', {'form':form, 'msg':msg})


def Chart(request):
    exp1 = expense.objects.values('Expense_date').annotate(daily_amount=Sum('Amount'))
    exp = exp1.order_by('Expense_date')
    print(exp)
    return render(request, 'expense_app/chart.html', {'exp':exp})
