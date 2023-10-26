from django.shortcuts import render

# Create your views here.
def contacts_index(request):
    return render(request, 'main/contacts.html')


def home_index(request):
    return render(request, 'main/home.html')
