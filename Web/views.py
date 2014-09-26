from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum, Count
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import json
from django.utils import timezone
from Hajj import settings
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from Web.models import Activity, Action, ActionHistory, CampUser


def auth_user(request):
    if not request.user.is_authenticated():
        return render(request, 'hajj/login.html', {})
    return None


def index(request):
    ret = auth_user(request)
    if ret is None:
        if len(request.user.groups.all()) == 0:
            return render(request, 'hajj/login.html', {})
        if request.user.groups.all()[0].name == "QA Manager":
            return qa_view(request)
        elif request.user.groups.all()[0].name == "Camp Manager":
            return camp_view(request)
        elif request.user.groups.all()[0].name == "Executive Manager":
            return executive_view(request)
    return ret


def executive_view(request):
    ret = auth_user(request)
    if ret is None:
        # PREPARE DATA THAT NEEDS TO BE RENDER IN TEMPLATE
        user_id = 0
        now = settings.datetime.now()
        supervisor_list = Action.objects.all()\
            .filter(activity__start_date__lte=now, activity__end_date__gte=now)\
            .values('user_id').order_by('user_id')\
            .annotate(total=Count('status'), done=Sum('status'))

        row = []
        cols = []
        columns = 3
        for supervisor in supervisor_list:
            cu = CampUser.objects.get(user_id=supervisor["user_id"])
            cols.append({
                "camp": cu.camp.name,
                "camp_id": cu.camp_id,
                "count": int(supervisor["total"]) - supervisor["done"],
                "user": supervisor["user_id"]
            })
            if len(cols) % columns == 0:
                row.append(cols)
                cols = []
        if len(cols) > 0:
            row.append(cols)

        return render(request, 'hajj/officer.html', {"activities": {"user": request.user.username, "list": row}})
    return ret


def camp_view(request):
    ret = auth_user(request)
    if ret is None:
        # PREPARE DATA THAT NEEDS TO BE RENDER IN TEMPLATE
        camp = request.user.campuser_set.get(user_id=request.user.id)
        camp_users = CampUser.objects.all().filter(camp_id=camp.camp_id).exclude(user_id=camp.user_id)
        user_id = 0
        for cu in camp_users:
            user_id = cu.user_id
        now = settings.datetime.now()
        supervisor_list = Action.objects.all()\
            .filter(activity__start_date__lte=now, activity__end_date__gte=now)\
            .filter(user__id__exact=user_id)\
            .values('activity__supervisor').order_by('activity__supervisor')\
            .annotate(total=Count('status'), done=Sum('status'))

        row = []
        cols = []
        columns = 3
        for supervisor in supervisor_list:
            cols.append({
                "supervisor": supervisor["activity__supervisor"],
                "count": int(supervisor["total"]) - supervisor["done"],
                "user": user_id
            })
            if len(cols) % columns == 0:
                row.append(cols)
                cols = []
        if len(cols) > 0:
            row.append(cols)

        return render(request, 'hajj/manager.html', {"activities": {"user": request.user.username, "list": row}})
    return ret


def qa_view(request):
    ret = auth_user(request)
    if ret is None:
        # PREPARE DATA THAT NEEDS TO BE RENDER IN TEMPLATE
        now = settings.datetime.now()
        activity_list = Action.objects.all()\
            .filter(user__id__exact=request.user.id)\
            .filter(activity__start_date__lte=now, activity__end_date__gte=now)
        return render(request, 'hajj/qa.html', {"activities": {"list": activity_list, "user": request.user.username}})
    return ret


def sign_in(request):
    post_body = json.loads(request.body)
    username = post_body["username"]
    password = post_body['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if request.user.groups.all()[0].name == "QA Manager":
                return HttpResponse(json.dumps({"success": "qa"}), content_type="application/json")
            elif request.user.groups.all()[0].name == "Camp Manager":
                return HttpResponse(json.dumps({"success": "camp"}), content_type="application/json")
            elif request.user.groups.all()[0].name == "Executive Manager":
                return HttpResponse(json.dumps({"success": "executive"}), content_type="application/json")

    return HttpResponse(json.dumps({"error": "Invalid Credentials"}), content_type="application/json")


def sign_out(request):
    logout(request)
    return HttpResponse(json.dumps({"success": "Logged out"}), content_type="application/json")


def log_action(request, activity_id):
    post_body = json.loads(request.body)
    action = Action.objects.all()\
        .filter(activity__id__exact=activity_id, user__id__exact=request.user.id)
    for act in action:
        if "comment" in post_body:
            act.comment = post_body["comment"]
        if "status" in post_body:
            act.status = True
            if post_body["status"] == "False":
                act.status = False
        history = ActionHistory(status=act.status, comment=act.comment,
                                updated_at=timezone.now(), user=act.user, activity=act.activity)
        # UPDATE
        act.save()
        history.save()
    return HttpResponse(json.dumps({"success": "Saved!"}), content_type="application/json")


def supervisor_detail(request):
    post_body = json.loads(request.body)
    supervisor = post_body["supervisor"]
    user_id = post_body["user"]
    # PREPARE DATA THAT NEEDS TO BE RENDER IN TEMPLATE
    now = settings.datetime.now()
    activity_list = Action.objects.all()\
        .filter(user__id__exact=user_id, status=False)\
        .filter(activity__start_date__lte=now, activity__end_date__gte=now, activity__supervisor__exact=supervisor)
    template = render(request, 'hajj/supervisor.html', {"activities": {"list": activity_list, "s": supervisor}})
    return HttpResponse(json.dumps({"success": template.content}), content_type="application/json")


def camp_detail(request):
    post_body = json.loads(request.body)
    user_id = post_body["user"]
    camp_name = post_body["camp"]
    now = settings.datetime.now()
    supervisor_list = Action.objects.all()\
        .filter(activity__start_date__lte=now, activity__end_date__gte=now)\
        .filter(user__id__exact=user_id)\
        .values('activity__supervisor').order_by('activity__supervisor')\
        .annotate(total=Count('status'), done=Sum('status'))

    row = []
    cols = []
    columns = 3
    for supervisor in supervisor_list:
        cols.append({
            "supervisor": supervisor["activity__supervisor"],
            "count": int(supervisor["total"]) - supervisor["done"],
            "user": user_id
        })
        if len(cols) % columns == 0:
            row.append(cols)
            cols = []
    if len(cols) > 0:
        row.append(cols)
    template = render(request, 'hajj/camp.html', {"activities": {"list": row, "camp": camp_name}})
    return HttpResponse(json.dumps({"success": template.content}), content_type="application/json")