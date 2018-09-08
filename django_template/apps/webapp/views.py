from django.http.response import HttpResponse


def test(request):
    return HttpResponse('this is webapp test')