from django.db import models
from django.db.models import F
class Home(models.Model):
    page_title=models.CharField(max_length=15,default="Blog")
    two_letter_of_name=models.CharField(max_length=2,verbose_name="Two letter of name for logo")
    photo = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100,default="Web Developer")
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class About(models.Model):
    photo = models.ImageField(upload_to='photos/about/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class About_skills(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE,related_name='skills')
    name = models.CharField(max_length=100)
    percent = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Categories(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Portfolio(models.Model):
    photo = models.ImageField(upload_to='photos/portfolio/')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Services(models.Model):
    image = models.ImageField(upload_to='photos/services/',null=True)
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name
class Resume_photo(models.Model):
    photo = models.ImageField(upload_to='photos/resume/',verbose_name="Resume oynasi uchun")
    is_active = models.BooleanField(default=True)

class Experience(models.Model):
    JOB_TYPE_CHOICES = [
        ('FULLTIME', 'Full-time'),
        ('PARTTIME', 'Part-time'),
    ]

    job = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job_type = models.CharField(verbose_name="Job Type", max_length=100, choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.job} - {self.company}"

    class Meta:
        ordering = [F('end_date').desc(nulls_first=True), '-start_date']

class Education(models.Model):
    degree = models.CharField(max_length=255, verbose_name="Mutaxassislik (Daraja)")
    university = models.CharField(max_length=255, verbose_name="Universitet nomi")
    start_date = models.DateField(verbose_name="Boshlangan sana")
    end_date = models.DateField(null=True, blank=True, verbose_name="Tugallangan sana")

    def __str__(self):
        return f"{self.degree} - {self.university}"

    class Meta:
        ordering = [F('end_date').desc(nulls_first=True), '-start_date']
class Clients(models.Model):
    image = models.ImageField(upload_to='photos/clients/')
    body = models.TextField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_url=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
class Blog_posts(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    update_date = models.DateField(auto_now=True)
    read = models.BooleanField(default=False)




class Footer(models.Model):
    about_title = models.CharField(max_length=80, default="About")
    about_text = models.TextField()

    # Social links
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)

    # Contact
    contact_title = models.CharField(max_length=80, default="Contact")
    address = models.TextField()
    phone1 = models.CharField(max_length=50, blank=True, null=True)
    phone2 = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"Footer ({'Published' if self.is_published else 'Draft'})"
