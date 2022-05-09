import unittest

class TestDynamicClass(unittest.TestCase):
    def test_DynamicClass_HowItWorks_GetAttribut(self):
        from PyGameSudoku.DynamicClass import DynamicClass
        config = DynamicClass({ "title":"pySudoku", "shape": { "width":640, "height":480 } })
        self.assertEquals("pySudoku", config.title)
        self.assertEquals(640, config.shape.width)
        self.assertEquals(480, config.shape.height)

    def test_DynamicClass_HowItWorks_GetDictionary(self):
        from PyGameSudoku.DynamicClass import DynamicClass
        config = DynamicClass({ "shape": { "width":640, "height":480 } })
        self.assertEquals({ "width":640, "height":480 }, config.shape.__dict__)

    def test_DynamicClass_MissingAttribute_AttributeError(self):
        from PyGameSudoku.DynamicClass import DynamicClass
        config = DynamicClass()
        with self.assertRaises(AttributeError):
            title = config.title
