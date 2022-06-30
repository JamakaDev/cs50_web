from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import util
from markdown2 import markdown as md
from random import choice

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
                    query_list.append(que)
            return render(request, "encyclopedia/entry.html", {
                'title': 'Query Search',
                'description': query_list,
            });
    tmp, title = title, util.get_entry(title)
    if not title:
        return render(request, "encyclopedia/error.html", {'title': tmp, 'entry': None})
    return render(request, "encyclopedia/entry.html", {
        'title': tmp,
        'description': md(title)
    })

def create(request):
    if request.method == "POST":
        title = request.POST['new_title'].capitalize()
        description = request.POST['new_entry']
        if title in util.list_entries() or title in ('Css',"Html"): 
            return render(request, 'encyclopedia/error.html', {
                'title': None,
                'entry': title
            })
        with open(f'/home/jamakadev/Desktop/CS50_WEB/cs50_web/wiki/entries/{title}.md', 'w') as file:
            file.write(f'# {title}\n\n')
            file.write(description)
            return redirect(f"/wiki/{title}", title=title)
    return render(request, 'encyclopedia/create.html')

def random(request):
    url = choice(util.list_entries())
    return redirect(f'wiki/{url}')

def edit(request, name=None):
    if request.method == 'POST':
        title = request.POST['new_title']
        description = request.POST['edit_entry'].split()[2:]
        
        with open(f'/home/jamakadev/Desktop/CS50_WEB/cs50_web/wiki/entries/{title}.md', 'w') as file:
            file.write(f'# {title}\n\n')
            file.write(' '.join(description))
            return redirect(f"/wiki/{title}", title=title)
    if not name: return render(request, "encyclopedia/error.html", {'title': 'Invalid', 'entry': None})
    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "info": util.get_entry(name),
    })

