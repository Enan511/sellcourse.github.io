from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth import logout
from .forms import ProfileForm
from .models import UserProfile
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.http import JsonResponse
from .models import Cart, CartCourse, Course
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'home.html')


def allcourses(request):
    return render(request, 'allcourses.html')


# def create_account(request):
#     return render(request, 'create_account.html')

def forget_password(request):
    return render(request, 'password_reset_form.html')


# def login(request):
#     return render(request, 'login.html')

def navbar(request):
    return render(request, 'navbar.html')


def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose the email content
            email_subject = f"Contact Form Submission: {subject}"
            email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Send the email
            send_mail(
                email_subject,
                email_body,
                'aninshams@gmail.com',  # Your email address as the sender
                ['atikshams8@gmail.com'],  # The address where you want to receive contact messages
                fail_silently=False,
            )

            messages.success(request, "Thank you for your message. We will get back to you soon.")
            return redirect('contact_success')  # Redirect to a success page or another page
        else:
            messages.error(request, "There were errors with your submission. Please correct the indicated fields.")
    else:
        form = ContactForm()  # Render a new form if GET request
    
    return render(request, 'contact.html', {'form': form})


def account_recovery(request, token):
    return render(request, 'account_recovery.html')


def teachers(request):
    return render(request, 'teachers.html')



def profile(request):
    return render(request, 'profile.html')


def submission(request):
    return render(request, 'course_submission.html')


def course_page(request):
    return render(request, 'course_page.html')


def create_account(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Set success message
            messages.success(request, 'Registration successful. You can now log in.')
            # Redirect to login page
            return redirect('login') 
    else:
        form = RegistrationForm()

    return render(request, 'create_account.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                # Add an error message to the form
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')  



def profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Update associated User object
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['surname']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})







def course_info(request):
    return render(request, 'course_info.html')



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def ssc_courses(request):
    ssc_courses_list = Course.objects.filter(category='SSC')
    paginator = Paginator(ssc_courses_list, 6)  # Show 6 courses per page

    page = request.GET.get('page')
    try:
        ssc_courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ssc_courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ssc_courses = paginator.page(paginator.num_pages)

    return render(request, 'ssc.html', {'courses': ssc_courses})


def hsc_courses(request):
    hsc_courses_list = Course.objects.filter(category='HSC')
    paginator = Paginator(hsc_courses_list, 6)  # Show 6 courses per page

    page = request.GET.get('page')
    try:
        hsc_courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hsc_courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hsc_courses = paginator.page(paginator.num_pages)

    return render(request, 'hsc.html', {'courses': hsc_courses})

def admission_courses(request):
    admission_courses_list = Course.objects.filter(category='Admission')
    paginator = Paginator(admission_courses_list, 6)  # Show 6 courses per page

    page = request.GET.get('page')
    try:
        admission_courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        admission_courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        admission_courses = paginator.page(paginator.num_pages)

    return render(request, 'admission.html', {'courses': admission_courses})




from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Course

def courses_all(request):
    # Get all courses
    courses_all_list = Course.objects.all()

    # Sort courses based on user request
    sort_by = request.GET.get('sort_by')
    if sort_by == 'price_high_to_low':
        courses_all_list = courses_all_list.order_by('-price')
    elif sort_by == 'price_low_to_high':
        courses_all_list = courses_all_list.order_by('price')

    # Pagination
    paginator = Paginator(courses_all_list, 6)
    page = request.GET.get('page')
    try:
        courses_all = paginator.page(page)
    except PageNotAnInteger:
        courses_all = paginator.page(1)
    except EmptyPage:
        courses_all = paginator.page(paginator.num_pages)

    return render(request, 'courses_all.html', {'courses': courses_all})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Ensure the course exists
    return render(request, 'course_detail.html', {'course': course})


def search_courses(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses_all.html', {'courses': courses})

def search_courses_ssc(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(category='SSC', title__icontains=query)
    else:
        courses = Course.objects.filter(category='SSC')
    return render(request, 'ssc.html', {'courses': courses})

def search_courses_hsc(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(category='HSC', title__icontains=query)
    else:
        courses = Course.objects.filter(category='HSC')
    return render(request, 'hsc.html', {'courses': courses})

def search_courses_admission(request):

    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(category='Admission', title__icontains=query)
    else:
        courses = Course.objects.filter(category='Admission')
    return render(request, 'admission.html', {'courses': courses})

@login_required
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create a Cart for the user

    cart_course, created = CartCourse.objects.get_or_create(cart=cart, course=course)
    if not created:
        cart_course.quantity += 1  # Increment the quantity if it exists
        cart_course.save()

    # Return JSON response indicating success
    return JsonResponse({"success": True, "message": "Course added to cart"})

@login_required
def cart_view(request):
    # Retrieve the user's cart and related courses
    cart = Cart.objects.filter(user=request.user).first()
    cart_courses = CartCourse.objects.filter(cart=cart)  # Get all CartCourses for the user
    
    # Initialize variables for the template context
    cart_items = []
    total_products = 0

    # Loop through the CartCourses to populate cart items
    for cart_course in cart_courses:
        course = cart_course.course
        quantity = cart_course.quantity
        total_price = course.price * quantity  # Calculate total price for this item
        
        # Append details to the cart_items list
        cart_items.append({
            "course": course,
            "quantity": quantity,
            "total_price": total_price,
        })
        
        total_products += total_price  # Update the grand total
    
    # Render the cart template with the correct context
    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total_products': total_products
        }
    )
@csrf_exempt
@login_required
def remove_from_cart(request, course_id):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)  # Get the user's cart
        cart_course = get_object_or_404(CartCourse, cart=cart, course_id=course_id)
        cart_course.delete()  # Delete the specified course
        return JsonResponse({"success": True})  # Return success response
    else:
        return JsonResponse({"success": False, "message": "Invalid request"})
@login_required
def update_cart(request, course_id, increment):
    # Find the cart and the specific course in the cart
    cart = get_object_or_404(Cart, user=request.user)
    cart_course = get_object_or_404(CartCourse, cart=cart, course_id=course_id)

    # Update the quantity based on the increment
    cart_course.quantity += increment

    # Ensure the quantity doesn't go below 1
    if cart_course.quantity < 1:
        cart_course.delete()  # If quantity is less than 1, remove it
    else:
        cart_course.save()  # Save the updated quantity

    return JsonResponse({"success": True, "message": "Quantity updated"})