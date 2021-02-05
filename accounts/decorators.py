from django.http import HttpResponse
# from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

# def unauthenticated_user(view_func):
# 	def wrapper_func(request, *args, **kwargs):
# 		if request.user.is_authenticated:
# 			return redirect('home')
# 		else:
# 			return view_func(request, *args, **kwargs)

# 	return wrapper_func

def role_required(allowed_roles=[]):
	def decoration(view_func):
		def wrap(request,*args,**kwargs):
			if request.role in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponseRedirect(reverse('You are not authorized to view this page'))	

		return decorator


def admin_only(allowed_roles=[]):
	
		def wrap(request,*args,**kwargs):
			if request.role == "Admin":
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponseRedirect(reverse('You are not authorized to view this page'))	

		return wrap

# def allowed_users(allowed_roles=[]):
# 	def decorator(view_func):
# 		def wrapper_func(request, *args, **kwargs):

# 			group = None
# 			if request.user.groups.exists():
# 				group = request.user.groups.all()[0].name

# 			if group in allowed_roles:
# 				return view_func(request, *args, **kwargs)
# 			else:
# 				return HttpResponse('You are not authorized to view this page')
# 		return wrapper_func
# 	return decorator

# def admin_only(view_func):
# 	def wrapper_function(request, *args, **kwargs):
# 		group = None
# 		if request.user.groups.exists():
# 			group = request.user.groups.all()[0].name

# 		if group == 'customer':
# 			return redirect('user-page')

# 		if group == 'admin':
# 			return view_func(request, *args, **kwargs)

# 	return wrapper_function
