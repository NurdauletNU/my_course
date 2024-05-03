from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_app import utils, models


@utils.Decorators.constr_def_logger(is_class=False)
def index_http(request):
    return HttpResponse("Hello, world. You're at the django_app index.")


@utils.Decorators.constr_def_logger(is_class=False)
@utils.Decorators.dec_error_handle
def index_json(request):
    print(1 / 0)
    return JsonResponse(data={'message': "Hello, world"}, safe=False)


class Home(View):  # Mixins
    @utils.Decorators.constr_def_logger(is_class=True)
    def get(self, request, *args, **kwargs):
        _contacts = models.Contact.objects.filter(is_completed=True)
        context = {"contacts": _contacts}
        return render(request, "home.html", context=context)

    def post(self, request, *args, **kwargs):
        print('POST', request.POST)
        models.Contact.objects.create(
            username=request.POST['username'],
            position=None,
            number=request.POST['number'],
            description=request.POST.get('description', ''),
        )
        return redirect(reverse('home'))


def contact_delete(request, contact_id):
    models.Contact.objects.filter(id=int(contact_id)).delete()
    return redirect(reverse('home'))
