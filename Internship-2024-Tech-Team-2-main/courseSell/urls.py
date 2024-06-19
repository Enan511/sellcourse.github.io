from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    path('course/', views.course_page, name='course_page'),
    path('create-account/', views.create_account, name='create_account'),
    path('allcourses', views.allcourses, name='allcourses'),
    path('login/', views.user_login, name='login'),
    path('navbar/', views.navbar, name='navbar'),
    path('profile/', views.profile, name='profile'),
    path('teacher/', views.teachers, name='teachers'),
    path('submission/', views.submission, name='submission'),
    path('logout/', views.logout_view, name='logout'),
    path('course_info/', views.course_info, name='course_info'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordResetView.as_view(template_name='change_password.html'), name='change_password'),
    path('ssc/', views.ssc_courses, name='ssc_courses'),
    path('hsc/', views.hsc_courses, name='hsc_courses'),
    path('admission/', views.admission_courses, name='admission_courses'),
    path('course_all/', views.courses_all, name='coursesall'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'), 
    path('search/', views.search_courses, name='search_courses'),
    path('search_ssc/', views.search_courses_ssc, name='search_courses_ssc'),
    path('search_hsc/', views.search_courses_hsc, name='search_courses_hsc'),
    path('search_admission/', views.search_courses_admission, name='search_courses_admission'),
    path('contact/', views.contact_view, name='contact'),  # URL for the contact form submission
    path('contact/success/', lambda request: render(request, 'contact_success.html'), name='contact_success'),
    path('cart/', views.cart_view, name='cart'),  # Cart page
    path('add_to_cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart operation
    path('remove_from_cart/<int:course_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:course_id>/<int:increment>/', views.update_cart, name='update_cart'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

