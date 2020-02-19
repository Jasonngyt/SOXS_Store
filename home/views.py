from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')
    
    
def faq(request):
    return render(request, 'home/FAQ.html')
    
    
def privacy(request):
    return render(request, 'home/Privacy_Policy.html')


def tnc(request):
    return render(request, 'home/Terms_n_Conditions.html')
    
    
def return_policy(request):
    return render(request, 'home/Return_n_Refund.html')


def about(request):
    return render(request, 'home/about.html')