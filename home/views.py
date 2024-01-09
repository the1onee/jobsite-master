from random import random

from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm #add this
from django.views.generic import DetailView


from . import form
from .models import Request, Namecl, catagry, viewblogs, User, Mohmed, Comment, Startup
from .form import CommentForm, numcom, numcilnt, NewUserForm, postmeta, MohmedForm

# Create your views here.
User = get_user_model()



def viewblog(ret):
    us=ret.user

    if ret.method == 'POST':
        # create a form instance and populate it with data from the request:
        fom = CommentForm(ret.POST, ret.FILES)
        if fom.is_valid():
            new_comment = fom.save(commit=False)



            new_comment.save()



    else:
        fom =CommentForm()


    return render(request=ret, template_name='home/home.html',context={'user':us
                                                                       ,'form':fom})



#--------------------------------- person as def

def viewindexcom(ret,slug):

    usee=User.objects.filter(is_company=True)
    userrre=ret.user

    postname =viewblogs.objects.all().filter(author__is_name=True)
    postcom = viewblogs.objects.all().filter(author__is_company=True)
    userperson=Mohmed.objects.all()
    cat=catagry.objects.all()
    num3="num1"
    us=["Ford", "Volvo", "BMW","gfhgf", "Volvo", "BMW","gfhgf"]
    company=Startup.objects.all().order_by('-slug')[:2]





    return render(ret,'home/indexcompny.html', {'posts':postname,
                                          'postcom': postcom,
                                          'userperson':userperson,
                                          'cat':cat,
                                        'lastes':company,

        'slug':"comany",

                                          'users':userrre})

def viewindex(ret,slug):
    if ret.user.is_name == True:
        usee = User.objects.filter(is_name=True)
        userrre = ret.user

        postname = viewblogs.objects.all()
        postcom = viewblogs.objects.all().filter(author__is_company=True)
        userperson = Mohmed.objects.all()
        cat = catagry.objects.all()
        num3 = ret.user.id
        us = ["Ford", "Volvo", "BMW", "gfhgf", "Volvo", "BMW", "gfhgf"]
        company = viewblogs.objects.filter(author__is_company=True)
        companyy = Startup.objects.filter(name__in=['mrlon'])
    else:
        usee = User.objects.filter(is_company=True)
        userrre = ret.user

        postname = viewblogs.objects.all().filter(author__is_name=True)
        postcom = viewblogs.objects.all().filter(author__is_company=True)
        userperson = Mohmed.objects.all()
        cat = catagry.objects.all()
        num3 = "num1"
        us = ["Ford", "Volvo", "BMW", "gfhgf", "Volvo", "BMW", "gfhgf"]
        company = Startup.objects.filter(name__in=['mrlon', 'ali'])
        companyy = Startup.objects.filter(name__in=['mrlon'])


    if ret.user.is_name == True:
        return render(ret, 'home/index.html', {'posts': postname,
                                               'postcom': postcom,
                                               'userperson': userperson,
                                               'cat': cat,
                                               'lastes': company,
                                               'lastess': companyy,
                                               'slug': num3,

                                               'users': userrre})

    else:
        return render(ret, 'home/indexcompny.html', {'posts': postname,
                                                     'postcom': postcom,
                                                     'userperson': userperson,
                                                     'cat': cat,
                                                     'lastes': company,

                                                     'slug': "comany",

                                                     'users': userrre})








def viewcatogry(ret,slug):
    if ret.user.is_name == True:
        usee = User.objects.filter(is_name=True)
        userrre = ret.user

        postnamee = viewblogs.objects.all()
        postcom = viewblogs.objects.all().filter(author__is_company=True)
        userperson = Mohmed.objects.all()
        cat = catagry.objects.all()
        num3 = "num1"
        us = ["Ford", "Volvo", "BMW", "gfhgf", "Volvo", "BMW", "gfhgf"]
        company = viewblogs.objects.filter(author__is_company=True)

    else:
        usee = User.objects.filter(is_company=True)
        userrre = ret.user

        postnamee = viewblogs.objects.all().filter(author__is_name=True)
        postcom = viewblogs.objects.all().filter(author__is_company=True)
        userperson = Mohmed.objects.all()
        cat = catagry.objects.all()
        num3 = "num1"
        us = ["Ford", "Volvo", "BMW", "gfhgf", "Volvo", "BMW", "gfhgf"]
        company = Startup.objects.filter(name__in=['mrlon', 'ali'])




    userrre=ret.user

    postname =viewblogs.objects.all().filter(catag__slug=slug)




    us=["Ford", "Volvo", "BMW","gfhgf", "Volvo", "BMW","gfhgf"]


    return render(ret,'catgry/catogry.html', {'lastes':postname,

        'slug':us,

                                          'users':userrre,
                                              'posts': postnamee,
                                              'postcom': postcom,
                                              'userperson': userperson,
                                              'cat': cat,
                                              'lastess': company,

                                              'slug': slug,

                                              'users': userrre})




def viewblogforperson(ret,slug):
    if ret.user.is_name==True:
        mod = Mohmed.objects.get(slug=slug)

    else:
        mod = Startup.objects.get(slug=slug)






    view =viewblogs.objects.filter(author__username=slug)
    retor=slug

    if ret.user.is_name == True:
        return render(ret, 'catgry/catforperson.html', {
        'mohmed': mod,
            'hi':retor,
                                          'blogs':view,})
    else:
        return render(ret, 'catgry/catforcom.html', {
            'hi': retor,
        'mohmed': mod,

                                          'blogs':view,






                                          })



def viewedit(ret,slug):
    if ret.user.is_name == True:
        view = Mohmed.objects.get(slug=slug)
    else:
        view = Startup.objects.get(slug=slug)

    view =ret.user
    if ret.method == 'POST':
        # create a form instance and populate it with data from the request:
        fom = MohmedForm(data=ret.POST)
        if fom.is_valid():
            new_comment = fom.save(commit=False)
            new_comment.user=view

            new_comment.save()

            if ret.user.is_name == True:
                return HttpResponseRedirect('http://127.0.0.1:8000/index/'+str(ret.user))
            else:
                return HttpResponseRedirect('http://127.0.0.1:8000/indexcom/'+str(ret.user))




    else:
        fom = MohmedForm()

    if ret.user.is_name == True:
        return render(ret,'edit/edit.html',{'form': fom })
    else:
        return render(ret, 'edit/editcom.html', {'form': fom})




def viewportfilo(ret,slug):
    if ret.user.is_name == True:
        porrt=Mohmed.objects.get(slug=slug)
    else:
        porrt=Startup.objects.get(slug=slug)


    sell=slug

    sl = "admin"

    if ret.user.is_name == True:
        return render(ret, 'portfilo/index.html', {
            'ret':slug,'rett':ret.user,
            'formm': porrt,
        'sell':sell,
        })
    else:
        return render(ret, 'portfilo/indexcom.html', {
            'ret': slug,'rett':ret.user,
            'formm': porrt,
        'sell':sell,
        })








def viewpostshre(ret,slug):
    if ret.user.is_name == True:
        porrt = Mohmed.objects.get(slug=slug)
    else:
        porrt = Startup.objects.get(slug=slug)
    sl = "admin"
    view = ret.user
    if ret.method == 'POST':
        # create a form instance and populate it with data from the request:
        fom =postmeta(ret.POST,ret.FILES)
        if fom.is_valid():
            new_comment = fom.save(commit=False)

            new_comment.author=view

            new_comment.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/index/'+str(ret.user))


    else:
        fom = postmeta()


    return render(ret,'post/share.html',{'post':  porrt ,'form': fom })



#---------------------------------------------------read blog
def viewblogread(ret,slug):

    if ret.user.is_name == True:
        porrt = Mohmed.objects.get(slug=slug)
    else:
        porrt = Startup.objects.get(slug=slug)
    view =ret.user

    fom=viewblogs.objects.get(slug=slug)
    hi=slug



    com = fom.comments.filter(active=True)

    new_comment = None
    if ret.method == 'POST':
        comment_form = CommentForm(data=ret.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = fom
            new_comment.postore=ret.user

            new_comment.save()
    else:
        comment_form = CommentForm()



    return render(ret,'edit/readblog.html',{'mohmed': porrt,
                                            'blogs': fom,
                                            'comm': com,
                                            'hi':hi,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form
                                              })





def signup(request):
    r=True
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            user.is_name=True
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('http://127.0.0.1:8000/index/'+str(request.user))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name='login/sinup.html', context={"register_form": form})


def signup_com(request):
    r=True
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_company=True
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('http://127.0.0.1:8000/indexcom/'+str(request.user))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name='login/sing_com.html', context={"register_form": form})





def login_request(request):


    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('http://127.0.0.1:8000/index/' + str(request.user))



            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login/log.html", context={"form":form})

def logout_request(request):
    logout(request)  # Call the logout function
    return redirect('http://127.0.0.1:8000/')


#-----------------------------------------------company def



def viewblogforcomp(ret,slug):
    mod = Startup.objects.get(slug=slug)
    rett=slug


    view =viewblogs.objects.filter(author__username=slug)

    return render(ret, 'catgry/catforperson.html', {
        'mohmed': mod,'ret':rett,
                                          'blogs':view,





                                          })

def viewblogreadcom(ret,slug):
    view =ret.user
    porrt = Startup.objects.get(user=ret.user)
    fom=viewblogs.objects.get(slug=slug)


    hi=slug
    com = fom.comments.filter(active=True)

    new_comment = None
    if ret.method == 'POST':
        comment_form = CommentForm(data=ret.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = fom
            new_comment.postore=ret.user
            fom.clean_fields()
            new_comment.save()
            n=range

    else:
        comment_form = CommentForm()



    return render(ret,'edit/readblogcom.html',{'mohmed': porrt,
                                            'blogs': fom,
                                            'comm': com,
                                               "hi":hi,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form
                                              })

def viewblogforcom(ret,slug):
    mod = Startup.objects.get(slug=slug)
    rett=slug


    view =viewblogs.objects.filter(author__username=slug)

    return render(ret, 'catgry/catforperson.html', {
        'mohme': mod,'ret':rett,
                                          'blogs':view,





                                          })


