from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Business
from .forms import BusinessForm

# Create your views here.
def home(request):

	context = {

	"title" : " Random Business "
	}

	return render(request, 'home.html', context)


def business_list(request):

	objects = Business.objects.all()
	context = {

	"objects" : objects
	}

	return render(request, 'business_list.html', context)


def business_detail(request,business_id):
	detail = Business.objects.get(id=business_id)

	context= {
	"business": detail
	}

	return render(request, 'business_detail.html',context)


def business_create(request):
	form = BusinessForm(request.POST or None)
	if form.is_valid():
		form.save()

		return redirect("business_list")

	context = {
	"form":form
	}

	return render(request,"business_create.html",context)


def business_update(request,business_id):
	item = Business.objects.get(id=business_id)
	form = PostForm(instance = item)
	if request.method == "POST":

		form = PostForm(request.POST or None, instance = item)

		
		if form.is_valid():
			form.save()
			return redirect("business_list")

	context = {

	"form": form,
	"item": item,	

	}

	return render(request, "business_update.html", context)



def business_delete(request,post_id):
	Post.objects.get(id=post_id).delete()

	return redirect("business_list")


	