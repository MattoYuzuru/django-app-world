from django.shortcuts import render, HttpResponse


def index_page(request):
    return HttpResponse('Hello, World!')


def post_page(request):
    return HttpResponse('New Page')


def view_post_page(request):
    pass