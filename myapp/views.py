# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("hello world raka")


def raka_name(request):
    return HttpResponse("Rakesh Kumar sah")


def test(request):
    return render(request, "test.html")


def pass_value_dynamically(request):
    return render(request, "pass_value_runtime.html", {"value_raka": "Kumar Gupta"})


def youtube(request):
    return render(request, "you_tube_test.html")


def raka_fb_link(request):
    return render(request, "Facebook_Raka_Test.html",
                  {"value_raka": "Kumar Gupta", "fb_url_link": "https://www.facebook.com/"})


def sample_page(request):
    # after submit, calling new html file (submit_output html)
    return render(request, "sample_test.html")


def submit_name_anything(request):
    # after submit, calling new html file (submit_output html)
    return render(request, "submit_output.html")


def add_number(request):
    return render(request, "addition.html")


def add_result(request):
    a = int(request.GET["text1"])
    b = int(request.GET["text2"])
    res = a + b
    return render(request, "addition_result.html", {"result": res})


def login(request):
    return render(request, "login.html")
