from django.shortcuts import render
from . import forms


def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'Thank you we have received your information.'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'Welcome. Please complete the following form.'
    return render(request, 'signup.html', {'html': html, 'form': form})
