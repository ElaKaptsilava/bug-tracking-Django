from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.views.decorators.http import require_http_methods

from .models import Bug


@require_http_methods(["GET"])
def bug(request):
    user_id = request.GET.get('user_id', False)
    project_id = request.GET.get('project_id', False)
    if user_id and project_id:
        get_bug = get_list_or_404(Bug, user=user_id, project=project_id)
        json_bug_obj = serialize("json", get_bug, fields=('project', 'user', 'description'))
        return HttpResponse(json_bug_obj, content_type="application/json")
    elif user_id and project_id is False:
        get_bug = get_list_or_404(Bug, user=user_id)
        json_bug_obj = serialize("json", get_bug, fields=('project', 'user', 'description'))
        return HttpResponse(json_bug_obj, content_type="application/json")
    elif project_id and user_id is False:
        get_bug = get_list_or_404(Bug, project=project_id)
        json_bug_obj = serialize("json", get_bug, fields=('project', 'user', 'description'))
        return HttpResponse(json_bug_obj, content_type="application/json")
