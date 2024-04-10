from django.shortcuts import render


# Create your views here.
def index(requset):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(requset, 'main/index.html', data)


def about(requset):
    return render(requset, 'main/about.html')
