from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, UpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from .models import Account
from story.models import StoryBook
from django.db import IntegrityError
from django.contrib import messages


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
	else:
		form = RegistrationForm()

	context['registration_form'] = form
	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')

def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST, request.FILES)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return redirect("home")

		else:
			context['error'] = "Invalid email or password"
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, "account/login.html", context)

def update_view(request): 
	context = {}
	if request.method == 'POST':
		form = UpdateForm(request.POST, request.FILES)
		
		user = request.POST.get('username')
		email = request.POST.get('email')
		image = request.FILES.get('image')
		old_password = request.POST.get('old_pass')
		new_password = request.POST.get('new_pass')
		
		member = Account.objects.get(username=request.user.username)
		if user != member.username and Account.objects.filter(username=user).exists():
			context['username_error'] = "Username already exists!"
		elif email != member.email and Account.objects.filter(email=email).exists():
			context['email_error'] = "Email already exists!"
		elif not check_password(old_password, member.password) and new_password:
			context['password_error'] = "Old password is incorrect!"
		else:
			old_username = member.username
			member.username = user
			member.email = email
			if image:
				member.profile_picture = image
			if new_password:
				member.set_password(new_password)  # This hashes and sets the new password
			member.save()
			change_storybook_username(old_username, user)

			update_session_auth_hash(request, member)
			return redirect("stories")
	else:
		form = UpdateForm()

	context['form'] = form
	return render(request, 'account/update.html', context)

def change_storybook_username(old_username, new_username):
	storybooks = StoryBook.objects.filter(username=old_username)
	for storybook in storybooks:
		storybook.username = new_username
		storybook.save()