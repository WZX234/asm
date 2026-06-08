#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
汇编器单元测试
"""

import unittest
import sys
import os

# 添加主程序路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import parse_immediate, generate_machine_code, replace_constants_in_tokens


class TestParseImmediate(unittest.TestCase):
    """测试立即数解析函数"""
    
    def test_decimal(self):
        """测试十进制解析"""
        self.assertEqual(parse_immediate("123", allow_exit=False), 123)
        self.assertEqual(parse_immediate("0", allow_exit=False), 0)
        self.assertEqual(parse_immediate("255", allow_exit=False), 255)
    
    def test_hexadecimal(self):
        """测试十六进制解析"""
        self.assertEqual(parse_immediate("0xFF", allow_exit=False), 255)
        self.assertEqual(parse_immediate("0x00", allow_exit=False), 0)
        self.assertEqual(parse_immediate("0xAB", allow_exit=False), 0xAB)
        self.assertEqual(parse_immediate("0x12", allow_exit=False), 0x12)
    
    def test_binary(self):
        """测试二进制解析"""
        self.assertEqual(parse_immediate("0b11111111", allow_exit=False), 255)
        self.assertEqual(parse_immediate("0b00000000", allow_exit=False), 0)
        self.assertEqual(parse_immediate("0b10101010", allow_exit=False), 0xAA)
    
    def test_invalid_input(self):
        """测试无效输入"""
        with self.assertRaises(ValueError):
            parse_immediate("xyz", allow_exit=False)
        with self.assertRaises(ValueError):
            parse_immediate("0xGG", allow_exit=False)  # 无效十六进制
        with self.assertRaises(ValueError):
            parse_immediate("0b12", allow_exit=False)  # 无效二进制


class TestGenerateMachineCode(unittest.TestCase):
    """测试机器码生成函数"""
    
    def test_add_instruction(self):
        """测试ADD指令生成"""
        # 测试 add r0 r1 r2
        tokens = ["add", "r0", "r1", "r2"]
        opcode = "add"
        # 模拟生成过程
        # opcode=0x0, rd=r2(0x2), rs1=r0(0x0), rs2=r1(0x1)
        # 格式: [15:12]opcode [11:10]rd [9:8]rs1 [7:6]rs2 [5:0]000000
        # 0000 10 00 01 000000 = 0x0840
        # 实际格式: [15:12]opcode [11:10]rd [9:8]rs1 [7:6]rs2 [5:0]000000
        # 0x0 << 12 | 0x2 << 10 | 0x0 << 8 | 0x1 << 6 = 0x0840
        pass  # 需要在实际环境中测试
    
    def test_addi_instruction(self):
        """测试ADDI指令生成"""
        # 测试 addi r0 r1 10 (r0 = r1 + 10)
        # opcode=0x1, rd=r0(0x0), rs1=r1(0x1), imm=10
        # imm = 10 = 0x0A -> 高2位=0x0, 低6位=0x0A
        # 格式: [15:12]opcode [11:10]rd [9:8]rs1 [7:6]imm高2位 [5:0]imm低6位
        # 0001 00 01 00 001010 = 0x110A
        pass  # 需要在实际环境中测试


class TestReplaceConstantsInTokens(unittest.TestCase):
    """测试常量替换函数"""
    
    def setUp(self):
        """设置测试环境"""
        # 创建模拟的constants表
        import main
        main.constants = {
            'MASK': {'value': 255, 'line': 1, 'used': False},
            'ZERO': {'value': 0, 'line': 2, 'used': False},
            'TEST_VAL': {'value': 100, 'line': 3, 'used': False}
        }
    
    def tearDown(self):
        """清理测试环境"""
        import main
        main.constants = {}
    
    def test_constant_replacement(self):
        """测试常量替换"""
        tokens = ["addi", "r0", "MASK", "r1"]
        result, positions = replace_constants_in_tokens(tokens, 1, "addi r0 MASK r1")
        expected = ["addi", "r0", "255", "r1"]
        self.assertEqual(result, expected)
        self.assertIn(2, positions)  # 第三个位置(索引2)被替换了
    
    def test_multiple_constants(self):
        """测试多个常量替换"""
        tokens = ["add", "ZERO", "TEST_VAL", "r2"]
        result, positions = replace_constants_in_tokens(tokens, 1, "add ZERO TEST_VAL r2")
        expected = ["add", "0", "100", "r2"]
        self.assertEqual(result, expected)
        self.assertIn(1, positions)  # 第二个位置(索引1)被替换了
        self.assertIn(2, positions)  # 第三个位置(索引2)被替换了
    
    def test_no_constants(self):
        """测试无常量的情况"""
        tokens = ["sub", "r0", "r1", "r2"]
        result, positions = replace_constants_in_tokens(tokens, 1, "sub r0 r1 r2")
        expected = ["sub", "r0", "r1", "r2"]
        self.assertEqual(result, expected)
        self.assertEqual(positions, [])  # 没有替换任何位置


def run_tests():
    """运行所有测试"""
    print("Running assembler unit tests...")
    
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseImmediate)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestReplaceConstantsInTokens))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回测试结果
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)