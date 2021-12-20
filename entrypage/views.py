from django.shortcuts import render


def entry(request):
    main = []
    return render(request, 'entrypage.html', {'entrypg': main})
