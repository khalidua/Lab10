import unittest
from app import addTask, get_tasks,tasks

class TestTaskFunctions(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        addTask("Buy groceries")
        self.assertIn("Buy groceries", tasks)

    def test_get_tasks(self):
        addTask("Buy groceries")
        addTask("Clean the house")
        task_list = get_tasks()
        self.assertEqual(task_list, ["Buy groceries", "Clean the house"])

if __name__ == '__main__':
    unittest.main()
