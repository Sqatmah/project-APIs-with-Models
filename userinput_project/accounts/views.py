from django.shortcuts import render,redirect
from .forms import UserDataForm
from .models import UserData
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


##FORM VIEW
#  
def form_view(request):
    form = UserDataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'accounts/form_view.html', {'form': form})


## FUNCTION BASED VIEW ( FBV )
def function_view(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     UserData.objects.create(name=name, email=email)
    return redirect('user_list')
    return render(request, 'accounts/function_view.html')


## CLASS BASED VIEW ( CBV )

class ClassBasedView(View):
    def get(self, request):
        form = UserDataForm()
        return render(request, 'accounts/class_view.html', {'form': form})
    
    def post(self, request):
        form = UserDataForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('user_list')
        return render(request, 'accounts/class_view.html', {'form': form})
    

## GENERIC VIEW 

class GenericCreateView(CreateView):
     model = UserData
     form_class = UserDataForm
     template_name = 'accounts/generic_view.html'
     success_url = reverse_lazy('user_list')


## Showing User Results /present
def user_list(request):
    users = UserData.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})        