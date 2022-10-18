from django.shortcuts import redirect, render , get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def books(request):
	search = Book.objects.all()
	title = None
	if 'search_name' in request.GET:
		title = request.GET['search_name']
		if title:
			search = search.filter(title__icontains = title)

	context = {
		'categories': Category.objects.all(),
		'books': search,
		'category_form': CategoryForm(),
		}
	return render(request , 'pages/books.html', context)


def delete(request, id):
	book_del = get_object_or_404(Book , id = id)
	if request.method == 'POST':
		book_del.delete()
		return redirect('/')
	return render(request , 'pages/delete.html')


def index(request):
	if request.method == 'POST':
		new_book = BookForm(request.POST, request.FILES)
		if new_book.is_valid():
			new_book.save()
		new_category = CategoryForm(request.POST)
		if new_category.is_valid():
			new_category.save()
		
	context = {
		'categories': Category.objects.all(),
		'books': Book.objects.all(),
		'form': BookForm(),
		'category_form': CategoryForm(),
		'allbooks': Book.objects.filter(active=True).count(),
		'soldbooks': Book.objects.filter(status = 'sold').count(),
		'rentalbooks': Book.objects.filter(status = 'rental').count(),
		'avialblebooks': Book.objects.filter(status = 'availble').count(),

		}
	return render(request , 'pages/index.html',context)


def update(request, id):
	book_id = Book.objects.get(id = id)
	if request.method == 'POST':
		book_save = BookForm(request.POST, request.FILES, instance= book_id)
		if book_save.is_valid:
			book_save.save()
	else:
		book_save = BookForm(instance=book_id)

	context = {
		'form':book_save
	}
	return render(request , 'pages/update.html', context)