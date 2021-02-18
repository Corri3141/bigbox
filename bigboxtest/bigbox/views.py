from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Box, Activity
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BoxListView(ListView):
    model = Box

def box_detail_view(request, id):
    box = get_object_or_404(Box, pk=id)
    activities = box.activities.all()[:5]

    context = {
        "box" : box,
        "activities":activities,
    }
    return render(request, "bigbox/box_detail.html", context)


def activities_view(request, id):
    box = get_object_or_404(Box, pk=id)
    activities_list = box.activities.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(activities_list, 20)
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        activities = paginator.page(1)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
        
    context = {
        "activities":activities,
        "box":box,
    }
    return render(request, "bigbox/activities.html", context)

def detail_activity_view(request, box_id,id):
    box = Box.objects.get(id=box_id)
    activity = box.activities.get(id=id)
    context = {
        "activity":activity,
        "reasons":activity.reasons.all(),
    }
    return render(request, "bigbox/activity.html", context)


# Create your views here.
