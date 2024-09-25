# Sprint_4
## Краткое описание тестов:  
1. `test_add_new_book_add_two_books` - проверяет добавление двух книг  
2. `test_set_book_genre_success` - проверяет, что жанр книги устанавливается при наличии книги и жанра в списках  
3. `test_set_book_genre_if_genre_not_in_list` - проверяет, что жанр книги не устанавливается, если жанра нет в списке  
4. `test_get_book_genre_existing_book_in_list` - проверяет, что выводится текущий словарь по имени книги, существующей в списке  
5. `test_get_book_genre_not_existing_book_in_list` - проверяет, что метод возвращает None, если книги нет в списке  
6. `test_get_books_with_specific_genre` - проверяет вывод списка книг с определенным жанром  
7. `test_get_books_for_children_only_for_children` - проверяет, что возвращаются жанры, подходящие для детей
8. `test_get_books_genre` - проверяет, что метод возвращает словарь с книгами и жанрами
9. `test_get_books_for_children_no_age_rating` - проверяет, что книги из genre_age_rating не возвращаются
10. `test_add_book_in_favorites` - проверяет, что книга добавляется в избранное
11. `test_delete_book_from_favorites` - проверяет, что книга удаляется из избранного, если она там есть
12. `test_get_list_of_favorites_books` - проверяет получение списка избранного  

### Фикстуры вынесены в отдельный файл conftest.py  