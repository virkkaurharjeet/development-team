import unittest
from todolist import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_item(self):
        self.todo_list.add_item("Test Task")
        self.assertEqual(len(self.todo_list.items), 1)
        self.assertEqual(self.todo_list.items[0]["title"], "Test Task")
        self.assertIsNone(self.todo_list.items[0]["deadline"])
        self.assertFalse(self.todo_list.items[0]["completed"])

    def test_add_item_with_deadline(self):
        self.todo_list.add_item("Test Task", "2023-12-31")
        self.assertEqual(self.todo_list.items[0]["deadline"], "2023-12-31")

    def test_add_item_empty_title(self):
        with self.assertRaises(ValueError):
            self.todo_list.add_item("")

    def test_edit_item_title(self):
        self.todo_list.add_item("Task 1")
        self.todo_list.edit_item(0, title="Updated Task 1")
        self.assertEqual(self.todo_list.items[0]["title"], "Updated Task 1")

    def test_edit_item_deadline(self):
        self.todo_list.add_item("Task 1", "2023-12-01")
        self.todo_list.edit_item(0, deadline="2023-12-31")
        self.assertEqual(self.todo_list.items[0]["deadline"], "2023-12-31")

    def test_edit_item_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.edit_item(1, title="Non-existent Task")

    def test_complete_item(self):
        self.todo_list.add_item("Task 1")
        self.todo_list.complete_item(0)
        self.assertTrue(self.todo_list.items[0]["completed"])

    def test_complete_item_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.complete_item(1)

    def test_delete_item(self):
        self.todo_list.add_item("Task 1")
        self.todo_list.delete_item(0)
        self.assertEqual(len(self.todo_list.items), 0)

    def test_delete_item_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.delete_item(0)

    def test_get_all_items(self):
        self.todo_list.add_item("Task 1")
        self.todo_list.add_item("Task 2")
        all_items = self.todo_list.get_all_items()
        self.assertEqual(len(all_items), 2)
        self.assertEqual(all_items[0]["title"], "Task 1")
        self.assertEqual(all_items[1]["title"], "Task 2")

if __name__ == '__main__':
    unittest.main()