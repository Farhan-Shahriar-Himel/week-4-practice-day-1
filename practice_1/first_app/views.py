from django.shortcuts import render
from first_app.form import StudentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        std = StudentForm(request.POST)
        if std.is_valid():
            print(std.cleaned_data)
    else:
        std = StudentForm()
    return render(request, 'home.html', {'form': std})