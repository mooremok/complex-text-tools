"""
Test cases for complex_text_tools package
"""

import unittest
from complex_text_tools import remove_extra_spaces, count_eff_len


class TestComplexTextTools(unittest.TestCase):
    
    def test_remove_extra_spaces(self):
        # Test mixed Chinese and English text
        text = "这 是  中文 测试  文本 ，  mixed  English  text  here ， 还 有   symbols :  ;  !  "
        expected = "这是中文测试文本，mixed English text here，还有symbols:;!  "
        result = remove_extra_spaces(text)
        self.assertEqual(result, expected)
        
    def test_count_eff_len(self):
        # Test text length counting
        text = "这是一段 mixed text 包含 123.45 数字"
        result = count_eff_len(text)
        # Should return an integer count
        self.assertIsInstance(result, int)
        
        # Test underscore words counting - this was the original issue
        text2 = "变量_total_words和total_words应各计为1字"
        result2 = count_eff_len(text2)
        # 变量(2) _total_words(1) 和(1) total_words(1) 应(1) 各(1) 计(1) 为(1) 1(1) 字(1) = 10
        # 中文字符: 变量和应各计为字 = 8个
        # 英文单词: _total_words, total_words = 2个
        # 总计: 8 + 2 = 10个
        self.assertEqual(result2, 10)
        
        # Test year handling - this was also an issue
        text3 = "中国是强大的，所以就在2010年"
        result3 = count_eff_len(text3)
        # 中文字符: 中国是强大的所以就在年 = 11个
        # 标点符号: ， = 1个
        # 年份数字: 2010 = 1个
        # 总计: 11 + 1 + 1 = 13个
        self.assertEqual(result3, 13)


if __name__ == '__main__':
    unittest.main()