import json

from pytz import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EventsForm
from .models import Events
from seldon.settings import TIME_ZONE


def events_list(request):
    events = Events.objects.all()
    if not events:
        events = []
    return render(request, 'events/events_list.html', {'events_list': events})


@login_required(login_url='login')
def events_edit(request, event):
    edit_event = get_object_or_404(Events, pk=event)
    if request.method == "POST":
        form = EventsForm(request.POST, instance=edit_event)
        if form.is_valid():
            edit_event = form.save(commit=False)
            edit_event.save()
            return redirect('events_list')
    else:
        edit_event.date = edit_event.date.astimezone(timezone(TIME_ZONE)).isoformat()[:-6]
        form = EventsForm(instance=edit_event)
    return render(request, 'events/event_edit.html', {'form': form})


@login_required(login_url='login')
def events_create(request):
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('events_list')
    else:
        form = EventsForm()
    return render(request, 'events/event_create.html', {'form': form})


def calendar(request):
    events = Events.objects.all()
    r = {}
    for event in events:
        print(event)
        print(event.date.year)
        print(event.date.month)
        print(event.date.day)
        r[event.date.day] = event.subject
    # j = json.dumps({"12": "sdf", "13": "sdf"})
    print(r)
    j = json.dumps(r)
    print(j.replace('"', '\\"'))
    return render(request, 'events/calendar.html', {'datata': j})