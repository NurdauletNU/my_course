import React, { useState, useEffect } from "react";
import axios from "axios";

interface Book {
  id: number;
  title: string;
  description: string;
}

function BookList() {
  const [books, setBooks] = useState<Book[]>([]);
  const [currentBookIndex, setCurrentBookIndex] = useState(0);
  const [totalPages, setTotalPages] = useState(0);

  useEffect(() => {
    async function fetchBooks() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/book/");
        setBooks(response.data.serialized_books);
        setTotalPages(response.data.total_pages);
      } catch (error) {
        console.error("Ошибка при получении данных о книгах:", error);
      }
    }

    fetchBooks();
  }, []);

  const handleNextBook = () => {
    if (currentBookIndex < books.length - 1) {
      setCurrentBookIndex(currentBookIndex + 1);
    }
  };

  const handlePrevBook = () => {
    if (currentBookIndex > 0) {
      setCurrentBookIndex(currentBookIndex - 1);
    }
  };

  const currentPage = currentBookIndex + 1;

  return (
    <div>
      <h1>Список книг</h1>
      <div>
        {books.length > 0 && (
          <div>
            <h2>{books[currentBookIndex].title}</h2>
            <p>{books[currentBookIndex].description}</p>
          </div>
        )}
        <div>
          <button onClick={handlePrevBook} disabled={currentBookIndex === 0}>
            Предыдущая книга
          </button>
          <button
            onClick={handleNextBook}
            disabled={currentBookIndex === books.length - 1}
          >
            Следующая книга
          </button>
          <p>
            Страница {currentPage} из {totalPages}
          </p>
        </div>
      </div>
    </div>
  );
}

export default BookList;
