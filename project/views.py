from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import UserRegisterForm, AssignmentForm, SubmissionForm
from .models import Assignment, Submission


@login_required(login_url="login")
def home_page(request):

    assignments = Assignment.objects.all()

    context = {"assignments": assignments}

    return render(request, "home_page.html", context)


@login_required(login_url="login")
def assignment_page(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    context = {"assignment": assignment}
    user = request.user

    if request.method == "POST":
        file = request.FILES["file"]

        submission = Submission.objects.create(
            student=user,
            file=file,
            assignment=assignment,
        )

    if request.user.is_staff:
        submissions = assignment.submissions.all()
        context["submissions"] = submissions

        return render(request, "assignment.html", context)

    else:
        submissions = user.submissions.all()
        context["submissions"] = submissions

        return render(request, "assignment-student.html", context)


def create_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uy ishi muvaffaqiyatli yaratildi!")
            return redirect("home")
    else:
        form = AssignmentForm()
    return render(request, "assignments/create_assignment.html", {"form": form})


def submit_assignment(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Uy ishi muvaffaqiyatli yuklandi!")

            return redirect("submit-assignment")
    else:
        form = SubmissionForm()
    return render(request, "assignments/submit_assignment.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect("home")

        else:
            messages.error(request, "Login yoki parol noto'g'ri!")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz!")
    return redirect("login")
