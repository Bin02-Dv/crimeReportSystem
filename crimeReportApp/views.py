from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CrimeReports
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('login')
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        nin = request.POST['nin']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist!!')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist!!')
            return redirect('signup')
        elif cpassword != password:
            messages.error(request, 'Password and confirm password missed match!!')
            return redirect('signup')
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password, first_name=full_name, )
            new_user.save()
            messages.success(request, 'Sign Up completed successfully...')
            return redirect('login')
    return render(request, "signup.html")

@login_required(login_url='/')
def dashboard(request):
    user = request.user
    all_new_reports = CrimeReports.objects.filter(status=False).count()
    context = {
        'user':user,
        'all_new_reports':all_new_reports
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='/')
def user_settings(request):
    user = request.user
    
    if request.method == 'POST':
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        # Check if password and confirm password match
        if cpassword != password:
            messages.error(request, 'Password and Confirm password mismatch!')
        else:
            # Set the new password
            user.set_password(password)
            user.save()
            
            # Update session to prevent logout after password change
            update_session_auth_hash(request, user)
            
            # Add a success message and redirect
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('/')

    all_new_reports = CrimeReports.objects.filter(status=False).count()
    context = {
        'user':user,
        'all_new_reports':all_new_reports
    }
    return render(request, "settings.html", context)

@login_required(login_url='/')
def crimeReport(request):
    user = request.user
    if request.method == 'POST':
        if request.FILES.get('evidence'):
            full_name = user.first_name
            email = user.email
            crime_type = request.POST['crime_type']
            location = request.POST['location']
            description = request.POST['description']
            evidence = request.FILES.get('evidence')
            
            # Create new crime report
            new_report = CrimeReports.objects.create(
                user=user,
                full_name=full_name, 
                email_address=email,  # Fixed typo here
                crime_type=crime_type, 
                location=location,
                description=description, 
                evidence=evidence
            )
            
            # Redirect to 'viewReport' page after successful submission
            return redirect('viewReport')

    # Render the form page with user information
    all_new_reports = CrimeReports.objects.filter(status=False).count()
    context = {
        'user':user,
        'all_new_reports':all_new_reports
    }
    return render(request, "crimeReport.html", context)

@login_required(login_url='/')
def viewReport(request):
    user = request.user
    crimes = CrimeReports.objects.filter(user=user).order_by('-id')
    all_crimes = CrimeReports.objects.all().order_by('-id')
    all_new_reports = CrimeReports.objects.filter(status=False).count()
    context = {
        'user':user,
        'crimes':crimes,
        'all_crimes':all_crimes,
        'all_new_reports':all_new_reports
    }
    return render(request, "viewReport.html", context)

def update_crime(request, id):
    crime = CrimeReports.objects.get(id=id)
    crime.status = True
    crime.save()
    return redirect("viewReport")

def delete_crime(request, id):
    crime = CrimeReports.objects.get(id=id)
    crime.delete()
    return redirect("viewReport")