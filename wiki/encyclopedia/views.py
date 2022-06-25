from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": sorted(util.list_entries())
    })

def entry(request, title):
    tmp, title = title, util.get_entry(title)
    if not title:
        return render(request, "encyclopedia/error.html", {'title': tmp})
    return render(request, "encyclopedia/entry.html", {
        'title': tmp,
        'description': title.split()[2:] 
    })

