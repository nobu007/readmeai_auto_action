import unittest
import subprocess


class TestAction(unittest.TestCase):
    def test_action_runs(self):
        # アクションが正しく実行されるかを確認するための簡単なテスト
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)  # 正常終了を確認


if __name__ == "__main__":
    unittest.main()
