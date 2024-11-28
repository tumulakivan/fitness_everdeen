from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Schedule, WorkoutTip
from .forms import WorkoutForm, WorkoutTipForm
from .models import Workout
from .forms import WorkoutForm


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            next_url = request.GET.get('next', 'main')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')


# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            try:
                user = User.objects.create_user(
                    username=username, 
                    password=password, 
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name
                )
                messages.success(request, "Registration successful!")
                return redirect('login')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
    return render(request, 'accounts/register.html')



# Main Dashboard
def main_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must log in first.")
        return redirect('login')

    # Fetch the user's workouts (if any)
    workouts = Workout.objects.filter(user=request.user)

    return render(request, 'accounts/main.html', {
        'username': request.user.username,
        'workouts': workouts,  # Pass workouts to the main dashboard
    })



# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


# Workout Management
def workout_list(request):
    schedules = Schedule.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'accounts/workout_list.html', {'schedules': schedules})


@login_required  # Ensure that only logged-in users can add a workout
def add_workout(request):
    if request.method == 'POST':
        workout_name = request.POST.get('workout_name')
        description = request.POST.get('description')
        workout_type = request.POST.get('workout_type')

        workout = Workout(
            name=workout_name,
            description=description,
            workout_type=workout_type,
            user=request.user 
        )
        workout.save()

        return redirect('main') 

    return render(request, 'accounts/add_workout.html')


@login_required
def edit_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout updated successfully!")
            return redirect('main')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'accounts/edit_workout.html', {'form': form})


@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    workout.delete()
    messages.success(request, "Workout deleted successfully!")
    return redirect('main')


# Tip Management
def tip_list(request):
    tips = WorkoutTip.objects.all()
    return render(request, 'accounts/tip_list.html', {'tips': tips})


def add_tip(request):
    if request.method == 'POST':
        form = WorkoutTipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout tip added successfully!")
            return redirect('tip_list')
    else:
        form = WorkoutTipForm()
    return render(request, 'accounts/add_tip.html', {'form': form})


def update_tip(request, pk):
    tip = get_object_or_404(WorkoutTip, pk=pk)
    if request.method == 'POST':
        form = WorkoutTipForm(request.POST, instance=tip)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout tip updated successfully!")
            return redirect('tip_list')
    else:
        form = WorkoutTipForm(instance=tip)
    return render(request, 'accounts/update_tip.html', {'form': form})


def delete_tip(request, pk):
    tip = get_object_or_404(WorkoutTip, pk=pk)
    tip.delete()
    messages.success(request, "Workout tip deleted successfully!")
    return redirect('tip_list')
