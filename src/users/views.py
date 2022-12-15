from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings


from .forms import NewUserForm


# Create your views here.

def sign_up_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful"))
            return redirect('home')
    
    else:
        form = NewUserForm()
    return render(request, 'authenticate/sign_up.html', {'form': form})


# https://stackoverflow.com/questions/38431166/redirect-to-next-after-login-in-django  Rune kaagard's answer. 
# He suggests it is a more secure way of redirecting to a url from the login.
# Method 2 is documented below


def _redirect_after_login(request):
    nxt = request.POST.get("next", None)
    print('Next here', nxt)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    # don't fully understand this branch
    elif not url_has_allowed_host_and_scheme(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
       
    else:
        return redirect(nxt)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return _redirect_after_login(request) # have to implement going straight to to their feed later. ie login ---straight to---> feed when the user was not first redirected to login
        else:
            messages.error(request, ("There was an error with your login attempt. Try again."))
            return redirect('login')    
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out successfully."))
    return redirect('home')




#---- Redirecting the user to their intended page after redirecting them to first login. ---#
# Method 2. From an online article.


'''
def login_user(request):

    valuenext= request.POST.get('next')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and valuenext=='':
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('home')

        if user is not None and valuenext != '':
            login(request, user)
            messages.success(request, "Your feed")
            context= {'valuenext': valuenext}
            return redirect(valuenext)
        else:
            messages.success(request, "Nope")
            return render(request, 'authenticate/login.html', {})
        
        #if user is not None:
         #   login(request, user)
          #  return _redirect_after_login(request) # have to implement going straight to to their feed later 
            #return redirect(request.GET.get('next', 'home'))
        #else:
         #   messages.error(request, ("There was an error with your login attempt. Try again."))
          #  return redirect('login')    
    else:
        return render(request, 'authenticate/login.html', {})

'''
