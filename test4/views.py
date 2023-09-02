from django.shortcuts import render


# Create your views here.


def test4(requetst):
    d=33
    return render(requetst, 'test4/test4.html')
