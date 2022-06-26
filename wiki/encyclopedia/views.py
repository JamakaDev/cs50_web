from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    });

def entry(request, title):
    if request.method == 'POST':
        query_list, entries =  [], util.list_entries()
        query = request.POST['q'].upper()
        if query:
            for que in entries:
                info = util.get_entry(que)
                if query in info.upper():
                    query_list.append(info.split()[2])
            return render(request, "encyclopedia/entry.html", {
                'title': 'Query Search',
                'description': query_list,
            });
    tmp, title = title, util.get_entry(title)
    if not title:
        return render(request, "encyclopedia/error.html", {'title': tmp})
    return render(request, "encyclopedia/entry.html", {
        'title': tmp,
        'description': title.split()[3:] 
    })

