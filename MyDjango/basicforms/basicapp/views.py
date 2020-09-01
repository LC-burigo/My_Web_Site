from django.shortcuts import render
from basicapp.forms import FormsName


def index(request):
    return render(request, 'basicapp/index.html')


def go_to(request):
    return render(request, 'basicapp/Go_to_form_page.html')


def form_name_view(request):
    form = FormsName()

    if request.method == 'POST':
        form = FormsName(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR FROM INVALID')

    return render(request, 'basicapp/form_page.html', {'form': form})
