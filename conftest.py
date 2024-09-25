import pytest

from main import BooksCollector

# создаем новый экземпляр класса BooksCollector()
@pytest.fixture
def collector():
    return BooksCollector()

# добавляем в экземпляр BooksCollector() две книги
@pytest.fixture
def collector_add_book(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Зловещие мертвецы')
    return collector
