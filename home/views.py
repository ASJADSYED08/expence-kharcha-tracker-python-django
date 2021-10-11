from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home(request):
    profile = Profile.objects.filter(user=request.user).first()
    expenses = Expense.objects.filter(user=request.user)
    if request.method == "POST":
        text=request.POST.get("text")
        amount=request.POST.get("amount")
        exp_type=request.POST.get("exp_type")

        expense=Expense(name=text , amount=amount , expense_type=exp_type , user=request.user)
        expense.save()

        if exp_type =="Positive":
            profile.balance += float(amount)
        else:
            profile.balance -= float(amount)
            profile.expenses += float(amount)

        profile.save()
        return redirect('/')

    context = {'profile' : profile , 'expenses' : expenses}
    return render(request,'home.html',context)
           