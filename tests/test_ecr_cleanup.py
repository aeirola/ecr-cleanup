from unittest import TestCase

from ecr_cleanup.ecr_cleanup import main

class TestMain(TestCase):

    def test_help(self):
        with self.assertRaises(SystemExit) as cm:
            main(['-h'])

        self.assertEqual(cm.exception.code, 0)

    def test_missing(self):
        with self.assertRaises(SystemExit) as cm:
            main([])

        self.assertEqual(cm.exception.code, 2)
