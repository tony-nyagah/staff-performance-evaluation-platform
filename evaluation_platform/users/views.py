from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

# from evaluation_platform.evaluations.models import UserEvaluation, UserSection, Evaluation


@login_required
def home_view(request):
    # today = timezone.now().date()
    # current_year = today.year
    #
    # user_evaluations = UserEvaluation.objects.filter(staff_member=request.user)
    # current_year_evaluation = UserEvaluation.objects.filter(
    # current_year_user_evaluation = user_evaluations.
    #
    # if not existing_evaluation:
    #     user_evaluation = UserEvaluation.objects.filter(evaluation__year=current_year).first()
    #     if not user_evaluation:
    #         user_evaluation = UserEvaluation.objects.create(
    #             year=current_year,
    #             start_date=timezone.now().date(),
    #             submission_deadline=timezone.now().date() + timezone.timedelta(days=30),
    #         )
    #
    #     user_evaluation = UserEvaluation.objects.create(
    #         staff_member=request.user, evaluation=evaluation
    #     )
    #
    #     default_sections = UserSection.objects.all()
    #     for default_section in default_sections:
    #         UserSection.objects.create(
    #             user_evaluation=user_evaluation,
    #             section=default_section,
    #         )
    # else:
    #     evaluation = existing_evaluation
    #
    # evaluations = UserEvaluation.objects.filter(
    #     evaluation__start_date__lte=today,
    #     evaluation__submission_deadline__gte=today,
    #     staff_member=request.user,
    # )
    #
    # return render(request, "users/home.html", {"evaluations": evaluations})
    return render(request, "users/home.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, message="Invalid email or password.")
    return render(request, template_name="users/login.html")


@login_required
def profile_view(request):
    return render(request, template_name="users/profile.html")


def logout_view(request):
    logout(request)
    messages.info(request, message="You have been logged out.")
    return redirect("login")
