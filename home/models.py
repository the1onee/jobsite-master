from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.
from mywork import settings

class User(AbstractUser):
    is_name = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Request(models.Model):
    name = models.CharField("name",max_length=64)
    email = models.EmailField(_("email"),max_length=64)

    meassg = models.TextField("message",max_length=64)

    def __str__(self):
        return self.name





class Mohmed(models.Model):

    name = models.CharField(_("name:"),max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    img=models.ImageField(("img"),upload_to='profile',blank=True,null=True)
    slug = models.SlugField(_("slug"), blank=True, null=True)
    skis_name=models.TextField(_("skills"),blank=True, null=True)
    aboutme = models.TextField(_("about me "), blank=True, null=True)



    #about your
    phone = models.CharField(_("phone"),max_length=12, blank=True, null=True)
    address=models.CharField(_("your address"),max_length=50, blank=True, null=True)
    email=models.EmailField(_("email"))
    dgree=models.CharField(_("Dgree"),max_length=50, blank=True, null=True)
    experns=models.IntegerField(_("experns"), blank=True, null=True)
    brith=models.DateField(_("brithday"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Mohmed, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Mohmed")
        verbose_name_plural = _("Mohmeds")

    def __str__(self):
        return self.name




class Startup(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    year_founded = models.IntegerField()
    about = models.TextField()
    slug = models.SlugField(_("slug"), blank=True, null=True)
    website = models.URLField()
    logo = models.ImageField(upload_to='startup_logos/')
    address = models.TextField()
    employee_count = models.IntegerField()
    founder = models.CharField(max_length=100)
    founder_email = models.EmailField()
    founder_phone = models.CharField(max_length=20)
    video_pitch = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Startup, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Namecompany(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name







class Namecl(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    pub_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    img=models.ImageField(("imgg"),upload_to='profile',blank=True,null=True)
    born = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)


    # --------------
    pohon = models.CharField(max_length=14,null=True, blank=True)

    alqsm = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
             self.slug = slugify(self.user)
             return super().save(*args, **kwargs)

    def __str__(self):
        return self.name








#-----------------------------------------------

PROFESSION_CHOICES = [    ('software_developer', 'Software Developer'),    ('data_scientist', 'Data Scientist'),    ('network_engineer', 'Network Engineer'),    ('information_security_analyst', 'Information Security Analyst'),    ('technical_support_specialist', 'Technical Support Specialist'),    ('systems_administrator', 'Systems Administrator'),    ('technical_project_manager', 'Technical Project Manager'),    ('ux_designer', 'User Experience Designer'),    ('technical_writer', 'Technical Writer'),    ('it_manager', 'IT Manager'),    ('cloud_engineer', 'Cloud Engineer'),    ('devops_engineer', 'DevOps Engineer'),    ('qa_engineer', 'Quality Assurance Engineer'),    ('business_analyst', 'Business Analyst'),    ('database_administrator', 'Database Administrator'),    ('mobile_app_developer', 'Mobile App Developer'),    ('game_developer', 'Game Developer'),    ('ai_engineer', 'Artificial Intelligence Engineer'),    ('machine_learning_engineer', 'Machine Learning Engineer'),    ('robotics_engineer', 'Robotics Engineer'),]

class catagry(models.Model):
    name = models.CharField(max_length=255, choices=PROFESSION_CHOICES)
    slug = models.SlugField(max_length=255,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(catagry, self).save(*args, **kwargs)

    def __str__(self):

        return self.name

class viewblogs(models.Model):

    title = models.CharField(_("title:"), max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(_("slug"),max_length=200, unique=True)
    img = models.ImageField(("img"), upload_to='profilee', blank=True, null=True)
#------------------------------

    body = RichTextField(_("body"),blank=True, null=True)
    updated_on = models.DateTimeField(_("updated_on"),auto_now=True)
    catag = models.ForeignKey(catagry, on_delete=models.CASCADE, related_name='catagry', blank=True, null=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(_("created "),auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(viewblogs, self).save(*args, **kwargs)




    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    postore = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postforyour')
    slug = models.SlugField(_("slug"), max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(
        viewblogs, on_delete=models.CASCADE, related_name='comments')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.postore)
        super(Comment, self).save(*args, **kwargs)




    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

