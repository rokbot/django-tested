from django.views.generic import TemplateView, UpdateView
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models
from . import forms


class HomeView(TemplateView):
    template_name = 'biridie/home.html'


class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kargs):
        # import ipdb; ipdb.set_trace()  # BREAKPOINT
        return super(AdminView, self).dispatch(request, *args, **kargs)


class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'birdie/update.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'Martin':
            raise Http404()
        return super(PostUpdateView, self).post(request, *args, **kwargs)
