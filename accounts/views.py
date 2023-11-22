from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import StudentDetails, EntrepreneurDetails, InvestorDetails, Projects

# Create your views here.
def studentRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/studentRegister.html', {'error_message': "Username already exists."})
            
            elif User.objects.filter(email=email).exists():
                return render(request, 'accounts/studentRegister.html', {'error_message': "Email already exists."})
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()

                user1=auth.authenticate(username=username, password=password1)
            
                if user1 is not None:
                    auth.login(request, user1)
                    return redirect('/accounts/student-details')
                return redirect('/accounts/student-login')

        else:
            return render(request, 'accounts/studentRegister.html', {'error_message': "Password didn't match."})
        
    return render(request, 'accounts/studentRegister.html')

def entrepreneurRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/entrepreneurRegister.html', {'error_message': "Username already exists."})
            
            elif User.objects.filter(email=email).exists():
                return render(request, 'accounts/entrepreneurRegister.html', {'error_message': "Email already exists."})
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()

                user1=auth.authenticate(username=username, password=password1)
            
                if user1 is not None:
                    auth.login(request, user1)
                    return redirect('/accounts/entrepreneur-details')
                return redirect('/accounts/entrepreneur-login')
            
        else:
            return render(request, 'accounts/entrepreneurRegister.html', {'error_message': "Password didn't match."})
        
    return render(request, 'accounts/entrepreneurRegister.html')

def investorRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/investorRegister.html', {'error_message': "Username already exists."})
            
            elif User.objects.filter(email=email).exists():
                return render(request, 'accounts/investorRegister.html', {'error_message': "Email already exists."})
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()
                user1=auth.authenticate(username=username, password=password1)
            
                if user1 is not None:
                    auth.login(request, user1)
                    return redirect('/accounts/investor-details')
        else:
            return render(request, 'accounts/investorRegister.html', {'error_message': "Password didn't match."})
        
    
    return render(request, "accounts/investorRegister.html")

def investorDetails(request):
    if request.method == 'POST':
        mobile_number = request.POST['mobile_number']
        landline_number = request.POST['landline_number']
        website = request.POST['website']
        state = request.POST['state']
        city = request.POST['city']
        photo = request.FILES['image']
        about = request.POST['about']
        focus_industries = request.POST['focus_industries']
        focus_sectors = request.POST['focus_sectors']
        startup_stages = request.POST['startup_stages']
        min_investment_range = request.POST['min_investment_range']
        max_investment_range = request.POST['max_investment_range']
        user = request.user

        print(user)

        investor = InvestorDetails(mobile_number=mobile_number, landline_number=landline_number, website=website, state=state, city=city, photo=photo, about=about, focus_industries=focus_industries, focus_sectors=focus_sectors, startup_stages=startup_stages, min_investment_range=min_investment_range, max_investment_range=max_investment_range, user=user)
        investor.save()
        return redirect('/accounts/successful-registration')
    
    return render(request , 'accounts/investorInfo.html')

def registerResponse(request):
    return render(request , 'accounts/response.html')

def studentLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/accounts/dashboard')
        else:
            return render(request, 'accounts/studentLogin.html', {'error_message': "Invalid Credentials"})

    return render(request=request, template_name="accounts/studentLogin.html")

def entrepreneurLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/entrepreneurLogin.html', {'error_message': "Invalid Credentials"})

    return render(request=request, template_name="accounts/entrepreneurLogin.html")

def studentDetails(request):
    if request.method == 'POST':
        image = request.FILES['image']
        age = request.POST['age']
        mobile = request.POST['mobile']
        college = request.POST['college']
        state = request.POST['state']
        city = request.POST['city']
        role = request.POST['role']
        interest1 = request.POST['interest1']
        interest2 = request.POST['interest2']
        interest3 = request.POST['interest3']
        about_yourself = request.POST['about_yourself']
        user = request.user

        student = StudentDetails(photo=image, age=age, mobile=mobile, college=college, state=state, city=city, role=role, interest1=interest1, interest2=interest2, interest3=interest3, about_yourself=about_yourself, user=user)
        student.save()
        return redirect('/accounts/dashboard')
    
    return render(request , 'accounts/studentInfo.html')

def submitProjectIdea(request):
    if request.method == 'POST':
        organization_name = request.POST['organization_name']
        sector = request.POST['sector']
        business_phone_number = request.POST['business_phone_number']
        document1 = request.FILES['document1']
        document2 = request.FILES['document2']
        theme = request.POST['theme']
        category = request.POST['category']
        problem_statement_title = request.POST['problem_statement_title']
        problem_statement_description = request.POST['problem_statement_description']
        demo_link = request.POST['demo_link']
        dataset = request.POST['dataset']

        project = Projects(organization_name=organization_name, sector=sector, business_phone_number=business_phone_number, document1=document1, document2=document2, theme=theme, category=category, problem_statement_title=problem_statement_title, problem_statement_description=problem_statement_description, demo_link=demo_link, dataset=dataset)
        project.save()

        return redirect('/accounts/successful-registration')
    
    return render(request, "accounts/projectSubmit.html")


def entrepreneurDetails(request):
    if request.method == 'POST':
        image = request.FILES['image']
        age = request.POST['age']
        mobile = request.POST['mobile']
        state = request.POST['state']
        city = request.POST['city']
        role = request.POST['role']
        interest1 = request.POST['interest1']
        interest2 = request.POST['interest2']
        interest3 = request.POST['interest3']
        about_yourself = request.POST['about_yourself']
        user = request.user

        student = EntrepreneurDetails(photo=image, age=age, mobile=mobile, state=state, city=city, role=role, interest1=interest1, interest2=interest2, interest3=interest3, about_yourself=about_yourself, user=user)
        student.save()
        return redirect('/accounts/dashboard')
    
    return render(request , 'accounts/entrepreneurInfo.html')


def dashboard(request):
    investors = InvestorDetails.objects.all()
    projects = Projects.objects.all()

    context = {
        'investors': investors,
        'projects': projects,
    }

    return render(request , 'accounts/dashboard.html', context)

def logoutPage(request):
    auth.logout(request)
    return redirect('/')