from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.core.validators import RegexValidator
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import RangeOperators
from django.db.models import Q

User = get_user_model()


def split_this_contactnum(cnum):
    # convert this int type into an str object
    cnum = str(cnum)

    # Initialize a list
    this_list = []

    # Iterate each str into list of str
    for obj in cnum:
        this_list.append(obj)

    # Remove 6 3 from the list
    this_list.pop(0)
    this_list.pop(0)

    # initialize new str variable
    new_doc_contact_num = ""

    # iterate each list item and append to str variable
    for each_lst in this_list:
        new_doc_contact_num += each_lst

    # convert str into int
    new_doc_contact_num = int(new_doc_contact_num)

    # return the update contact num to be display back to caller
    return new_doc_contact_num


def current_school_year():
    date_now = date.today()
    years = 1
    try:
        year_only = date_now.replace(year=date_now.year + years)
    except ValueError:
        year_only = date_now.replace(year=date_now.year + years, day=28)
    sy = " ".join(
        map(str, [date_now.strftime("%Y"), "-", year_only.strftime("%Y")]))

    return sy


class school_year(models.Model):
    sy = models.CharField(max_length=11, primary_key=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sy


class shs_track(models.Model):
    track_name = models.CharField(max_length=50)
    definition = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.track_name


class shs_strand(models.Model):
    track = models.ForeignKey(
        shs_track, on_delete=models.SET_NULL, null=True, related_name="track_strand")
    strand_name = models.CharField(max_length=100)
    definition = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.strand_name


class student_admission_details(models.Model):

    class SexChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    admission_owner = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="admission_details")
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=2, choices=SexChoices.choices)
    date_of_birth = models.DateField()
    birthplace = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50)

    # Elementary school details
    elem_name = models.CharField(max_length=50)
    elem_address = models.CharField(max_length=50)
    elem_region = models.CharField(max_length=30)
    elem_year_completed = models.DateField()
    elem_pept_passer = models.BooleanField(default=False)
    elem_pept_date_completion = models.DateField(null=True, blank=True)
    elem_ae_passer = models.BooleanField(default=False)
    elem_ae_date_completion = models.DateField(null=True, blank=True)
    elem_community_learning_center = models.CharField(max_length=50)
    elem_clc_address = models.CharField(max_length=50)

    # Junior High school details
    jhs_name = models.CharField(max_length=50)
    jhs_address = models.CharField(max_length=50)
    jhs_region = models.CharField(max_length=30)
    jhs_year_completed = models.DateField()
    jhs_pept_passer = models.BooleanField(default=False)
    jhs_pept_date_completion = models.DateField(null=True, blank=True)
    jhs_ae_passer = models.BooleanField(default=False)
    jhs_ae_date_completion = models.DateField(null=True, blank=True)
    jhs_community_learning_center = models.CharField(max_length=50)
    jhs_clc_address = models.CharField(max_length=50)

    is_validated = models.BooleanField(default=False)
    admission_sy = models.ForeignKey(
        school_year, on_delete=models.SET_NULL, null=True, related_name="sy_admitted")
    first_chosen_strand = models.ForeignKey(
        shs_strand, on_delete=models.SET_NULL, null=True, related_name="first_strand")
    second_chosen_strand = models.ForeignKey(
        shs_strand, on_delete=models.SET_NULL, null=True, related_name="second_strand")

    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_created"]
        get_latest_by = ["date_created"]

    def __str__(self):
        return f"{self.admission_owner}: {self.last_name}, {self.first_name} {self.middle_name} - {self.sex}"

    def elementary_school(self):
        return self.elem_name

    def jhs(self):
        return self.jhs_name

    def student_basic_details(self):
        return {
            "student_acc_id": self.admission_owner.id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "date_of_birth": self.date_of_birth,
            "birthplace": self.birthplace,
            "nationality": self.nationality,
        }


class student_enrollment_details(models.Model):
    student_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_enrollment_details")
    admission_details = models.ForeignKey(
        student_admission_details, on_delete=models.SET_NULL, null=True, related_name="user_student_enrollment_details")
    selected_strand = models.ForeignKey(
        shs_strand, on_delete=models.SET_NULL, null=True, related_name="chosen_strand")
    full_name = models.CharField(max_length=35)
    permanent_home_address = models.CharField(max_length=50)
    cp_number_regex = RegexValidator(regex=r"^(09)([0-9]{9})$")
    cellphone_number = models.CharField(
        max_length=11, unique=True, validators=[cp_number_regex])
    age_validator = RegexValidator(regex=r"([0-9])")
    age = models.CharField(max_length=3, validators=[age_validator])

    report_card = models.ImageField(upload_to="Report_cards/%Y/")
    profile_image = models.ImageField(upload_to="User_profiles/")

    is_passed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    enrolled_schoolyear = models.ForeignKey(
        school_year, on_delete=models.SET_NULL, null=True, related_name="sy_enrolled")

    date_created = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name