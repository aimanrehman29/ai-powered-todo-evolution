import unittest

from todo.store import TaskNotFoundError, TaskStore


class TaskStoreTests(unittest.TestCase):
    def test_add_and_list_returns_tasks(self) -> None:
        store = TaskStore()
        first = store.add("First task", "Alpha")
        second = store.add("Second task", "Beta")

        tasks = store.list_all()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)
        self.assertEqual(tasks[0].status, "open")
        self.assertEqual(tasks[1].status, "open")

    def test_update_changes_fields(self) -> None:
        store = TaskStore()
        created = store.add("Title", "Desc")

        updated = store.update(created.id, title="New Title", description="New Desc")

        self.assertEqual(updated.title, "New Title")
        self.assertEqual(updated.description, "New Desc")
        self.assertFalse(updated.completed)

    def test_update_requires_field(self) -> None:
        store = TaskStore()
        created = store.add("Title", "Desc")

        with self.assertRaises(ValueError):
            store.update(created.id)

    def test_toggle_flips_status(self) -> None:
        store = TaskStore()
        created = store.add("Title", "Desc")

        toggled = store.toggle(created.id)
        self.assertTrue(toggled.completed)

        toggled_again = store.toggle(created.id)
        self.assertFalse(toggled_again.completed)

    def test_delete_removes_task_and_unknown_id_errors(self) -> None:
        store = TaskStore()
        created = store.add("Title", "Desc")

        removed = store.delete(created.id)
        self.assertEqual(removed.id, created.id)
        self.assertEqual(store.list_all(), [])

        with self.assertRaises(TaskNotFoundError):
            store.delete(created.id)

    def test_unknown_id_on_update_raises(self) -> None:
        store = TaskStore()
        store.add("Existing", "Task")

        with self.assertRaises(TaskNotFoundError):
            store.update(99, title="Nope")

    def test_add_allows_duplicate_titles_with_unique_ids(self) -> None:
        store = TaskStore()
        first = store.add("Repeated", "First")
        second = store.add("Repeated", "Second")

        self.assertNotEqual(first.id, second.id)
        self.assertEqual(first.title, second.title)
        self.assertEqual(store.list_all()[0].status, "open")


if __name__ == "__main__":
    unittest.main()
