from django.shortcuts import render
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeletionMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import IntegrityError, transaction
from django.db.models import Prefetch, Count, Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ratelimit.decorators import ratelimit
from adminportal.models import *
from datetime import date, datetime
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.db import IntegrityError
from . models import *
from studentportal.models import documentRequest
from . forms import *


User = get_user_model()


def validate_latestSchoolYear(sy):
    # Return true if school year is ongoing/latest
    try:
        return date.today() <= sy.until
    except Exception as e:
        print(e)
        return False


def registrar_only(user):
    return user.is_registrar


@method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(registrar_only, login_url="studentportal:index")], name="dispatch")
class registrarDashboard(TemplateView):
    template_name = "registrarportal/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboard"
        return context


@method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(registrar_only, login_url="studentportal:index")], name="dispatch")
class getList_documentRequest(ListView, DeletionMixin):
    allow_empty = True
    context_object_name = "listOfDocumentRequests"
    http_method_names = ["get", "post"]
    paginate_by = 35
    template_name = "registrarPortal/documentRequests/listOfDocumentRequests.html"
    success_url = "/Registrar/RequestDocuments/"

    def delete(self, request, *args, **kwargs):
        try:
            self.cancel_this_request.is_cancelledByRegistrar = True
            self.cancel_this_request.save()
        except Exception as e:
            messages.warning(request, "Error.")
        return HttpResponseRedirect(self.success_url)

    def get_queryset(self):
        return documentRequest.registrarObjects.values("id", "document__documentName", "request_by__display_name", "scheduled_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Document Requests"
        return context

    def dispatch(self, request, *args, **kwargs):
        if ("pk" in request.POST) and request.method == "POST":
            self.cancel_this_request = documentRequest.registrarObjects.filter(
                id=int(request.POST["pk"])).first()
        return super().dispatch(request, *args, **kwargs)


@method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(registrar_only, login_url="studentportal:index")], name="dispatch")
class view_schoolYears(ListView):
    allow_empty = True
    context_object_name = "listOfSchoolYear"
    http_method_names = ["get"]
    paginate_by = 1
    template_name = "registrarPortal/schoolyear/listOfSchoolYear.html"

    def get_queryset(self):
        return schoolYear.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "School Years"
        return context


@method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(registrar_only, login_url="studentportal:index")], name="dispatch")
class add_schoolYear(FormView):
    form_class = add_schoolyear_form
    http_method_names = ["get", "post"]
    template_name = "registrarportal/schoolyear/addSchoolYear.html"

    # For revision, redirect user to enrollment and admission scheduling
    success_url = "/Registrar/schoolyear/"

    def form_valid(self, form):
        try:
            start_on = form.cleaned_data["start_on"]
            until = form.cleaned_data["until"]

            if start_on < until:
                self.new_sy = schoolYear.objects.create(
                    start_on=start_on, until=until)
                messages.success(
                    self.request, f"SY: {self.new_sy.display_sy()} is created.")
            else:
                messages.warning(self.request, "Invalid Period. Try again.")
                return self.form_invalid(form)

        except Exception as e:
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.get_sy = schoolYear.objects.first()
        if self.get_sy and not validate_latestSchoolYear(self.get_sy):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("registrarportal:schoolyear"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add School Year"
        return context
