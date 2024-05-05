from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import StoryBook, TextEntry
from account.models import Account
import prompTale
import json

def create_story(request):
	if request.method == 'POST':
		prompt_text = request.POST.get('input_prompt')

	story_book_id = prompTale.generateStory(prompt_text, request.user.username)

	story_book = get_object_or_404(StoryBook, id=story_book_id)
	story_book_pages = story_book.text.all()
	story_book_images = story_book.images.all()
	content = zip(story_book_pages, story_book_images)

	context = {'Title': story_book.title,
			   'content': content,
			   'Id': story_book.id}
	
	return render(request, 'story/create.html', context)



def edit_story(request, story_book_id):
	story_book = get_object_or_404(StoryBook, id=story_book_id)
	story_book_pages = story_book.text.all()
	story_book_images = story_book.images.all()
	content = zip(story_book_pages, story_book_images)
	context = {'Title': story_book.title,
			   'content': content,
			   'Id': story_book.id}
	return render(request, 'story/create.html', context)


def my_stories(request):
	# retrieving the story books of the user
	rating = 0.0
	context = {}
	story_books = StoryBook.objects.filter(username=request.user.username)
	for book in story_books:
		rating += book.rating

	if len(story_books) > 0:
		context['owner_rating'] = rating/len(story_books)
	else:
		context['owner_rating'] = 0.0
	context['story_books'] = story_books
	context['book_count'] = len(story_books)
	context['ratings'] = [1.0, 2.0, 3.0, 4.0, 5.0]
	return render(request, 'story/stories.html', context)


def save_story(request, story_book_id):
	if request.method == 'POST':
		try:
			story_book = get_object_or_404(StoryBook, id=story_book_id)
			story_book.title = request.POST.get('title')
			story_book.text.clear() #if id exists, delete the existing text
			story_book.save()
		except:
			title = request.POST.get('title')
			description = 'hello'
			is_public = request.POST.get('is_public') == 'on'  # Assuming is_public is a checkbox

			# Create a new instance of the StoryBook model
			story_book = StoryBook(
				username = request.user.username,
				title=title,
				description=description,
				is_public=is_public
			)
			story_book.save()

		# adding pages to story book
		for i in range(1, 6): 
			page_text = request.POST.get("text" + str(i))
			page_color = request.POST.get("color" + str(i))
			page_font = request.POST.get("font" + str(i))
			print(page_font)
			print(page_color)
			text_entry = TextEntry.objects.create(text=page_text, color=page_color, font=page_font)
			story_book.text.add(text_entry)


	return redirect('stories')


def delete_story_book(request, story_book_id):
	story_book = get_object_or_404(StoryBook, id=story_book_id)
	if (story_book.username == request.user.username): # if request is initiated by the true owner
		story_book.delete()
		return JsonResponse({'message': 'success'}, status=200)
	return JsonResponse({'message': 'not found'}, status=200)

def make_public(request, story_book_id):
	story_book = get_object_or_404(StoryBook, id=story_book_id)
	new_status = story_book.is_public != True
	story_book.set_public_status(new_status)
	return JsonResponse({'message': 'success'}, status=200)

def view_story(request, story_book_id):
	story_book = get_object_or_404(StoryBook, id=story_book_id)
	story_book_pages = story_book.text.all()
	story_book_images = story_book.images.all()
	content = zip(story_book_pages, story_book_images)
	context = {'Title': story_book.title,
			   'content': content,
			   'Id': story_book.id}
	return render(request, 'story/view.html', context)

def download_story(request, story_book_id, title):
	story_book = get_object_or_404(StoryBook, id=story_book_id)
	story_book_pages = story_book.text.all()
	story_book_images = story_book.images.all()
	content = zip(story_book_pages, story_book_images)
	context = {'Title': story_book.title,
			   'content': content,
			   'Id': story_book.id}
	return render(request, 'story/download.html', context)
