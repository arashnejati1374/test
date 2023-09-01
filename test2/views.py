from django.shortcuts import render


def test2(requst):
    return render(requst, 'test2/test2.html')
