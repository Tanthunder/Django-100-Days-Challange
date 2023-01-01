from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from .forms import CodeForm
from app1.models import CustomUser
from app2.models import Code
from .utils import email

@login_required
def home(request):
    return render(request, 'app2/index.html',{})

def auth_view(request):
    """Authenticate user and store user id in session."""
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('verify')
    return render(request, 'app2/code_form.html',{'form':form})

def verify(request):
    """Verify code sent in mail and let user login."""
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}:{code}"

        if not request.POST:
            #send mail with code
            email(code_user,user.email)

        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
    return render(request, 'app2/verify.html',{'form':form})