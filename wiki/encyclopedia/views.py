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
                    query_list.append(info.split()[2])
            return render(request, "encyclopedia/entry.html", {
                'title': 'Query Search',
                'description': query_list,
            });
    tmp, title = title, util.get_entry(title)
    if not title:
        return render(request, "encyclopedia/error.html", {'title': tmp, 'entry': None})
    return render(request, "encyclopedia/entry.html", {
        'title': tmp,
        'description': ' '.join(title.split()[2:])
    })

def create(request):
    if request.method == "POST":
        title = request.POST['new_title'].capitalize()
        description = request.POST['new_entry']
        if title in util.list_entries() or title == 'Css': 
            return render(request, 'encyclopedia/error.html', {
                'title': None,
                'entry': title
            })
        with open(f'/home/jamakadev/Desktop/CS50_WEB/cs50_web/wiki/entries/{title}.md', 'w') as file:
            file.write(md(f'# {title}\n\n'))
            file.write(md(description))
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "description": description
        })
    return render(request, 'encyclopedia/create.html')

def random(request):
    url = choice(util.list_entries())
    return redirect(f'wiki/{url}')