from django.db import models
from django.contrib.auth.models import User

def get_user_email():
    # This function retrieves the email from the User model during object creation
    return User.objects.first().email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    information = models.TextField()
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.user.username



class Course(models.Model):
    SSC = 'SSC'
    HSC = 'HSC'
    ADMISSION = 'Admission'

    CATEGORY_CHOICES = [
        (SSC, 'SSC'),
        (HSC, 'HSC'),
        (ADMISSION, 'Admission'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ensure decimal field for price
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=SSC)

    def __str__(self):
        return self.title

class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review = models.TextField()

class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_materials/', default='default.pdf')
    youtube_link = models.URLField(blank=True, null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through='CartCourse', related_name='carts')  # M2M relation with CartCourse

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartCourse(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Ensure positive integer for quantity

    def __str__(self):
        return f"{self.course.title} in {self.cart.user.username}'s cart"