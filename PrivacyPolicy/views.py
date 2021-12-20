from django.shortcuts import render


def policy(request):
    privacy = []
    return render(request, 'privacy_docs.html', {'privacy': privacy})
