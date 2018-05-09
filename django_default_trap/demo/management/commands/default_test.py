from django.core.management.base import BaseCommand
from django_default_trap.demo.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        book1 = Book(name='Book 1')
        print('book1.author = %s' % book1.detail.get('author'))
        book1.detail['author'] = 'Steven'
        print('book1.author = %s' % book1.detail.get('author'))
        book1.save()
        print('book1 saved.')

        book2 = Book(name='Book 2')
        print('book2.author = %s' % book2.detail.get('author'))
        book2.save()
