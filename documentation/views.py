from django.shortcuts import render, HttpResponse


def home(request):
    documentation = []
    return render(request, 'doc_home.html', {'documentation': documentation})


def faq(request):
    questions = []
    return render(request, 'faq.html', {'questions': questions})


def policy(request):
    our_policy = []
    return render(request, 'policy.html', {'our_policy': our_policy})


def feature(request):
    features = []
    return render(request, 'features.html', {'features': features})
