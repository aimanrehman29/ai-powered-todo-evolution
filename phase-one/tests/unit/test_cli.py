import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from todo import cli
from todo.store import TaskStore


class CliTests(unittest.TestCase):
    def _run(self, argv, store: TaskStore):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = cli.run(argv, store=store)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_cli_add_and_list_outputs_task(self) -> None:
        store = TaskStore()
        code, _, _ = self._run(["add", "Test task", "--description", "Details"], store)
        self.assertEqual(code, 0)

        code, out, _ = self._run(["list"], store)
        self.assertEqual(code, 0)
        self.assertIn("Test task", out)
        self.assertIn("(open)", out)

    def test_update_requires_field_returns_error(self) -> None:
        store = TaskStore()
        self._run(["add", "Task"], store)

        code, _, err = self._run(["update", "1"], store)

        self.assertEqual(code, 1)
        self.assertIn("Provide at least one field to update", err)

    def test_toggle_unknown_id_returns_error(self) -> None:
        store = TaskStore()

        code, _, err = self._run(["toggle", "5"], store)

        self.assertEqual(code, 1)
        self.assertIn("not found", err)

    def test_delete_removes_task(self) -> None:
        store = TaskStore()
        self._run(["add", "Keep"], store)
        self._run(["add", "Remove"], store)

        code, _, _ = self._run(["delete", "1"], store)
        self.assertEqual(code, 0)

        code, out, _ = self._run(["list"], store)
        self.assertEqual(code, 0)
        self.assertNotIn("[1]", out)
        self.assertIn("[2]", out)

    def test_add_rejects_empty_title(self) -> None:
        store = TaskStore()

        code, _, err = self._run(["add", ""], store)

        self.assertEqual(code, 1)
        self.assertIn("Title is required", err)

    def test_add_allows_duplicate_titles_and_prints_confirmation(self) -> None:
        store = TaskStore()

        code1, out1, _ = self._run(["add", "Dup"], store)
        code2, out2, _ = self._run(["add", "Dup"], store)

        self.assertEqual(code1, 0)
        self.assertEqual(code2, 0)
        self.assertIn("Added task 1: Dup", out1)
        self.assertIn("Added task 2: Dup", out2)

        code, out, _ = self._run(["list"], store)
        self.assertEqual(code, 0)
        self.assertIn("[1]", out)
        self.assertIn("[2]", out)


if __name__ == "__main__":
    unittest.main()
