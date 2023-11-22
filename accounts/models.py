from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentDetails(models.Model):
    photo = models.ImageField(upload_to = 'photos/student/', blank = True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class EntrepreneurDetails(models.Model):
    photo = models.ImageField(upload_to = '%Y/%m/%d/photos/entrepreneur/', blank = True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)


class InvestorDetails(models.Model):
    mobile_number = models.CharField(max_length=12)
    landline_number = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank = True, default = '')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = '%Y/%m/%d/photos/investor/', blank = True)
    about = models.TextField()
    focus_industries = models.CharField(max_length=100)
    focus_sectors = models.CharField(max_length=100)
    startup_stages = models.CharField(max_length=100)
    min_investment_range = models.IntegerField()
    max_investment_range = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'InvestorDetails'


class Projects(models.Model):
    organization_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    business_phone_number = models.CharField(max_length=15)
    document1 = models.FileField(upload_to = '%Y/%m/%d/files/ProjectDoc1/')
    document2 = models.FileField(upload_to = '%Y/%m/%d/files/ProjectDoc2/', blank = True)
    theme = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    problem_statement_title = models.TextField()
    problem_statement_description = models.TextField()
    demo_link = models.URLField(null = True, blank = True)
    dataset = models.URLField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.problem_statement_title
