import unittest
from main import create_app
from models.Book import Book

class TestBooks(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db","seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_book_index(self):
        response = self.client.get("/books/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_book_create(self):
        response = self.client.post("/books/", json={
            "title": "test book"
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys())
        
        book = Book.query.get(data["id"])
        self.assertIsNotNone(book)