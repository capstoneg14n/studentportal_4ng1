
# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class admission_and_enrollment(TemplateView):
#     # Used to create admission and enrollment form, then create the school year
#     # Add Features to check if the given dates are properly set, if not, then it should inform the user/admin
#     template_name = "adminportal/AdmissionAndEnrollment/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Enrollment and Admission"
#         try:
#             sy = school_year.objects.latest("date_created")
#             context["sy"] = sy.sy

#             if sy.setup_sy.start_date > date.today() and validate_enrollmentSetup(self.request, sy):
#                 # if school year is less than 209 days and setup form will start soon
#                 context["start_soon"] = True  # For update period button
#                 context["start_date"] = sy.setup_sy.start_date.strftime(
#                     "%A, %b %d, %Y")
#                 context["end_date"] = sy.setup_sy.end_date.strftime(
#                     "%A, %b %d, %Y")
#                 context["uid"] = urlsafe_base64_encode(
#                     force_bytes(sy.setup_sy.id))

#             elif sy.setup_sy.end_date >= date.today() and validate_enrollmentSetup(self.request, sy):
#                 # if school year is less than 209 days and setup form will end soon
#                 if sy.setup_sy.still_accepting:
#                     # if enrollment is not postpone
#                     context["is_empty_count"] = self.count_validation2(sy)
#                     context["count_sy_details"] = self.count_validation1(sy)
#                     context["is_extend"] = True  # extend period
#                     context["end_dt"] = sy.setup_sy.end_date.strftime(
#                         "%A, %b %d, %Y")

#                     # use to postpone enrollment
#                     context["stop_accepting"] = True
#                     context["uid"] = urlsafe_base64_encode(
#                         force_bytes(sy.setup_sy.id))

#                 else:
#                     # if enrollment is postpone
#                     context["is_empty_count"] = self.count_validation2(sy)
#                     context["count_sy_details"] = self.count_validation1(sy)
#                     context["stop_from_accepting"] = True
#                     context["is_extend"] = True  # extend period
#                     context["end_dt"] = sy.setup_sy.end_date.strftime(
#                         "%A, %b %d, %Y")
#                     context["uid"] = urlsafe_base64_encode(
#                         force_bytes(sy.setup_sy.id))

#             else:
#                 if sy.setup_sy.end_date <= date.today() and validate_enrollmentSetup(self.request, sy):
#                     # if school year is less than 209 days and setup form period has ended
#                     context["is_empty_count"] = self.count_validation2(sy)
#                     context["count_sy_details"] = self.count_validation1(sy)
#                     context["extend_notif"] = f"Enrollment and Admission for S.Y. {sy} have already ended."
#                     context["uid"] = urlsafe_base64_encode(
#                         force_bytes(sy.setup_sy.id))
#             if not validate_enrollmentSetup(self.request, sy):
#                 # If school year is greater than 209 days.
#                 context["new_enrollment"] = True

#         except Exception as e:
#             # if no school year
#             # if with school year but no setup form
#             # messages.error(self.request, e)
#             context["no_record"] = True
#         return context

#     def count_validation2(self, sy):
#         enrollment_count = Count(
#             "sy_enrolled", filter=Q(sy_enrolled__is_denied=False))
#         admission_count_sy = Count(
#             "sy_admitted", filter=Q(sy_admitted__is_denied=False))
#         count_if_exist = school_year.objects.filter(id=sy.id).annotate(
#             e_count=enrollment_count, a_count=admission_count_sy).first()

#         return False if count_if_exist.e_count or count_if_exist.a_count else True

#     def count_validation1(self, sy):
#         enrolled_count = Count(
#             "sy_enrolled", filter=Q(sy_enrolled__is_passed=True, sy_enrolled__is_denied=False))
#         pending_enrollment_count = Count(
#             "sy_enrolled", filter=Q(sy_enrolled__is_passed=False, sy_enrolled__is_denied=False))
#         admission_count = Count("sy_admitted", filter=Q(
#             sy_admitted__is_validated=True, sy_admitted__is_denied=False))  # For accepted
#         pending_admission_count = Count(
#             "sy_admitted", filter=Q(sy_admitted__is_validated=False, sy_admitted__is_denied=False))  # For pending but not denied

#         return school_year.objects.filter(id=sy.id).annotate(enrolled_students=enrolled_count, pending_enrollment=pending_enrollment_count, admitted_students=admission_count, pending_admission=pending_admission_count).first()


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class update_enrollment(FormView):
#     # If enrollment and admission will start soon
#     form_class = ea_setup_form
#     template_name = "adminportal/AdmissionAndEnrollment/update_enrollment.html"
#     success_url = "/School_admin/Admission_and_enrollment/"

#     def form_valid(self, form):
#         try:
#             if form.has_changed():
#                 start_date = form.cleaned_data["start_date"]
#                 end_date = form.cleaned_data["end_date"]
#                 if start_date < end_date:
#                     enrollment_admission_setup.objects.filter(id=self.convert_to_pk(
#                         self.kwargs["uid"])).update(start_date=start_date, end_date=end_date)
#                     messages.success(
#                         self.request, "Enrollment and Admission period is updated successfully.")
#                     return super().form_valid(form)
#                 else:
#                     messages.warning(
#                         self.request, "Dates are not valid! Try again.")
#                     return self.form_invalid(form)
#             else:
#                 return super().form_valid(form)
#         except Exception as e:
#             messages.error(self.request, e)
#             return super().form_valid(form)

#     def get_initial(self):
#         initial = super().get_initial()
#         get_obj = enrollment_admission_setup.objects.get(
#             id=self.convert_to_pk(self.kwargs["uid"]))
#         initial["start_date"] = get_obj.start_date
#         initial["end_date"] = get_obj.end_date
#         return initial

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             uid = self.convert_to_pk(self.kwargs["uid"])
#             get_obj = enrollment_admission_setup.objects.get(id=uid)
#             if validate_enrollmentSetup(request, get_obj.ea_setup_sy):
#                 if get_obj.start_date > date.today() and get_obj.end_date > date.today():
#                     return super().dispatch(request, *args, **kwargs)
#                 else:
#                     messages.warning(
#                         request, "Enrollment and Admission period are no longer valid.")
#                     return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#             else:
#                 messages.warning(request, "%s is no longer valid." %
#                                  get_obj.ea_setup_sy.sy)
#                 return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Update Date"
#         context["setup_details"] = enrollment_admission_setup.objects.values(
#             "ea_setup_sy__sy").get(id=self.convert_to_pk(self.kwargs["uid"]))
#         return context

#     def convert_to_pk(self, uid):
#         return force_str(urlsafe_base64_decode(uid))


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class extend_enrollment(FormView):
#     # for extend button
#     # still_accepting will set to True
#     form_class = extend_enrollment
#     success_url = "/School_admin/Admission_and_enrollment/"
#     template_name = "adminportal/AdmissionAndEnrollment/extend_enrollment.html"

#     def form_valid(self, form):
#         try:
#             if form.has_changed():
#                 end_date = form.cleaned_data["end_date"]
#                 if end_date > date.today():
#                     enrollment_admission_setup.objects.filter(id=self.convert_to_pk(
#                         self.kwargs["uid"])).update(end_date=end_date, still_accepting=True)
#                     get_enrollment = enrollment_admission_setup.objects.values(
#                         'end_date').get(id=self.convert_to_pk(self.kwargs["uid"]))
#                     messages.success(
#                         self.request, "Enrollment and Admission period is successfully extended until %s." % get_enrollment["end_date"].strftime("%A, %b %d, %Y"))
#                     return super().form_valid(form)
#                 else:
#                     messages.warning(
#                         self.request, "End date must be greater than date today.")
#                     return self.form_invalid(form)
#             else:
#                 get_obj = enrollment_admission_setup.objects.filter(
#                     id=self.convert_to_pk(self.kwargs["uid"])).first()
#                 if not get_obj.still_accepting:
#                     # if postpone
#                     get_obj.still_accepting = True
#                     get_obj.save()
#                     messages.success(
#                         self.request, "Enrollment and Admission is open again.")
#                     return super().form_valid(form)
#                 return super().form_valid(form)
#         except Exception as e:
#             messages.error(self.request, e)
#             return super().form_valid(form)

#     def get_initial(self):
#         initial = super().get_initial()
#         get_obj = enrollment_admission_setup.objects.get(
#             id=self.convert_to_pk(self.kwargs["uid"]))
#         initial["end_date"] = get_obj.end_date
#         return initial

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             get_obj = enrollment_admission_setup.objects.get(
#                 id=self.convert_to_pk(self.kwargs["uid"]))
#             if validate_enrollmentSetup(request, get_obj.ea_setup_sy):
#                 if get_obj.start_date <= date.today():
#                     return super().dispatch(request, *args, **kwargs)
#                 else:
#                     messages.warning(
#                         request, "You cannot extend the enrollment date using this function.")
#                     return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#             else:
#                 # if school year creation date is greater than 209 days
#                 messages.warning(request, "%s is no longer valid." %
#                                  get_obj.ea_setup_sy.sy)
#                 return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Extend Period"
#         context["school_year"] = enrollment_admission_setup.objects.values(
#             "ea_setup_sy__sy").get(id=self.convert_to_pk(self.kwargs["uid"]))
#         return context

#     def convert_to_pk(self, uid):
#         return force_str(urlsafe_base64_decode(uid))


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class postpone_enrollment(TemplateView):
#     template_name = "adminportal/AdmissionAndEnrollment/postpone_enrollment.html"

#     def post(self, request, *args, **kwargs):
#         try:
#             get_enrollment = enrollment_admission_setup.objects.get(
#                 id=self.convert_to_pk(self.kwargs["uid"]))
#             get_enrollment.still_accepting = False
#             get_enrollment.save()
#             messages.success(
#                 request, "Enrollment and Admission are now postponed.")
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             get_obj = enrollment_admission_setup.objects.get(
#                 id=self.convert_to_pk(self.kwargs["uid"]))

#             if validate_enrollmentSetup(request, get_obj.ea_setup_sy):
#                 if get_obj.start_date <= date.today() and get_obj.end_date >= date.today():
#                     if get_obj.still_accepting:
#                         return super().dispatch(request, *args, **kwargs)
#                     else:
#                         messages.warning(
#                             request, "Enrollment and Admission are already postponed.")
#                         return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#                 else:
#                     messages.warning(
#                         request, "Enrollment and Admission period should have already started and not yet finished.")
#                     return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#             else:
#                 messages.warning(request, "School year is no longer valid.")
#                 return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))

#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Postpone Enrollment"
#         context["sy"] = enrollment_admission_setup.objects.values(
#             'ea_setup_sy__sy').get(id=self.convert_to_pk(self.kwargs["uid"]))
#         return context

#     def convert_to_pk(self, uid):
#         return force_str(urlsafe_base64_decode(uid))


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class open_enrollment_admission(FormView):
#     template_name = "adminportal/AdmissionAndEnrollment/setup_enrollment.html"
#     form_class = ea_setup_form
#     success_url = "/School_admin/Admission_and_enrollment/"

#     def form_valid(self, form):
#         if form.has_changed():
#             start_date = form.cleaned_data["start_date"]
#             end_date = form.cleaned_data["end_date"]

#             if start_date < end_date:
#                 try:
#                     sy = school_year.objects.latest("date_created")
#                     if validate_enrollmentSetup(self.request, sy):
#                         obj_create_from_existing_obj = enrollment_admission_setup.objects.create(
#                             ea_setup_sy=sy,
#                             start_date=start_date,
#                             end_date=end_date,
#                         )
#                         messages.success(
#                             self.request, "Setup Form for S.Y. %s is created successfully." % sy.sy)
#                         return super().form_valid(form)
#                     else:
#                         obj_pure_create = enrollment_admission_setup.objects.create(
#                             ea_setup_sy=school_year.objects.get_or_create(
#                                 sy=compute_schoolyear(1)
#                             ),
#                             start_date=start_date,
#                             end_date=end_date,
#                         )
#                         messages.success(
#                             self.request, "Setup Form for S.Y. %s is created successfully." % obj_pure_create.ea_setup_sy.sy)
#                         return super().form_valid(form)
#                 except:
#                     try:
#                         obj_created = enrollment_admission_setup.objects.create(
#                             ea_setup_sy=school_year.objects.create(
#                                 sy=compute_schoolyear(1)),
#                             start_date=start_date,
#                             end_date=end_date,
#                         )
#                         messages.success(
#                             self.request, "S.Y. %s Enrollment and Admission Forms is created successfully." % obj_created.ea_setup_sy.sy)
#                         return super().form_valid(form)
#                     except Exception as e:
#                         messages.error(self.request, e)
#                         return self.form_invalid(form)
#             else:
#                 messages.warning(
#                     self.request, "Start date should be less than the End Date.")
#                 return self.form_invalid(form)
#         else:
#             messages.warning(self.request, "Fill all fields with valid data.")
#             return self.form_invalid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Setup Details"
#         context["sy"] = self.sy_display()
#         return context

#     def sy_display(self):
#         try:
#             sy_obj = school_year.objects.latest("date_created")
#             return sy_obj.sy if validate_enrollmentSetup(self.request, sy_obj) else compute_schoolyear(1)
#         except:
#             return compute_schoolyear(1)

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             sy = school_year.objects.latest("date_created")
#             if validate_enrollmentSetup(request, sy):
#                 # if school year is less than 209 days since its creation
#                 try:
#                     # If school_year has enrollment_admission_setup
#                     get_sy_objs = enrollment_admission_setup.objects.get(
#                         ea_setup_sy=sy)
#                     messages.warning(
#                         request, "You already have a setup form for S.Y. %s." % sy.sy)
#                     return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))
#                 except:
#                     if request.method == "GET":
#                         messages.warning(
#                             request, "S.Y. %s has no admission and enrollment setup form. Create Now." % sy.sy)
#                     return super().dispatch(request, *args, **kwargs)
#             else:
#                 # If school_year is greater than 209 days since its creation
#                 return super().dispatch(request, *args, **kwargs)
#         except:
#             # if there's no data in school_year table
#             return super().dispatch(request, *args, **kwargs)


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class adm_details(DetailView):
#     # Get the admission details of any admission status
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/adm_details.html"
#     context_object_name = "admissionDetails"
#     model = student_admission_details

#     # Add features to validate if an admission still qualified to be validated according to school year and current date

#     def post(self, request, *args, **kwargs):
#         try:
#             obj = student_admission_details.objects.filter(
#                 id=self.kwargs["pk"])
#             if "accept" in request.POST:
#                 # Accept admission
#                 # Add functions to validate if an admission is still qualified to be accepted. To qualify, the admission_sy.date_created should be less than 209 days
#                 redirect_link = self.where_to_redirect(obj)
#                 self.validate_obj(obj)
#                 return HttpResponseRedirect(redirect_link)

#             elif "pen_nxt_accept" in request.POST:
#                 # Accept enrollment and redirect to the next pending enrollment details
#                 nxt = self.get_next_pending_url(self.kwargs["pk"])
#                 self.validate_obj(obj)
#                 return HttpResponseRedirect(nxt)

#             elif "denied" in request.POST:
#                 # Denied enrollment with no comments
#                 nxt = self.where_to_redirect(obj)
#                 self.denied_obj(obj)
#                 return HttpResponseRedirect(nxt)

#             elif "submit_revs" in request.POST:
#                 # Denied enrollment and save comments
#                 comments = request.POST.get('review')
#                 if comments:
#                     next_link = self.where_to_redirect(obj)
#                     self.denied_obj(obj)
#                     self.add_comments(obj, comments)
#                     return HttpResponseRedirect(next_link)
#                 else:
#                     messages.warning(
#                         request, "Add a comment if you click the submit button for denied.")
#                     return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#             elif "pend_next_denied_with_revs" in request.POST:
#                 # Denied pending enrollment and save comments, then redirect to the next pending enrollment
#                 comments = request.POST.get('review')
#                 if comments:
#                     next_link = self.get_next_pending_url(self.kwargs["pk"])
#                     self.denied_obj(obj)
#                     self.add_comments(obj, comments)
#                     return HttpResponseRedirect(next_link)
#                 else:
#                     messages.warning(
#                         request, "Add a comment if you click the submit button for denied.")
#                     return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#             elif "hold" in request.POST:
#                 try:
#                     obj = obj.first()
#                     if obj.is_validated and not obj.is_denied:
#                         obj.is_denied = True
#                         obj.save()
#                         obj.refresh_from_db()
#                         messages.warning(
#                             request, "You hold the validated admission of Mr / Ms. %s" % obj.first_name)
#                         return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))
#                     else:
#                         messages.warning(
#                             request, "Admission can no longer be hold.")
#                         return HttpResponseRedirect(reverse("adminportal:admitted_students"))
#                 except Exception as e:
#                     messages.error(request, e)
#                     return HttpResponseRedirect(reverse("adminportal:admitted_students"))

#             elif "next_valid" in request.POST:
#                 nxt = self.get_next_valid_url(self.kwargs["pk"])
#                 return HttpResponseRedirect(nxt)

#             elif "rev_nxt_accept" in request.POST:
#                 # Accept from revision list, then next revision details
#                 self.validate_obj(obj)
#                 nxt = self.get_next_for_revision_url(self.kwargs["pk"])
#                 return HttpResponseRedirect(nxt)

#             elif "rev_next" in request.POST:
#                 nxt = self.get_next_for_revision_url(self.kwargs["pk"])
#                 return HttpResponseRedirect(nxt)

#             elif "nxt_denied" in request.POST:
#                 nxx = self.get_next_denied_url(self.kwargs["pk"])
#                 return HttpResponseRedirect(nxx)

#             elif "next_denied_with_revs" in request.POST:
#                 comments = request.POST.get('review')
#                 if comments:
#                     next_link = self.get_next_denied_url(self.kwargs["pk"])
#                     self.denied_obj(obj)
#                     self.add_comments(obj, comments)
#                     return HttpResponseRedirect(next_link)
#                 else:
#                     messages.warning(
#                         request, "Add a comment if you click the submit button for denied.")
#                     return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#             elif "to_pending" in request.POST:
#                 try:
#                     nxt = self.where_to_redirect(obj)
#                     obj = obj.first()
#                     obj.is_validated = False
#                     obj.is_denied = False
#                     obj.save()
#                     obj.refresh_from_db()
#                     messages.success(
#                         request, "%s admission is moved to pending." % obj.first_name)
#                     return HttpResponseRedirect(nxt)
#                 except Exception as e:
#                     messages.error(request, e)
#                     return HttpResponseRedirect(reverse("adminportal:hold_admissions"))

#             elif "hold_next_denied_with_revs" in request.POST:
#                 comments = request.POST.get("review")
#                 if comments:
#                     next_link = self.get_next_hold_url(self.kwargs["pk"])
#                     self.denied_obj(obj)
#                     self.add_comments(obj, comments)
#                     return HttpResponseRedirect(next_link)
#                 else:
#                     messages.warning(
#                         request, "Add a comment if you click the submit button for denied.")
#                     return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#             else:
#                 return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:details", kwargs={"pk": self.kwargs["pk"]}))

#     def add_comments(self, obj, comments):
#         obj = obj.first()
#         for_review_admission.objects.create(to_review=obj, comment=comments)

#     def denied_obj(self, obj):
#         obj = obj.first()
#         obj.is_validated = False
#         obj.is_denied = True
#         obj.save()

#     def validate_obj(self, obj):
#         obj = obj.first()
#         obj.is_validated = True
#         obj.is_denied = False
#         obj.save()
#         obj.refresh_from_db()

#     def get_next_hold_url(self, pk):
#         # Get the next url hold admission
#         try:
#             qs = student_admission_details.objects.values_list('id', flat=True).filter(
#                 is_validated=True, is_denied=True).order_by("admission_sy__sy", "date_modified", "id", "date_created")
#             if qs:
#                 try:
#                     qs_count = qs.count()
#                     tupl_to_list = list(qs)
#                     nxt_id = tupl_to_list.index(int(pk)) + 1
#                     nxx = tupl_to_list[nxt_id] if nxt_id < qs_count else tupl_to_list[0]
#                     return reverse("adminportal:details", kwargs={"pk": nxx})
#                 except ValueError:
#                     # if pk is not in the qs
#                     return reverse("adminportal:details", kwargs={"pk": tupl_to_list[0]})
#                 except Exception as e:
#                     messages.error(self.request, e)
#                     return reverse("adminportal:hold_admissions")
#             else:
#                 return reverse("adminportal:hold_admissions")
#         except Exception as e:
#             messages.error(self.request, e)
#             return reverse("adminportal:hold_admissions")

#     def get_next_denied_url(self, pk):
#         # Get the next url denied admission
#         try:
#             qs = student_admission_details.objects.values_list('id', flat=True).alias(count_reviews=Count("admission_review")).filter(
#                 count_reviews__lt=1, is_validated=False, is_denied=True).order_by("admission_sy__sy", "date_modified", "date_created", "id")
#             if qs:
#                 try:
#                     qs_count = qs.count()
#                     tupl_to_list = list(qs)
#                     nxt_id = tupl_to_list.index(int(pk)) + 1
#                     nxx = tupl_to_list[nxt_id] if nxt_id < qs_count else tupl_to_list[0]
#                     return reverse("adminportal:details", kwargs={"pk": nxx})
#                 except ValueError:
#                     # if pk is not in the qs
#                     return reverse("adminportal:details", kwargs={"pk": tupl_to_list[0]})
#                 except Exception as e:
#                     messages.error(self.request, e)
#                     return reverse("adminportal:denied_admissions")
#             else:
#                 return reverse("adminportal:denied_admissions")
#         except Exception as e:
#             messages.error(self.request, e)
#             return reverse("adminportal:denied_admissions")

#     def get_next_for_revision_url(self, pk):
#         # Get the next url for revision
#         try:
#             qs = student_admission_details.objects.values_list('id', flat=True).alias(count_reviews=Count("admission_review")).filter(
#                 count_reviews__gt=0, is_validated=False, is_denied=True).order_by("admission_sy__sy", "date_modified", "date_created", "id")
#             if qs:
#                 try:
#                     qs_count = qs.count()
#                     tupl_to_list = list(qs)
#                     nxt_id = tupl_to_list.index(int(pk)) + 1
#                     nxx = tupl_to_list[nxt_id] if nxt_id < qs_count else tupl_to_list[0]
#                     return reverse("adminportal:details", kwargs={"pk": nxx})
#                 except ValueError:
#                     # if pk is not in the qs
#                     return reverse("adminportal:details", kwargs={"pk": tupl_to_list[0]})
#                 except Exception as e:
#                     messages.error(self.request, e)
#                     return reverse("adminportal:forReviewAdmission")
#             else:
#                 return reverse("adminportal:forReviewAdmission")
#         except Exception as e:
#             messages.error(self.request, e)
#             return reverse("adminportal:forReviewAdmission")

#     def get_next_pending_url(self, pk):
#         # Get the next pending pk after the given pk using the same queryset
#         try:
#             sy = school_year.objects.latest("date_created")
#             qs = student_admission_details.objects.values_list("id", flat=True).filter(
#                 admission_sy=sy, is_validated=False, is_denied=False).order_by("date_modified", "date_created", "id")

#             if qs:
#                 try:
#                     qs_count = qs.count()
#                     tupl_to_list = list(qs)
#                     nxt_id = tupl_to_list.index(int(pk)) + 1
#                     nxx = tupl_to_list[nxt_id] if nxt_id < qs_count else tupl_to_list[0]
#                     return reverse("adminportal:details", kwargs={"pk": nxx})
#                 except ValueError:
#                     # If pk is no longer pending
#                     return reverse("adminportal:details", kwargs={"pk": tupl_to_list[0]})
#                 except:
#                     return reverse("adminportal:admission")
#             else:
#                 return reverse("adminportal:admission")
#         except Exception as e:
#             messages.error(self.request, e)
#             return reverse("adminportal:admission")

#     def get_next_valid_url(self, pk):
#         # Get the next valid pk after the given pk using the same queryset
#         try:
#             sy = school_year.objects.latest("date_created")
#             qs = student_admission_details.objects.values_list("id", flat=True).filter(
#                 admission_sy=sy, is_validated=True, is_denied=False).order_by("admission_sy__sy", "date_modified", "date_created", "id")

#             if qs:
#                 try:
#                     qs_count = qs.count()
#                     tupl_to_list = list(qs)
#                     nxt_id = tupl_to_list.index(int(pk)) + 1
#                     nxx = tupl_to_list[nxt_id] if nxt_id < qs_count else tupl_to_list[0]
#                     return reverse("adminportal:details", kwargs={"pk": nxx})
#                 except ValueError:
#                     # If pk is no longer pending or not in the retrieve queryset
#                     return reverse("adminportal:details", kwargs={"pk": tupl_to_list[0]})
#                 except:
#                     return reverse("adminportal:admitted_students")
#             else:
#                 return reverse("adminportal:admitted_students")
#         except Exception as e:
#             messages.error(self.request, e)
#             return reverse("adminportal:admitted_students")

#     def where_to_redirect(self, obj):
#         # If accept only
#         obj1 = obj.first()
#         if obj1.is_validated and obj1.is_denied:
#             # if hold
#             return obj1.to_holdList()
#         elif not obj1.is_validated and not obj1.is_denied:
#             # if pending
#             return obj1.to_pendingList()
#         elif not obj1.is_validated and obj1.is_denied:
#             # if denied
#             rev_obj = for_review_admission.objects.filter(
#                 to_review__id=obj1.id).count()
#             if rev_obj > 0:
#                 return obj1.to_reviewList()
#             else:
#                 return obj1.to_deniedList()
#         else:
#             return obj1.to_admittedList()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Admission Details"

#         adm_obj = student_admission_details.objects.filter(
#             id=self.kwargs["pk"]).first()

#         if not adm_obj.is_validated and not adm_obj.is_denied:
#             # If pending
#             context["pending"] = True
#             context["status_txt"] = '<i class="bi bi-hourglass-split"> Pending </i>'
#             context["btn_redirectTo"] = adm_obj.to_pendingList()
#         elif adm_obj.is_validated and not adm_obj.is_denied:
#             # if validated
#             context["status_txt"] = '<i class="bi bi-check2-circle"> Validated </i>'
#             context["btn_redirectTo"] = adm_obj.to_admittedList()

#             # Option to hold enrollment for admission with no valid enrollment data
#             context["validated"] = self.can_hold()

#         elif not adm_obj.is_validated and adm_obj.is_denied:
#             # if denied
#             rev_obj = for_review_admission.objects.filter(
#                 to_review__id=adm_obj.id).count()
#             if rev_obj > 0:
#                 # if denied with review
#                 context["revision"] = True
#                 context["status_txt"] = '<i class="bi bi-recycle"> For review </i>'
#                 context["review_contexts"] = for_review_admission.objects.values(
#                     "comment", "date_created").filter(to_review__id=self.kwargs["pk"]).order_by("date_created", "id")
#                 context["btn_redirectTo"] = adm_obj.to_reviewList()
#             else:
#                 # if denied and no review
#                 context["full_denied"] = True
#                 context["status_txt"] = '<i class="bi bi-trash3-fill"> Denied </i>'
#                 context["btn_redirectTo"] = adm_obj.to_deniedList()
#         else:
#             # For admission with is_validated=True, is_denied=True = Hold status
#             if adm_obj.is_validated and adm_obj.is_denied:
#                 context["is_hold"] = True
#                 context["status_txt"] = '<i class="bi bi-hourglass-split"> On-Hold </i>'
#                 context["btn_redirectTo"] = adm_obj.to_holdList()
#         return context

#     def can_hold(self):
#         enrollment_objs = student_enrollment_details.objects.filter(
#             admission_details__id=self.kwargs["pk"])
#         if enrollment_objs:
#             for obj in enrollment_objs:
#                 if obj.is_passed and not obj.is_denied:
#                     ans = False
#                     break
#             ans = True
#         else:
#             ans = True
#         return ans

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             student_admission_details.objects.get(id=self.kwargs["pk"])
#             return super().dispatch(request, *args, **kwargs)
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:admission_and_enrollment"))


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class admission(ListView):
#     # Get the list of pending admission using the latest school year
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/admission.html"
#     allow_empty = True
#     context_object_name = "pending_list"
#     paginate_by = 35

#     def get_queryset(self):
#         try:
#             sy = school_year.objects.latest("date_created")
#             if validate_enrollmentSetup(self.request, sy):
#                 qs = student_admission_details.objects.values("id", "date_created", "admission_owner__email", "last_name", "sex", "first_chosen_strand__strand_name", "second_chosen_strand__strand_name").filter(
#                     admission_sy=sy, is_validated=False, is_denied=False).order_by("date_modified", "date_created", "id")
#             else:
#                 qs = student_admission_details.objects.none()
#         except ObjectDoesNotExist:
#             messages.error(self.request, "You have no school year.")
#             qs = student_admission_details.objects.none()
#         except:
#             qs = student_admission_details.objects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Pending Admission"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class admitted_students(ListView):
#     # Get the list of admitted students from all school year
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/admitted.html"
#     allow_empty = True
#     context_object_name = "list_of_admitted"
#     paginate_by = 35

#     def get_queryset(self):
#         try:
#             qs = student_admission_details.objects.values("id", "date_created", "admission_owner__email", "last_name", "sex", "first_chosen_strand__strand_name",
#                                                           "second_chosen_strand__strand_name", "admission_sy__sy").filter(is_validated=True, is_denied=False).order_by("admission_sy__sy", "date_modified", "date_created", "id")
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_admission_details.objects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Admitted Students"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class review_admissionList(ListView):
#     # Get the list of for review admission from all school year
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/for_reviewList.html"
#     allow_empty = True
#     context_object_name = "forReview_List"
#     paginate_by = 35

#     def get_queryset(self):
#         try:
#             qs = student_admission_details.objects.values("id", "date_created", "admission_owner__email", "last_name", "sex", "first_chosen_strand__strand_name", "second_chosen_strand__strand_name", "admission_sy__sy").alias(
#                 count_reviews=Count("admission_review")).filter(count_reviews__gt=0, is_validated=False, is_denied=True).order_by("admission_sy__sy", "date_modified", "date_created", "id")
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_admission_details.objects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Admission for Revision"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class denied_admissionList(ListView):
#     # Get the list of denied admissions with no reviews from all school year
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/denied_admissions.html"
#     allow_empty = True
#     context_object_name = "denied_list"
#     paginate_by = 35

#     def get_queryset(self):
#         try:
#             qs = student_admission_details.objects.values("id", "date_created", "date_modified", "admission_owner__email", "last_name", "sex", "first_chosen_strand__strand_name", "second_chosen_strand__strand_name", "admission_sy__sy").alias(
#                 count_reviews=Count("admission_review")).filter(count_reviews__lt=1, is_validated=False, is_denied=True).order_by("admission_sy__sy", "date_modified", "date_created", "id")
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_admission_details.objects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Denied Admission"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class hold_admissionList(ListView):
#     # Get the list of hold admission, applicable to validated and denied = True admission.
#     # Applicable to admission with validated status and no valid enrollment status.
#     template_name = "adminportal/AdmissionAndEnrollment/admission_HTMLs/hold_admissions.html"
#     allow_empty = True
#     context_object_name = "hold_list"
#     paginate_by = 35

#     def get_queryset(self):
#         try:
#             qs = student_admission_details.objects.values("id", "date_created", "date_modified", "admission_owner__email", "last_name", "sex", "first_chosen_strand__strand_name",
#                                                           "second_chosen_strand__strand_name", "admission_sy__sy").filter(is_validated=True, is_denied=True).order_by("admission_sy__sy", "date_modified", "id", "date_created")
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_admission_details.objects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Hold Admissions"
#         return context


# def enrollment_not_existing_kwarg(request, qs, val):
#     if not qs:
#         # if qs = walang laman, then:
#         messages.warning(request, "%s does not exist." % val)


# def search_regex_match(request, val):
#     rgx = re.compile("([a-zA-Z\d\s]+)")
#     if rgx.fullmatch(val):
#         return True
#     else:
#         messages.warning(request, "%s is invalid." % val)
#         return False


# def dts_to_list(val):
#     try:
#         if int(val):
#             # if val is int
#             return True
#     except:
#         # if val is string
#         return False


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class pending_enrollment_list(ListView):
#     # Get the list of pending enrollment, applicable to valid admissions only.
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/enrollment.html"
#     allow_empty = True
#     context_object_name = "pending_enrollmentList"
#     paginate_by = 35

#     def post(self, request, *args, **kwargs):
#         try:
#             search_this = request.POST.get("search_this")
#             if search_this:
#                 if search_regex_match(request, search_this):
#                     return HttpResponseRedirect(reverse("adminportal:pending_enrollment", kwargs={"dts": search_this}))
#                 else:
#                     return HttpResponseRedirect(reverse("adminportal:pending_enrollment"))
#             else:
#                 messages.warning(
#                     request, "Enter the Student Name or ID to search.")
#                 return HttpResponseRedirect(reverse("adminportal:pending_enrollment"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:pending_enrollment"))

#     def get_queryset(self):
#         try:
#             sy = school_year.objects.latest('date_created')
#             if validate_enrollmentSetup(self.request, sy):
#                 if "dts" in self.kwargs:

#                     # Convert to list
#                     dts1 = [ltr for ltr in self.kwargs["dts"]]
#                     map_func_res = map(dts_to_list, dts1)

#                     if all(map_func_res):
#                         # if all are integers
#                         qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created').filter(
#                             id=int(self.kwargs["dts"]), enrolled_schoolyear__sy=sy, is_passed=False, is_denied=False).order_by('-date_created', '-last_modified', '-id')
#                         enrollment_not_existing_kwarg(
#                             self.request, qs, self.kwargs["dts"])

#                     else:
#                         # If combination of str and int, or pure str
#                         qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created').filter(
#                             full_name__unaccent__icontains=str(self.kwargs["dts"]), enrolled_schoolyear__sy=sy, is_passed=False, is_denied=False).order_by('-date_created', '-last_modified', '-id')
#                         enrollment_not_existing_kwarg(
#                             self.request, qs, self.kwargs["dts"])

#                 else:
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created').filter(
#                         enrolled_schoolyear__sy=sy, is_passed=False, is_denied=False).order_by('-date_created', '-last_modified', '-id')
#             else:
#                 qs = student_enrollment_details.validObjects.none()
#         except ObjectDoesNotExist:
#             messages.error(self.request, "You have no school year.")
#             qs = student_enrollment_details.validObjects.none()
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_enrollment_details.validObjects.none()
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Pending Enrollment"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class enrolled_students(ListView):
#     # Get the list of enrolled students from all school year
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/enrolled_students.html"
#     allow_empty = True
#     context_object_name = "enrolled_students"
#     paginate_by = 35

#     def post(self, request, *args, **kwargs):
#         try:
#             search_this = request.POST.get("search_this")
#             if search_this:
#                 if search_regex_match(request, search_this):
#                     return HttpResponseRedirect(reverse("adminportal:enrolled_students", kwargs={"dts": search_this}))
#                 else:
#                     return HttpResponseRedirect(reverse("adminportal:enrolled_students"))
#             else:
#                 messages.warning(
#                     request, "Enter the Student Name or ID to search.")
#                 return HttpResponseRedirect(reverse("adminportal:enrolled_students"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:enrolled_students"))

#     def get_queryset(self):
#         try:
#             if "dts" in self.kwargs:
#                 # if url with parameter
#                 # Convert to list
#                 dts1 = [ltr for ltr in self.kwargs["dts"]]

#                 # Map each item to True if integer, or False if string
#                 map_func_res = map(dts_to_list, dts1)

#                 if all(map_func_res):
#                     # if dts is integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').filter(
#                         id=int(self.kwargs["dts"]), is_passed=True, is_denied=False).order_by('-last_modified', '-id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#                 else:
#                     # if dts is not integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').filter(
#                         full_name__unaccent__icontains=str(self.kwargs["dts"]), is_passed=True, is_denied=False).order_by('-last_modified', '-id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#             else:
#                 qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age',
#                                                                     'is_late', 'is_repeater', 'date_created', 'last_modified').filter(is_passed=True, is_denied=False).order_by('-last_modified', '-id')
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_enrollment_details.validObjects.none()

#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Enrolled Students"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class for_review_enrollmentList(ListView):
#     # Get the list of enrollments for review from all school year
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/for_review_enrollments.html"
#     allow_empty = True
#     context_object_name = "for_review_students"
#     paginate_by = 35

#     def post(self, request, *args, **kwargs):
#         try:
#             search_this = request.POST.get("search_this")
#             if search_this:
#                 if search_regex_match(request, search_this):
#                     return HttpResponseRedirect(reverse("adminportal:ForReviewEnrollmentLists", kwargs={"dts": search_this}))
#                 else:
#                     return HttpResponseRedirect(reverse("adminportal:ForReviewEnrollmentLists"))
#             else:
#                 messages.warning(
#                     request, "Enter the Student Name or ID to search.")
#                 return HttpResponseRedirect(reverse("adminportal:ForReviewEnrollmentLists"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:ForReviewEnrollmentLists"))

#     def get_queryset(self):
#         try:
#             if "dts" in self.kwargs:
#                 # if url with parameter
#                 # Convert to list
#                 dts1 = [ltr for ltr in self.kwargs["dts"]]

#                 # Map each item to True if integer, or False if string
#                 map_func_res = map(dts_to_list, dts1)

#                 if all(map_func_res):
#                     # if dts is integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(
#                         count_reviews=Count("enrollment_review")).filter(id=int(self.kwargs["dts"]), is_passed=False, is_denied=True, count_reviews__gt=0).order_by('-enrolled_schoolyear__date_created', '-enrollment_review__last_modified', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#                 else:
#                     # if dts is not integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(count_reviews=Count(
#                         "enrollment_review")).filter(full_name__unaccent__icontains=str(self.kwargs["dts"]), is_passed=False, is_denied=True, count_reviews__gt=0).order_by('-enrolled_schoolyear__date_created', '-enrollment_review__last_modified', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#             else:
#                 qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(
#                     count_reviews=Count("enrollment_review")).filter(is_passed=False, is_denied=True, count_reviews__gt=0).order_by('-enrolled_schoolyear__date_created', '-enrollment_review__last_modified', 'id')
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_enrollment_details.validObjects.none()

#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Enrollment for Revision"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class denied_enrollment_list(ListView):
#     # Get the list of denied enrollments with no reviews
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/denied_enrollmentList.html"
#     allow_empty = True
#     context_object_name = "denied_enrollments"
#     paginate_by = 35

#     def post(self, request, *args, **kwargs):
#         try:
#             search_this = request.POST.get("search_this")
#             if search_this:
#                 if search_regex_match(request, search_this):
#                     return HttpResponseRedirect(reverse("adminportal:denied_enrollment_lists", kwargs={"dts": search_this}))
#                 else:
#                     return HttpResponseRedirect(reverse("adminportal:denied_enrollment_lists"))
#             else:
#                 messages.warning(
#                     request, "Enter the Student Name or ID to search.")
#                 return HttpResponseRedirect(reverse("adminportal:denied_enrollment_lists"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:denied_enrollment_lists"))

#     def get_queryset(self):
#         try:
#             if "dts" in self.kwargs:
#                 # if url with parameter
#                 # Convert to list
#                 dts1 = [ltr for ltr in self.kwargs["dts"]]

#                 # Map each item to True if integer, or False if string
#                 map_func_res = map(dts_to_list, dts1)

#                 if all(map_func_res):
#                     # if dts is integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(
#                         count_reviews=Count("enrollment_review")).filter(id=int(self.kwargs["dts"]), is_passed=False, is_denied=True, count_reviews__lt=0).order_by('-enrolled_schoolyear__date_created', '-last_modified', 'date_created', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#                 else:
#                     # if dts is not integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(count_reviews=Count(
#                         "enrollment_review")).filter(full_name__unaccent__icontains=str(self.kwargs["dts"]), is_passed=False, is_denied=True, count_reviews__lt=0).order_by('-enrolled_schoolyear__date_created', '-last_modified', 'date_created', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#             else:
#                 qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').alias(
#                     count_reviews=Count("enrollment_review")).filter(is_passed=False, is_denied=True, count_reviews__lt=1).order_by('-enrolled_schoolyear__date_created', '-last_modified', 'date_created', 'id')
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_enrollment_details.validObjects.none()

#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Denied Enrollments"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class hold_enrollment_lists(ListView):
#     # Get the list of hold enrollments
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/hold_enrollmentList.html"
#     allow_empty = True
#     context_object_name = "hold_enrollments"
#     paginate_by = 35

#     def post(self, request, *args, **kwargs):
#         try:
#             search_this = request.POST.get("search_this")
#             if search_this:
#                 if search_regex_match(request, search_this):
#                     return HttpResponseRedirect(reverse("adminportal:hold_enrollment_lists", kwargs={"dts": search_this}))
#                 else:
#                     return HttpResponseRedirect(reverse("adminportal:hold_enrollment_lists"))
#             else:
#                 messages.warning(
#                     request, "Enter the Student Name or ID to search.")
#                 return HttpResponseRedirect(reverse("adminportal:hold_enrollment_lists"))
#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse("adminportal:hold_enrollment_lists"))

#     def get_queryset(self):
#         try:
#             if "dts" in self.kwargs:
#                 # if url with parameter
#                 # Convert to list
#                 dts1 = [ltr for ltr in self.kwargs["dts"]]

#                 # Map each item to True if integer, or False if string
#                 map_func_res = map(dts_to_list, dts1)

#                 if all(map_func_res):
#                     # if dts is integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').filter(
#                         id=int(self.kwargs["dts"]), is_passed=True, is_denied=True).order_by('-enrolled_schoolyear__date_created', '-last_modified', '-date_created', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#                 else:
#                     # if dts is not integer type
#                     qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').filter(
#                         full_name__unaccent__icontains=str(self.kwargs["dts"]), is_passed=True, is_denied=True).order_by('-enrolled_schoolyear__date_created', '-last_modified', '-date_created', 'id')
#                     enrollment_not_existing_kwarg(
#                         self.request, qs, self.kwargs["dts"])

#             else:
#                 qs = student_enrollment_details.validObjects.values('id', 'enrolled_schoolyear', 'full_name', 'home_address__permanent_home_address', 'age', 'is_late', 'is_repeater', 'date_created', 'last_modified').filter(
#                     is_passed=True, is_denied=True).order_by('-enrolled_schoolyear__date_created', '-last_modified', '-date_created', 'id')
#         except Exception as e:
#             messages.error(self.request, e)
#             qs = student_enrollment_details.validObjects.none()

#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Hold Enrollments"
#         return context


# @method_decorator([login_required(login_url="usersPortal:login"), user_passes_test(superuser_only, login_url="registrarportal:dashboard")], name="dispatch")
# class enrollment_details(DetailView):
#     template_name = "adminportal/AdmissionAndEnrollment/enrollment_HTMLs/enrollment_details.html"
#     context_object_name = "stud_enrollment_details"

#     def post(self, request, *args, **kwargs):
#         try:
#             # get_enrollment will retrieved the object with valid admission using get() method.
#             get_enrollment = student_enrollment_details.validObjects.only(
#                 'id', 'enrolled_schoolyear').get(id=self.kwargs["pk"])

#             if validate_enrollmentSetup(request, get_enrollment.enrolled_schoolyear):
#                 # If enrollment sy is latest

#                 if "accept_pending" in request.POST:
#                     self.accept_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_pendingList())
#                 elif "denied_pending" in request.POST:
#                     self.denied_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_pendingList())
#                 elif "denied_pending_withreview" in request.POST:
#                     if not request.POST.get('review'):
#                         messages.warning(
#                             request, "You must add a comment if denied for revision.")
#                         return HttpResponseRedirect(reverse("adminportal:enrollment_details"), kwargs={"pk": self.kwargs["pk"]})
#                     self.denied_enrollment()
#                     self.save_comment(request.POST.get('review'))
#                     return HttpResponseRedirect(get_enrollment.to_pendingList())

#                 elif "accept_revision" in request.POST:
#                     self.accept_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_reviewList())

#                 elif "accept_denied" in request.POST:
#                     self.accept_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_deniedList())
#                 elif "denied_withrevision_submit" in request.POST:
#                     if not request.POST.get('review'):
#                         messages.warning(
#                             request, "You must add a comment if denied for revision.")
#                         return HttpResponseRedirect(reverse("adminportal:enrollment_details"), kwargs={"pk": self.kwargs["pk"]})
#                     self.denied_enrollment()
#                     self.save_comment(request.POST.get('review'))
#                     return HttpResponseRedirect(get_enrollment.to_deniedList())

#                 elif "re_validate" in request.POST:
#                     self.accept_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_holdList())
#                 elif "denied_hold" in request.POST:
#                     self.denied_enrollment()
#                     return HttpResponseRedirect(get_enrollment.to_holdList())
#                 elif "hold_withrevision_submit" in request.POST:
#                     if not request.POST.get('review'):
#                         messages.warning(
#                             request, "You must add a comment if denied for revision.")
#                         return HttpResponseRedirect(reverse("adminportal:enrollment_details"), kwargs={"pk": self.kwargs["pk"]})
#                     self.denied_enrollment()
#                     self.save_comment(request.POST.get('review'))
#                     return HttpResponseRedirect(get_enrollment.to_holdList())

#                 else:
#                     messages.warning(request, "Features will add soon.")
#                     return HttpResponseRedirect(reverse("adminportal:pending_enrollment"))

#             else:
#                 messages.warning(
#                     request, "%s is no longer editable." % get_enrollment.id)
#                 return HttpResponseRedirect(reverse('adminportal:Admission_and_enrollment'))

#         except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect(reverse('adminportal:Admission_and_enrollment'))

#     def save_comment(self, comment):
#         create_review = enrollment_review.objects.create(
#             to_review=student_enrollment_details.validObjects.get(
#                 id=int(self.kwargs["pk"])),
#             comment=comment
#         )

#     def denied_enrollment(self):
#         with transaction.atomic():
#             get_enrollment = student_enrollment_details.validObjects.select_for_update().get(
#                 id=int(self.kwargs["pk"]))
#             get_enrollment.is_passed = False
#             get_enrollment.is_denied = True
#             get_enrollment.save()

#     def accept_enrollment(self):
#         with transaction.atomic():
#             get_enrollment = student_enrollment_details.validObjects.select_for_update().get(
#                 id=int(self.kwargs["pk"]))
#             get_enrollment.is_passed = True
#             get_enrollment.is_denied = False
#             get_enrollment.save()

#     def next_pending_enrollment(self, id):
#         pass

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             student_enrollment_details.validObjects.get(id=self.kwargs["pk"])
#             return super().dispatch(request, *args, **kwargs)
#         except Exception as e:
#             messages.error(request, "Enrollment Details not found")
#             return HttpResponseRedirect(reverse("adminportal:pending_enrollment"))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Enrollment Details"

#         # The following codes will be used to get the enrollment status and other data related to the status
#         try:
#             enrolled_obj = student_enrollment_details.validObjects.get(
#                 id=self.kwargs["pk"])
#             count_enrollment_comments = enrollment_review.objects.filter(
#                 to_review=enrolled_obj).count()
#             context["enrollment_status"] = self.get_enrollment_status(
#                 enrolled_obj, count_enrollment_comments, enrolled_obj.enrolled_schoolyear)

#             context["valid_to_edit"] = validate_enrollmentSetup(
#                 self.request, enrolled_obj.enrolled_schoolyear)

#             match context["enrollment_status"]:
#                 case "Validated":
#                     context["back_btn"] = enrolled_obj.to_enrolledList()
#                     context["hold_enrollment"] = True if (
#                         date.today() - enrolled_obj.last_modified) == 7 else False
#                 case "Pending":
#                     context["back_btn"] = enrolled_obj.to_pendingList()
#                 case "Hold":
#                     context["back_btn"] = enrolled_obj.to_holdList()
#                 case "For revision":
#                     context["back_btn"] = enrolled_obj.to_reviewList()
#                     context["enrollment_comments"] = enrollment_review.objects.values_list(
#                         'comment', flat=True).filter(to_review=enrolled_obj).order_by("-date_created")
#                 case "Denied":
#                     context["back_btn"] = enrolled_obj.to_holdList()
#         except Exception as e:
#             # messages.error(self.request, e)
#             pass

#         return context

#     def get_enrollment_status(self, obj, count_reviews, sy):
#         if obj.is_passed and not obj.is_denied:
#             return "Validated"
#         elif not obj.is_passed and not obj.is_denied:
#             return "Pending"
#         elif obj.is_passed and obj.is_denied:
#             return "Hold"
#         else:
#             if not validate_enrollmentSetup(sy):
#                 return "No longer valid"
#             elif count_reviews > 0:
#                 return "For revision"
#             else:
#                 return "Denied"

#     def get_queryset(self):
#         return student_enrollment_details.validObjects.all()
