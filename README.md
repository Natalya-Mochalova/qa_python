# Финальный проект 4 спринта  "Юнит-тестирование"

## Набор тестов:
- Тест 1: Проверка добавления двух книг
  ##### test_add_new_book_add_two_books_added

- Тест 2: Проверка граничных значений длины названия книги (параметризация)   
  ##### test_add_new_book_zero_and_long_name_not_added

- Тест 3: Проверка невозможности добавления дубликата
  ##### test_add_new_book_duplicate_name_not_added
        
- Тест 4: Установка допустимого жанра для существующей книги
  ##### test_set_book_genre_valid_genre_set

- Тест 5: Нельзя установить недопустимый жанр для существующей книги
  ##### test_cannot_set_invalid_genre_for_existing_book_not_set

- Тест 6: Нельзя установить жанр для несуществующей книги
  ##### test_cannot_set_genre_for_nonexistent_book_not_set

- Тест 7: Получение книг по конкретному жанру
  ##### test_get_books_with_specific_genre_returns_correct_list

- Тест 8: Получение книг для детей (без возрастного рейтинга)
  ##### test_get_books_for_children_returns_correct_list

- Тест 9: Добавление книги в избранное
  ##### test_add_book_in_favorites_added

- Тест 10: Нельзя добавить несуществующую книгу в избранное
  ##### test_cannot_add_nonexistent_book_to_favorites_not_added

- Тест 11: Удаление книги из избранного
  ##### test_delete_book_from_favorites_removed_delete