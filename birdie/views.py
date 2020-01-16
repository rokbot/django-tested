from django.views.generic import TemplateView, UpdateView, View
from django.http import Http404
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models
from . import forms

import stripe


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


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        charge = stripe.Charge.create(
            amount=100,
            currency='sgd',
            description='',
            token=request.POST.get('token'),
        )
        send_mail(
            'Payment recived',
            'Charge {} succeeded!'.format(charge['id']),
            'server@example.com',
            ['admin@example.com', ],
        )
        return redirect('/')