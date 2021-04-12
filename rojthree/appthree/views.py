from django.shortcuts import render
from .forms import NewUserForm

def index(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'appthree/index.html',{'form':form})

#def help(request):
#    helpdict = {'help_insert':'HELP PAGE'}
#    return render(request,'appTwo/help.html',context=helpdict)

#def users(request):
    
# Create your views here.

