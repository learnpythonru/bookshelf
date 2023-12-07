from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from books.models import Book


def display_books_with_http(request: HttpRequest) -> HttpResponse:
    entities = Book.objects.all()

    if not entities:
        return HttpResponseNotFound('Ничего не найдено')

    return render(request=request, template_name='all_books.html', context={'books': entities})


def display_book_by_id_with_http(
    request: HttpRequest,
    book_id: int
) -> HttpResponse | HttpResponseNotFound:
    try:
        entity = Book.objects.get(pk=book_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ничего не найдено')

    return render(request=request, template_name='one_book.html', context={'book': entity})


def display_books_with_json(request: HttpRequest) -> JsonResponse | HttpResponseNotFound:
    entities = Book.objects.all()

    if not entities:
        return HttpResponseNotFound('Ничего не найдено')

    return JsonResponse(
        data=[
            {
                'title': entity.title,
                'author_full_name': entity.author_full_name,
                'year_of_publishing': entity.year_of_publishing,
                'copies_printed': entity.copies_printed,
            } for entity in entities
        ],
        safe=False
    )


def display_book_by_id_with_json(
    request: HttpRequest,
    book_id: int
) -> JsonResponse | HttpResponseNotFound:
    try:
        entity = Book.objects.get(pk=book_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ничего не найдено')
    return JsonResponse(
        data={
            'title': entity.title,
            'author_full_name': entity.author_full_name,
            'year_of_publishing': entity.year_of_publishing,
            'copies_printed': entity.copies_printed,
        },
        safe=False
    )
