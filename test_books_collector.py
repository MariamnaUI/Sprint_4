import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self,collector_add_book):

        assert len(collector_add_book.get_books_genre()) == 2


    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Комедии'),
        ('Зловещие мертвецы', 'Ужасы')
    ])
    def test_set_book_genre_success(self, collector_add_book, name, genre):
        collector_add_book.add_new_book(name)
        collector_add_book.set_book_genre(name, genre)

        assert collector_add_book.get_book_genre(name) == genre


    def test_set_book_genre_if_genre_not_in_list(self, collector_add_book):
        collector_add_book.set_book_genre('Гордость и предубеждение и зомби', 'Мелодрамы')

        assert  collector_add_book.get_book_genre('Гордость и предубеждение и зомби') == ''


    def test_get_book_genre_existing_book_in_list(self, collector_add_book):
        collector_add_book.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')

        assert collector_add_book.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'


    def test_get_book_genre_not_existing_book_in_list(self, collector):

        assert collector.get_book_genre('Отсутствующая книга') is None


    def test_get_books_with_specific_genre(self, collector_add_book):
        collector_add_book.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')

        assert collector_add_book.get_books_with_specific_genre('Комедии') == ['Гордость и предубеждение и зомби']


    def test_get_books_for_children_only_for_children(self, collector):
        collector.add_new_book('Детская книга 1')
        collector.set_book_genre('Детская книга 1','Мультфильмы')

        collector.add_new_book('Детская книга 2')
        collector.set_book_genre('Детская книга 2','Фантастика')

        books_for_children = collector.get_books_for_children()
        assert 'Детская книга 1' in books_for_children
        assert 'Детская книга 2' in books_for_children


    def test_get_books_genre(self, collector_add_book):
        collector_add_book.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')

        books_genre = collector_add_book.get_books_genre()
        assert books_genre == {'Гордость и предубеждение и зомби': 'Комедии',
                               'Зловещие мертвецы': ''}


    def test_get_books_for_children_no_age_rating(self, collector_add_book):
        collector_add_book.add_new_book('Детская книга 1')
        collector_add_book.set_book_genre('Детская книга 1', 'Мультфильмы')

        collector_add_book.add_new_book('Детская книга 2')
        collector_add_book.set_book_genre('Детская книга 2', 'Ужасы')

        books_for_children = collector_add_book.get_books_for_children()
        assert 'Детская книга 1' in books_for_children
        assert 'Детская книга 2' not in books_for_children


    def test_add_book_in_favorites(self, collector_add_book):
        collector_add_book.add_book_in_favorites('Гордость и предубеждение и зомби')

        favorites = collector_add_book.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites


    def test_delete_book_from_favorites(self,collector_add_book):
        collector_add_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_add_book.delete_book_from_favorites('Гордость и предубеждение и зомби')

        favorites = collector_add_book.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' not in favorites


    def test_get_list_of_favorites_books(self,collector_add_book):
        collector_add_book.add_book_in_favorites('Гордость и предубеждение и зомби')

        favorites = collector_add_book.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites
