import pytest


from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
  
    @pytest.mark.parametrize('book', ['','Удивительное путешествие Нильса Хольгерсс'])
    def test_add_new_book_zero_and_long_name_not_added(self, book, collector):
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_name_not_added(self, collector):
        book_name = 'Идиот'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_set(self, collector):
        book_name = 'Колобок'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_cannot_set_invalid_genre_for_existing_book_not_set(self, collector):
        book_name = 'Существующая книга'
        invalid_genre = 'Не жанр'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == ''

    def test_cannot_set_genre_for_nonexistent_book_not_set(self, collector):
            non_existent_book = 'Несуществующая книга'
            valid_genre = 'Фантастика'
            collector.set_book_genre(non_existent_book, valid_genre)
            assert non_existent_book not in collector.get_books_genre()

    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_1', 'Детективы')
        collector.set_book_genre('Книга_2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга_2']

    def test_get_books_for_children_returns_correct_list(self, collector):
        collector.add_new_book('Детская книга')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Детская книга', 'Фантастика')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        assert collector.get_books_for_children() == ['Детская книга']

    def test_add_book_in_favorites_added(self, collector):
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_cannot_add_nonexistent_book_to_favorites_not_added(self, collector):
        non_existent_book = 'Книга, которой нет в коллекции'
        collector.add_book_in_favorites(non_existent_book)
        assert non_existent_book not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removed_delete(self, collector):
        book_name = 'Идиот'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()