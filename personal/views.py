from django.shortcuts import render
from story.models import StoryBook
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def home_screen_view(request):
    context = {}
    rating = 0.0
    owner_books = StoryBook.objects.filter(username=request.user.username)
    all_books = StoryBook.objects.filter(is_public=True) # only public books will be displayed
    genres = []
    for book in all_books:
        genres.append(book.description)

    genres = list(set(genres))
    context['story_books'] = all_books
    context['book_count'] = len(owner_books)
    for book in owner_books:
        rating += book.rating
    if len(owner_books) > 0:
        context['owner_rating'] = rating/len(owner_books)
    else:
        context['owner_rating'] = 0.0
    context['ratings'] = [1.0, 2.0, 3.0, 4.0, 5.0]
    context['genres'] = genres
    return render(request, 'personal/home.html', context)


def rating(request, story_book_id, rate):
    story_book = get_object_or_404(StoryBook, id=story_book_id)
    story_book.add_rating(float(rate))
    return JsonResponse({'message': 'success'}, status=200)