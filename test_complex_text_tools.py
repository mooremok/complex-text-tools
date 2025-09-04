"""
Test cases for complex_text_tools package
"""

import unittest
from complex_text_tools import remove_extra_spaces, count_eff_len


class TestComplexTextTools(unittest.TestCase):
    
    def test_remove_extra_spaces(self):
        # Test mixed Chinese and English text
        text = "这 是  中文 测试  文本 ，  mixed  English  text  here ， 还 有   symbols :  ;  !  "
        expected = "这是中文测试文本，mixed English text here，还有 symbols:;!"
        result = remove_extra_spaces(text)
        self.assertEqual(result, expected)
        
    def test_count_eff_len(self):
        # Test text length counting
        text = "这是一段 mixed text 包含 123.45 数字"
        result = count_eff_len(text)
        # Should return an integer count
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()