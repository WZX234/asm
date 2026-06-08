import sys
import re


# ==================== 全局常量定义 ====================

# 定义全局常量
MAX_IMMEDIATE_VALUE = 255
MIN_IMMEDIATE_VALUE = 0
INSTRUCTION_BITS = 16
MAX_REGISTER_INDEX = 3
DEBUG = False


def debug_print(*args):
    if DEBUG:
        print(f"{Colors.MAGENTA}[DEBUG]{Colors.RESET}", *args)


# ==================== 颜色定义 ====================

class Colors:
    """终端颜色代码"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


def print_logo():
    B = "\033[1;38;2;12;12;12m"
    W = "\033[1;38;2;251;251;190m"
    HG = "\033[1;38;2;50;50;10m"
    LG = "\033[1;38;2;100;100;70m"
    R = "\033[0m"
    # 打印ASCII logo
    print(B + "#"*100)
    print(B + "#"*100)
    print(B + "#"*5 + W + "nflfllllllll" + B + "#"*4 + LG + "e" + W + "flllfi" +  B + "#"*6 + HG + "r" + W + "ffffflffff" + LG + "t" + B + "#" + W + "f"*5 + B + "#"*7 + W + "lflff" + LG + "m" + B + "#" + LG + "e" + W + "ffffl" + HG + "r" + B + "#"*4 + W + "lllff" + B + "#"*2 + W + "nffffflffflff" + LG + "b" + B + "#"*2)
    print(B + "#"*3 + LG + "r" + W + "lllllllllllllf" + LG + "l" + B + "#"*2 + LG + "e" + W + "flllli" + B + "#"*5 + HG + "#" + W + "ffffffffffl" + LG + "a" + B + "#" + W + "f"*5 + B + "#"*7 + W + "lffff" + LG + "m" + B + "#" + LG + "e" + W + "fflffl" + HG + "r" + B + "#"*3 + W + "fffff" + B + "#" + W + "nlfflfflffffff" + HG + "e" + B + "#"*2)
    print(B + "#"*3 + W + "l"*16 + B + "#"*2 + LG + "e" + W + "flllli" + B + "#"*5 + W + "iffffffflff" + LG + "s" + B + "#"*2 + W + "fffff" + B + "#"*7 + W + "lffff" + LG + "m" + B + "#" + LG + "e" + W + "f"*7 + B + "#"*3 + W + "f"*5 + B + "#" + W + "iffffffffffffa" + B + "#"*3)
    print(B + "#"*3 + HG + "@#@@@@#" + LG + "l" + W + "illllllf" + B + "#"*2 + LG + "e" + W + "flllli" + B + "#"*19 + W + "f"*5 + B + "#"*7 + W + "lfflf" + LG + "m" + B + "#" + LG + "m" + W + "f"*8 + B + "#"*2 + W + "f"*5 + B + "#"*5 + HG + "r" + W + "fflfl" + B + "#"*7)
    print(B + "#"*12 + W + "l"*7 + B + "#"*2 + LG + "e" + W + "llllli" + B + "#"*7 + W + "tlllllllll" + B + "#"*2 + W + "f"*5 + B + "#"*7 + W + "lffff" + LG + "m" + B + "#" + LG + "e" + W + "ffffffffl" + B + "#" + W + "f"*5 + B + "#"*5 + HG + "r" + W + "f"*5 + B + "#"*7)
    print(B + "#"*3 + LG + "e" + W + "flllf" + LG + "n" + B + "#"*2 + W + "l"*7 + B + "#"*2 + LG + "e" + W + "llllln" + B + "#"*5 + HG + "#" + W + "fflffffffff" + B + "#"*2 + W + "ffffl" + B + "#"*7 + W + "lffff" + LG + "m" + B + "#" + LG + "s" + W + "fffflfffffffffl" + B + "#"*5 + HG + "r" + W + "ffffl" + B + "#"*7)
    print(B + "#"*3 + W + "llllll" + LG + "n" + B + "#"*2 + W + "llllllf" + B + "#"*2 + LG + "e" + W + "flffl" + B + "#"*6 + W + "ifffffflflf" + LG + "a" + B + "#"*2 + W + "f"*5 + B + "#"*7 + W + "lllff" + LG + "m" + B + "#" + LG + "s" + W + "ffff" + LG + "e" + W + "tffflfffff" + B + "#"*5 + HG + "@" + W + "ffflf" + B + "#"*7)
    print(B + "#"*3 + W + "flllll" + LG + "n" + B + "#"*2 + W + "flllllf" + B + "#"*14 + W + "ilffft" + LG + "l"*3 + HG + "e" + B + "#"*4 + W + "fflff" + B + "#"*7 + W + "lffff" + LG + "m" + B + "#" + LG + "s" + W + "f"*4 + LG + "e" + B + "#" + W + "lffffflff" + B + "#"*5 + HG + "r" + W + "f"*5 + B + "#"*7)
    print(B + "#"*3 + W + "fllllf" + LG + "n" + B + "#"*2 + W + "llllllllflllflf" + LG + "n" + B + "#"*5 + W + "iffff" + LG + "a" + B + "#"*8 + W + "ffffllfllll" + HG + "@" + W + "lllff" + LG + "m" + B + "#" + LG + "s" + W + "ffff" + LG + "e" + B + "#"*2 + W + "lflfffff" + B + "#"*5 + HG + "r" + W + "ffflf" + B + "#"*7)
    print(B + "#"*3 + W + "fllllf" + LG + "n" + B + "#"*2 + W + "lllllllllllllll" + LG + "n" + B + "#"*5 + W + "ifffl" + LG + "a" + B + "#"*8 + W + "ffffflffffl" + B + "#" + W + "lffff" + LG + "m" + B + "#" + LG + "s" + W + "fflf" + LG + "e" + B + "#"*3 + W + "f"*7 + B + "#"*5 + HG + "r" + W + "f"*5 + B + "#"*7)
    print(B + "#"*3 + W + "fllllf" + LG + "n" + B + "#"*3 + W + "fllllllllllllf" + B + "#"*6 + W + "iffff" + LG + "a" + B + "#"*8 + W + "fffflfffff" + LG + "b" + B + "#" + W + "LFLFF" + LG + "m" + B + "#" + LG + "s" + W + "f"*4 + LG + "e" + B + "#"*4 + W + "lfffff" + B + "#"*5 + HG + "r" + W + "fffl" + LG + "s" + B + "#"*7)
    print(B + "#"*3 + W + "ffflff" + LG + "n" + B + "#"*4 + HG + "l" + W + "ffflffllff" + HG + "m" + B + "#"*7 + HG + "llll" + B + "#"*10 + HG + "lllllllll" + B + "#"*3 + HG + "lllllr" + B + "#" + HG + "ellllr" + B + "#"*5 + HG + "ellll" + B + "#"*5 + HG + "@lll" + B + "#"*9)
    print(B + "#"*100 + R)


# ==================== 辅助函数定义 ====================

def print_error(original_line, error_pos, error_len, message, hint=None, line_number=None, error_type="error", filename=None):
    """统一的错误提示格式(类似GCC/Clang风格)
    
    Args:
        original_line: 原始代码行
        error_pos: 错误位置的起始索引(从0开始)
        error_len: 错误部分的长度
        message: 错误消息
        hint: 可选的修复建议
        line_number: 行号（可选，用于显示错误位置）
        error_type: 错误类型(error, warning, note等)
        filename: 文件名（可选，用于显示错误文件）
    """
    line_clean = original_line.rstrip('\n')
    
    # 选择要显示的文件名：优先使用传入的 filename，其次回退到解析到的 input_filename，否则显示 <stdin>
    if filename is not None:
        file_display = filename
    else:
        if 'input_filename' in globals() and input_filename is not None:
            file_display = input_filename
        else:
            file_display = "<stdin>"

    # 对于立即数/偏移类错误，尝试只标记非法字符子集以提高定位精度
    def _refine_immediate_mark(orig, pos, length, msg):
        try:
            if pos is None:
                return pos, length
            seg = orig[pos: pos + (length or 1)]
            seg_stripped = seg.strip()
            if not seg_stripped:
                return pos, length

            # 二进制格式
            if seg_stripped.lower().startswith('0b'):
                body = seg_stripped[2:]
                for i, ch in enumerate(body):
                    if ch not in '01':
                        abs_idx = orig.find(body[i], pos)
                        return abs_idx, 1
                return pos, length

            # 十六进制格式
            if seg_stripped.lower().startswith('0x'):
                body = seg_stripped[2:]
                import string
                hexset = set(string.hexdigits)
                for i, ch in enumerate(body):
                    if ch not in hexset:
                        abs_idx = orig.find(body[i], pos)
                        return abs_idx, 1
                return pos, length

            # 十进制格式，标记非数字字符
            for i, ch in enumerate(seg_stripped):
                if not ch.isdigit() and ch != '-':
                    abs_idx = orig.find(ch, pos)
                    return abs_idx, 1
            return pos, length
        except Exception:
            return pos, length

    refined_pos, refined_len = _refine_immediate_mark(original_line, error_pos, error_len, message)

    # 如果标记看起来像标识符（寄存器名、标签或常量名），将 caret 扩展以覆盖整个连续的单词字符序列（字母/数字/_）
    def _expand_to_word(orig, pos, length):
        try:
            if pos is None:
                return pos, length
            n = len(orig)
            # 防守：越界检查
            if pos < 0 or pos >= n:
                return pos, length

            # 向左找到单词开始
            start = pos
            while start > 0 and (orig[start - 1].isalnum() or orig[start - 1] == '_'):
                start -= 1

            # 计算初始 end（若 length 给出，优先从 pos+length 推断）
            if length and length > 0:
                end = pos + length
            else:
                end = pos + 1
            if end > n:
                end = n

            # 向右扩展到单词结尾
            while end < n and (orig[end].isalnum() or orig[end] == '_'):
                end += 1

            # 如果扩展出的区域至少包含一个字母/数字，则返回新范围
            if end - start > 0 and any(ch.isalnum() or ch == '_' for ch in orig[start:end]):
                return start, end - start
            return pos, length
        except Exception:
            return pos, length

    refined_pos, refined_len = _expand_to_word(original_line, refined_pos, refined_len)

    # 尝试加载上下文文件内容（优先使用 filename 参数，否则使用全局 input_filename）
    ctx_lines = None
    file_path_to_open = filename if filename is not None else (input_filename if 'input_filename' in globals() else None)
    if line_number is not None and file_path_to_open is not None:
        try:
            try:
                with open(file_path_to_open, 'r', encoding='utf-8') as fh:
                    all_lines = fh.readlines()
            except UnicodeDecodeError:
                with open(file_path_to_open, 'r', encoding='gbk') as fh:
                    all_lines = fh.readlines()

            # 获取前一行、当前行、下一行（如果存在）
            ctx_lines = []
            idx = max(1, line_number - 1)
            for ln in range(idx, min(len(all_lines), line_number + 1) + 1):
                ctx_lines.append((ln, all_lines[ln - 1].rstrip('\n')))
        except Exception:
            ctx_lines = None

    # 若有上下文则调用详细错误显示， 否则使用简洁模式
    if ctx_lines:
        print_detailed_error(original_line, refined_pos, refined_len, message, hint, line_number, ctx_lines, file_path_to_open)
    else:
        # 简洁单行输出
        print(f"{Colors.CYAN}Traceback (most recent call last):{Colors.RESET}")
        print(f"{Colors.CYAN}  File \"{file_display}\", line {line_number if line_number is not None else '?'} , in <module>{Colors.RESET}")
        print(f"{Colors.WHITE}    {line_clean}{Colors.RESET}")
        caret_spaces = refined_pos if refined_pos is not None else 0
        caret_len = refined_len if refined_len and refined_len > 0 else 1
        caret = ' ' * (4 + caret_spaces) + f"{Colors.RED}{'^' * caret_len}{Colors.RESET}"
        print(caret)
        exc_name = 'SyntaxError' if error_type == 'error' else error_type.capitalize()
        print(f"{Colors.RED}{exc_name}:{Colors.RESET} {message}")
        if hint:
            print(f"{Colors.CYAN}Note:{Colors.RESET} {hint}")
        print()


def print_detailed_error(original_line, error_pos, error_len, message, hint=None, line_number=None, context_lines=None, filename=None):
    """详细的错误提示(类似GCC详细错误输出)
    
    Args:
        original_line: 原始代码行
        error_pos: 错误位置的起始索引
        error_len: 错误部分的长度
        message: 错误消息
        hint: 修复建议
        line_number: 行号
        context_lines: 上下文行列表 [(line_num, line_content)]
        filename: 文件名（可选，用于显示错误文件）
    """
    line_clean = original_line.rstrip('\n')
    
    # 选择要显示的文件名：优先使用传入的 filename，其次回退到解析到的 input_filename，否则显示 <stdin>
    if filename is not None:
        file_display = filename
    else:
        if 'input_filename' in globals() and input_filename is not None:
            file_display = input_filename
        else:
            file_display = "<stdin>"

    # 将错误位置扩展为覆盖整个标识符（寄存器/标签/常量）以得到更直观的 caret
    def _expand_to_word(orig, pos, length):
        try:
            if pos is None:
                return pos, length
            n = len(orig)
            if pos < 0 or pos >= n:
                return pos, length
            start = pos
            while start > 0 and (orig[start - 1].isalnum() or orig[start - 1] == '_'):
                start -= 1
            if length and length > 0:
                end = pos + length
            else:
                end = pos + 1
            if end > n:
                end = n
            while end < n and (orig[end].isalnum() or orig[end] == '_'):
                end += 1
            if end - start > 0 and any(ch.isalnum() or ch == '_' for ch in orig[start:end]):
                return start, end - start
            return pos, length
        except Exception:
            return pos, length

    error_pos, error_len = _expand_to_word(original_line, error_pos, error_len)

    # Python 风格的详细错误输出（包含上下文行），使用颜色：文件/traceback 青色，源码白色，指示红色，异常名红色
    print(f"{Colors.CYAN}Traceback (most recent call last):{Colors.RESET}")
    print(f"{Colors.CYAN}  File \"{file_display}\", line {line_number}, in <module>{Colors.RESET}")

    # 显示上下文行（包含前后各一行），高亮错误所在行并在行内标注错误位置
    if context_lines:
        for ctx_line_num, ctx_line in context_lines:
            prefix = '    '
            if ctx_line_num == line_number:
                print(f"{Colors.WHITE}{prefix}{ctx_line.rstrip()}{Colors.RESET}")
                caret_spaces = error_pos if error_pos is not None else 0
                caret_len = error_len if error_len and error_len > 0 else 1
                caret = ' ' * (len(prefix) + caret_spaces) + f"{Colors.RED}{'^' * caret_len}{Colors.RESET}"
                print(caret)
            else:
                print(f"{Colors.WHITE}{prefix}{ctx_line.rstrip()}{Colors.RESET}")
    else:
        print(f"{Colors.WHITE}    {line_clean}{Colors.RESET}")
        caret_spaces = error_pos if error_pos is not None else 0
        caret_len = error_len if error_len and error_len > 0 else 1
        caret = ' ' * (4 + caret_spaces) + f"{Colors.RED}{'^' * caret_len}{Colors.RESET}"
        print(caret)

    # 错误类型映射并高亮
    exc_name = 'SyntaxError'
    print(f"{Colors.RED}{exc_name}:{Colors.RESET} {message}")
    if hint:
        print(f"{Colors.CYAN}Note:{Colors.RESET} {hint}")
    print()


class AssemblerError:
    """错误类别定义"""
    SYNTAX_ERROR = "SYNTAX_ERROR"
    SEMANTIC_ERROR = "SEMANTIC_ERROR"
    TYPE_ERROR = "TYPE_ERROR"
    NAME_ERROR = "NAME_ERROR"
    VALUE_ERROR = "VALUE_ERROR"
    
    @staticmethod
    def get_error_message(error_type, **kwargs):
        """返回更精细化的错误说明(+修复建议)。

        返回字符串形式，包含错误描述和具体修复建议，便于直接展示。
        """
        # 按 error_type 和 subtype 返回具体消息与修复建议
        msg = "unknown error"
        hint = None

        if error_type == AssemblerError.SYNTAX_ERROR:
            subtype = kwargs.get('subtype', '')
            if subtype == 'const_syntax':
                msg = "expected syntax: const NAME VALUE"
                hint = "use: const IDENTIFIER NUMBER (examples: const MASK 0xFF, const LEN 10)"
            elif subtype == 'operand_count':
                msg = f"'{kwargs.get('opcode', '')}' expects {kwargs.get('expected', '')} operands, got {kwargs.get('actual', '')}"
                hint = "check operand count and order: opcode RS1 RS2 RD (destination last)"
            elif subtype == 'invalid_format':
                msg = "invalid instruction format"
                hint = "ensure correct operand ordering and types (see assembler docs)"

        elif error_type == AssemblerError.NAME_ERROR:
            subtype = kwargs.get('subtype', '')
            if subtype == 'undefined_const':
                name = kwargs.get('name', '')
                msg = f"use of undeclared constant '{name}'"
                hint = "declare it before use: const NAME VALUE (example: const MASK 0xFF)"
            elif subtype == 'duplicate_const':
                name = kwargs.get('name', '')
                msg = f"constant '{name}' redefined"
                hint = "remove or rename duplicate definitions; constants must be unique"
            elif subtype == 'undefined_label':
                name = kwargs.get('name', '')
                msg = f"use of undeclared label '{name}'"
                hint = "ensure the label is defined (e.g., L1:) or check for typos"
            elif subtype == 'invalid_register':
                name = kwargs.get('name', '')
                msg = f"invalid register name '{name}'"
                hint = "valid registers: r0, r1, r2, r3 — check for typos or out-of-range registers"

        elif error_type == AssemblerError.VALUE_ERROR:
            subtype = kwargs.get('subtype', '')
            if subtype == 'immediate_out_of_range':
                value = kwargs.get('value', '')
                mn = kwargs.get('min', 0)
                mx = kwargs.get('max', 255)
                msg = f"immediate value {value} out of range [{mn}, {mx}]"
                hint = f"use values in range {mn}..{mx}, examples: 0, 0xFF, 0b11111111; invalid examples: {mx+1}, -1"
            elif subtype == 'invalid_immediate':
                val = kwargs.get('value', '')
                msg = f"invalid immediate value '{val}'"
                hint = "valid formats: decimal (123), hex (0xFF), binary (0b10101010). Ensure binary uses only 0/1 and hex uses 0-9/A-F"

        elif error_type == AssemblerError.TYPE_ERROR:
            subtype = kwargs.get('subtype', '')
            if subtype == 'register_expected':
                msg = "expected register, got constant"
                hint = "use a register name (r0..r3) in this operand position"
            elif subtype == 'immediate_expected':
                msg = "expected immediate, got register"
                hint = "provide an immediate value (e.g., 5 or 0x05) in this position"

        elif error_type == AssemblerError.SEMANTIC_ERROR:
            subtype = kwargs.get('subtype', '')
            if subtype == 'const_reassignment':
                msg = "attempt to assign to constant"
                hint = "constants are immutable; use a different label or variable"
            elif subtype == 'reserved_keyword':
                name = kwargs.get('name', '')
                msg = f"'{name}' is a reserved keyword"
                hint = "rename your identifier to avoid reserved keywords"

        # 如果有 hint，则把它合并进返回字符串，保持兼容性
        if hint:
            return f"{msg}  Note: {hint}"
        return msg


# ==================== 函数定义 ====================

def replace_constants_in_tokens(tokens, line_number, original_line):
    """将tokens中的常量名替换为对应的值
    
    Args:
        tokens: 指令token列表
        line_number: 行号
        original_line: 原始代码行
    
    Returns:
        替换后的tokens列表和是否发生替换的标记
    """
    new_tokens = [tokens[0]]  # 保留操作码
    replaced_positions = []  # 记录哪些位置被替换了
    
    for i in range(1, len(tokens)):
        token = tokens[i]
        # 检查是否是常量名（不是数字，不是寄存器）
        is_const = False
        try:
            # 尝试解析为数字
            if token.startswith('0x') or token.startswith('0X'):
                int(token, 16)
            elif token.startswith('0b') or token.startswith('0B'):
                int(token, 2)
            else:
                int(token)
            # 是数字，不需要替换
            new_tokens.append(token)
            continue
        except ValueError:
            pass
        
        # 不是数字，检查是否是寄存器（大小写不敏感）
        if token.lower() in REGISTER_NAMES:
            new_tokens.append(token.lower())
            continue
        
        # 不是寄存器，可能是常量名
        const_name = token.lower()
        if const_name in constants:
            # 找到常量，替换为值
            constants[const_name]['used'] = True  # 标记为已使用
            const_value = constants[const_name]['value']
            new_tokens.append(str(const_value))
            replaced_positions.append(i)  # 记录这个位置被替换了
            is_const = True
        else:
            # 如果是标签名（在标签表中），也保留原样（标签在分支解析时处理）
            if token.lower() in labels:
                # 统一使用小写形式与标签表匹配一致
                new_tokens.append(token.lower())
            else:
                # 不是已知常量或标签，统一返回小写以减少后续匹配差异
                new_tokens.append(token.lower())
    
    return new_tokens, replaced_positions


def parse_immediate(imm_str, line_number=None, original_line=None, allow_exit=True, error_pos=None):
    """解析立即数，支持十进制、十六进制、二进制，返回整数值
    
    Args:
        imm_str: 立即数字符串
        line_number: 行号（用于错误提示）
        original_line: 原始代码行（用于错误提示）
        allow_exit: 是否允许直接退出程序
        error_pos: 错误位置索引（如果为None，则不显示箭头）
    """
    imm_str = imm_str.strip()
    # 新增：空值校验
    if not imm_str:
        if allow_exit and line_number is not None and original_line is not None:
            print_error(original_line, error_pos if error_pos is not None else 0, 1,
                       "empty immediate value",
                       "provide a valid number (decimal, hex, binary)",
                       line_number, "error", input_filename)
            sys.exit(1)
        raise ValueError("empty immediate value")
    
    try:
        if imm_str.startswith('0x') or imm_str.startswith('0X'):
            return int(imm_str, 16)
        elif imm_str.startswith('0b') or imm_str.startswith('0B'):
            return int(imm_str, 2)
        else:
            return int(imm_str)
    except ValueError:
        if allow_exit and line_number is not None and original_line is not None:
            print_error(original_line, error_pos if error_pos is not None else 0, len(imm_str), 
                       f"invalid immediate value '{imm_str}'",
                       f"valid immediate formats: 123, 0xFF, 0b10101010",
                       line_number, "error", input_filename)
            sys.exit(1)
        raise


def get_token_pos_len(original_line, token_index=None, token_text=None):
    """在原始行中定位按顺序的 token，返回 (start, length).

    - 如果提供 token_index（0 基），则返回该序号 token 的位置（跳过注释部分）。
    - 否则若提供 token_text，则尝试按 token 文本匹配（大小写不敏感）并返回第一个匹配项。
    - 回退策略：若匹配失败则使用简单的 lower().find() 作为最后手段，或返回 (0, len(token_text) or 1)。
    """
    line = original_line.rstrip('\n')
    # 去掉注释部分以避免匹配注释内容
    ci = line.find(';')
    if ci != -1:
        line = line[:ci]

    spans = [(m.start(), m.end() - m.start(), m.group(0)) for m in re.finditer(r'\S+', line)]

    if token_index is not None:
        if 0 <= token_index < len(spans):
            return spans[token_index][0], spans[token_index][1]

    if token_text is not None:
        t_low = token_text.lower()
        for start, length, txt in spans:
            if txt.lower() == t_low:
                return start, length

    # 最后的回退：在整行中查找子串
    if token_text:
        pos = line.lower().find(token_text.lower())
        if pos != -1:
            return pos, len(token_text)
    return 0, (len(token_text) if token_text else 1)

def generate_machine_code(tokens, opcode, line_number, original_line):
    """生成16位机器码"""
    op_code = opcodes[opcode]
    
    # nop 指令特殊处理
    if opcode == "nop":
        # 使用 opcode 表中的值编码为 [opcode<<12]
        return (op_code << 12)
    
    # 运算指令和 load 指令
    arithmetic_load_opcodes = {"add", "addi", "sub", "subi", "and", "andi", "or", "ori", "load"}
    
    if opcode in arithmetic_load_opcodes:
        # 汇编格式：opcode rs1 rs2/imm rd
        # tokens = [opcode, rs1, rs2/imm, rd]
        if len(tokens) != 4:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"'{opcode}' expects 3 operands, got {len(tokens)-1}",
                       f"correct syntax: {opcode} REG REG REG (example: {opcode} r0 r1 r2)",
                       line_number, "error")
            sys.exit(1)
            
        # 验证寄存器名，避免直接 KeyError 崩溃
        line_lower_for_find = original_line.lower()
        # rs1
        if tokens[1].lower() not in registers:
            pos, plen = get_token_pos_len(original_line, 1, tokens[1])
            print_error(original_line, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                       f"invalid register name '{tokens[1]}'",
                       "valid registers: r0, r1, r2, r3; check for typos",
                       line_number, "error", input_filename)
            sys.exit(1)
        rs1 = registers[tokens[1].lower()]
        # rd
        if tokens[3].lower() not in registers:
            pos, plen = get_token_pos_len(original_line, 3, tokens[3])
            print_error(original_line, pos if pos is not None else 0, plen if plen>0 else len(tokens[3]),
                       f"invalid register name '{tokens[3]}'",
                       "valid registers: r0, r1, r2, r3; destination register must be last",
                       line_number, "error", input_filename)
            sys.exit(1)
        rd = registers[tokens[3].lower()]
        
        # 判断第三个操作数是寄存器还是立即数
        is_immediate = False
        try:
            imm_value = parse_immediate(tokens[2], allow_exit=False)
            is_immediate = True
        except ValueError:
            # 不是数字，应为寄存器；先验证名称
            if tokens[2].lower() not in registers:
                pos, plen = get_token_pos_len(original_line, 2, tokens[2])
                print_error(original_line, pos if pos is not None else 0, plen if plen>0 else len(tokens[2]),
                           f"invalid register name '{tokens[2]}'",
                           "valid registers: r0, r1, r2, r3; check for typos",
                           line_number, "error", input_filename)
                sys.exit(1)
            rs2 = registers[tokens[2].lower()]
            is_immediate = False
        
        if is_immediate:
            # 立即数版本：[opcode][rd][rs1][imm高2位][imm低6位]
            # 验证范围：0-255（8位无符号）
            if imm_value < 0 or imm_value > 255:
                # 计算立即数的位置
                imm_pos, imm_len = get_token_pos_len(original_line, 2, tokens[2])
                print_error(original_line, imm_pos, imm_len if imm_len>0 else len(tokens[2]), 
                           "immediate value out of range [0, 255]",
                           "valid range: 0 to 255 (or 0x00 to 0xFF, 0b00000000 to 0b11111111)",
                           line_number, "error", input_filename)
                sys.exit(1)

            # 提取立即数的高2位和低6位
            imm_high = (imm_value >> 6) & 0x03
            imm_low = imm_value & 0x3F
            
            # 构建指令：[15:12]opcode [11:10]rd [9:8]rs1 [7:6]imm高2位 [5:0]imm低6位
            instruction = (op_code << 12) | (rd << 10) | (rs1 << 8) | (imm_high << 6) | imm_low
        else:
            # 寄存器版本：[opcode][rd][rs1][rs2][000000]
            instruction = (op_code << 12) | (rd << 10) | (rs1 << 8) | (rs2 << 6)
        
    else:
        # 分支和 store 指令
        # 汇编格式：opcode rs1 rs2 offset
        # tokens = [opcode, rs1, rs2, offset]
        branch_store_opcodes = {"beqa", "beqs", "blta", "blts", "store"}
        
        if opcode not in branch_store_opcodes:
            print_error(original_line, 0, len(tokens[0]), 
                       f"unknown opcode '{opcode}'",
                       "valid opcodes: add, addi, sub, subi, and, andi, or, ori, load, store, beqa, beqs, blta, blts, nop",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        if len(tokens) != 4:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"'{opcode}' expects 3 operands, got {len(tokens)-1}",
                       f"correct syntax: {opcode} REG REG IMM (example: {opcode} r0 r1 10)",
                       line_number, "error")
            sys.exit(1)
        
        # 验证分支/store 的寄存器操作数
        line_lower_for_find = original_line.lower()
        if tokens[1].lower() not in registers:
            pos, plen = get_token_pos_len(original_line, 1, tokens[1])
            print_error(original_line, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                       f"invalid register name '{tokens[1]}'",
                       "valid registers: r0, r1, r2, r3; check for typos",
                       line_number, "error", input_filename)
            sys.exit(1)
        rs1 = registers[tokens[1].lower()]
        if tokens[2].lower() not in registers:
            pos, plen = get_token_pos_len(original_line, 2, tokens[2])
            print_error(original_line, pos if pos is not None else 0, plen if plen>0 else len(tokens[2]),
                       f"invalid register name '{tokens[2]}'",
                       "valid registers: r0, r1, r2, r3; check for typos", 
                       line_number, "error", input_filename)
            sys.exit(1)
        rs2 = registers[tokens[2].lower()]
        # 计算偏移量的位置用于错误提示
        offset_pos, offset_len = get_token_pos_len(original_line, 3, tokens[3])
        offset = parse_immediate(tokens[3], line_number, original_line, error_pos=offset_pos)

        # 分支/store指令格式：[opcode][offset高2位][rs1][rs2][offset低6位]
        # 注意：偏移量已在主循环中校验过范围（0-255），这里不再重复校验
        offset_high = (offset >> 6) & 0x03
        offset_low = offset & 0x3F
        
        instruction = (op_code << 12) | (offset_high << 10) | (rs1 << 8) | (rs2 << 6) | offset_low
    
    return instruction


# ==================== 全局变量定义 ====================

# 指令表
opcodes = {
    "add": 0x0,
    "addi": 0x1,
    "sub": 0x2,
    "subi": 0x3,
    "and": 0x4,
    "andi": 0x5,
    "or": 0x6,
    "ori": 0x7,
    "load": 0x8,
    "store": 0x9,
    "beqa": 0xA,
    "beqs": 0xB,
    "blta": 0xC,
    "blts": 0xD,
    "nop": 0xE,
}

# 寄存器表
registers = {
    "r0": 0x0,
    "r1": 0x1,
    "r2": 0x2,
    "r3": 0x3,
}

# 预处理寄存器名称为小写集合，提高查找效率
REGISTER_NAMES = {reg.lower() for reg in registers.keys()}
# 伪指令表
pseudo_map = {
    "mov":  "addi",   # mov rs rd → addi rs 0 rd
    "clr":  "sub",    # clr rd → sub rd rd rd
    "inc":  "addi",   # inc rd → addi rd 1 rd
    "dec":  "subi",   # dec rd → subi rd 1 rd
    "shl":  "add",    # shl rd → add rd rd rd
    "str":  "store",  # str rs1 rs2 offset → store rs1 rs2 offset
}

# 常量表（用于 const 声明）
constants = {}

# 标签表（用于跳转指令）
labels = {}

# 错误代码定义
ERROR_CODES = {
    'CONST_NOT_DECLARED': 'E001',  # 使用了未声明的常量
    'CONST_WRITE_ATTEMPT': 'E002',  # 尝试写入常量
    'CONST_DUPLICATE': 'E003',      # 常量重复定义
    'CONST_OUT_OF_RANGE': 'E004',   # 常量值超出范围
    'NOT_NO_CONST': 'E005',         # NOT指令但未声明NOT_MASK常量
}

# 继续添加更精细的错误码（E006 起）
ERROR_CODES.update({
    'INVALID_REGISTER_NAME': 'E006',
    'IMMEDIATE_FORMAT_ERROR': 'E007',
    'LABEL_OFFSET_OUT_OF_RANGE': 'E008',
    'UNKNOWN_OPCODE': 'E009',
    'DUPLICATE_LABEL': 'E010',
    'INVALID_IMMEDIATE_RANGE': 'E011',
    'INVALID_CONST_SYNTAX': 'E012',
    'INVALID_FILE_ENCODING': 'E013',
})


def resolve_label_offset(label_name, current_address, original_line, line_number):
    """解析标签偏移量"""
    if label_name not in labels:
        label_pos, label_len = get_token_pos_len(original_line, None, label_name)
        print_error(original_line, label_pos, label_len if label_len>0 else len(label_name), 
                   f"use of undeclared label '{label_name}'",
                   f"label '{label_name}' is not defined in the code",
                   line_number, "error", input_filename)
        sys.exit(1)
    
    # 计算相对于当前位置的偏移量
    target_address = labels[label_name]

    # 计算无符号偏移及方向：硬件不支持有符号偏移
    # 根据新硬件语义，偏移基于当前指令的原始 PC（current_address）
    # 如果目标在当前之后，使用加法变体 (a)，偏移 = target - current
    # 如果目标在当前之前，使用减法变体 (s)，偏移 = abs(target - current)
    raw = target_address - current_address
    unsigned_offset = abs(raw)
    direction = 'a' if raw >= 0 else 's'

    # 验证偏移量范围：硬件只接受 0..255（无符号）
    if unsigned_offset < 0 or unsigned_offset > 255:
        label_pos, label_len = get_token_pos_len(original_line, None, label_name)
        print_error(original_line, label_pos, label_len if label_len>0 else len(label_name), 
               f"label offset {unsigned_offset} out of range [0, 255]",
               f"label '{label_name}' is too far away, offset must fit in 8-bit unsigned field",
               line_number, "error", input_filename)
        sys.exit(1)

    # 返回 (unsigned_offset, direction) 供调用者选择 a/s 变体并编码为无符号偏移
    return unsigned_offset, direction


# ==================== 主程序逻辑 ====================

# 显示LOGO
print_logo()

# 获取参数
addr = sys.argv[1:]

# 检查是否有调试标志
for arg in sys.argv[1:]:
    if arg == "-d" or arg == "--debug":
        DEBUG = True
        print(f"{Colors.CYAN}Debug mode enabled{Colors.RESET}")
        break

# 如果用户请求版本或帮助，优先处理并退出（无需文件参数）
if any(a in ("-v", "--version") for a in addr):
    print(f"{Colors.YELLOW}{Colors.BOLD}ASSEMBLER Version 2.0.0.1{Colors.RESET}")
    sys.exit()

if any(a in ("-h", "--help") for a in addr):
    print(f"{Colors.CYAN}Usage: asm [options] <assembly_file>{Colors.RESET}")
    print(f"{Colors.CYAN}Options:{Colors.RESET}")
    print(f"  {Colors.YELLOW}-v, --version{Colors.RESET}   Show assembler version information")
    print(f"  {Colors.YELLOW}-h, --help{Colors.RESET}      Show this help message")
    print(f"  {Colors.YELLOW}-o, --output{Colors.RESET}    Specify output file name (default: <input>_machine.txt)")
    sys.exit()

# 确定输入文件：第一个不以 '-' 开头的参数被视为输入文件
input_filename = None
for a in addr:
    if not a.startswith('-'):
        input_filename = a
        break

if input_filename is None:
    print(f"{Colors.CYAN}Hello! This is a simple assembler. To use it, provide the path to the assembly file as an argument.{Colors.RESET}")
    print(f"{Colors.CYAN}Usage: python main.py [options] <assembly_file>{Colors.RESET}")
    print(f"{Colors.CYAN}Options:{Colors.RESET}")
    print(f"{Colors.CYAN}  -d, --debug    Enable debug mode{Colors.RESET}")
    print(f"{Colors.CYAN}  -o, --output   Specify output file format (binary, hex, bin){Colors.RESET}")
    sys.exit()

# 打开文件：优先使用 UTF-8，失败则退回 GBK
try:
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        # 尝试使用 GBK 解码
        try:
            with open(input_filename, 'r', encoding='gbk') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            # 无法以 UTF-8 或 GBK 解码，使用统一错误提示
            print_error('', 0, 1,
                        f"file encoding not supported: {input_filename}",
                        "please save the assembly file in UTF-8 or GBK encoding",
                        None, "error", input_filename)
            sys.exit(1)

except FileNotFoundError:
    print(f"{Colors.RED}Error: File not found{Colors.RESET}")
    sys.exit(1)
except IOError:
    print(f"{Colors.RED}Error: Error opening file{Colors.RESET}")
    sys.exit(1)
except Exception as e:
    print(f"{Colors.RED}Error: {e}{Colors.RESET}")
    sys.exit(1)

# 开始编译
print(f"{Colors.BLUE}{Colors.BOLD}Assembling...{Colors.RESET}")


# 第一遍扫描：处理标签定义
line_num_temp = 0
instruction_count = 0  # 记录已生成的指令数（即机器码地址）
def is_immediate_str(s):
    try:
        s = s.strip()
        if s.startswith('0x') or s.startswith('0X'):
            int(s, 16)
        elif s.startswith('0b') or s.startswith('0B'):
            int(s, 2)
        else:
            int(s)
        return True
    except Exception:
        return False


def preprocess_lines(raw_lines):
    """预处理并完全展开伪指令，返回展开后的指令列表。

    每个条目为字典：{'text': normalized_text, 'original': original_raw_line, 'src_line': source_line_number}
    这样可以在后续两遍中使用同一份已展开数据，保证标签偏移一致性并保留原始行号用于错误提示。
    """
    out = []
    for idx, raw in enumerate(raw_lines, start=1):
        original_raw = raw.rstrip('\n')
        line_lower = original_raw.lower().strip()
        # 如果整行为空（仅空白字符），为保持源行与展开列表的行号对齐，加入占位条目
        if not line_lower:
            out.append({'text': '', 'original': original_raw, 'src_line': idx})
            continue

        # 去除注释（在处理之前保留原始行用于错误定位）
        comment_idx = line_lower.find(';')
        if comment_idx != -1:
            line_lower = line_lower[:comment_idx].strip()

        # 行内去除注释后若变为空白，同样加入占位条目以保留行号
        if line_lower == '':
            out.append({'text': '', 'original': original_raw, 'src_line': idx})
            continue

        tokens = line_lower.split()
        if len(tokens) == 0:
            continue

        # 标签保持原样（以冒号结尾）
        if tokens[0].endswith(':'):
            out.append({'text': line_lower, 'original': original_raw, 'src_line': idx})
            continue

        opcode = tokens[0]

        # 不再支持 sub RD IMM RS (立即数在前) 形式；此类形式将在第二遍报错

        # 展开伪指令映射为真实指令（mov/clr/inc/dec/shl/str）
        if opcode in pseudo_map:
            original_opcode = opcode
            real_inst = pseudo_map[opcode]
            if original_opcode == 'mov' and len(tokens) >= 3:
                # 校验：mov 源操作数必须为寄存器，目标也必须为寄存器
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"mov: source operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                if tokens[2].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 2, tokens[2])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[2]),
                                f"mov: destination operand must be a register, got '{tokens[2]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} 0 {tokens[2]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue
            if original_opcode == 'clr' and len(tokens) >= 2:
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"clr: operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} {tokens[1]} {tokens[1]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue
            if original_opcode == 'inc' and len(tokens) >= 2:
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"inc: operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} 1 {tokens[1]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue
            if original_opcode == 'dec' and len(tokens) >= 2:
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"dec: operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} 1 {tokens[1]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue
            if original_opcode == 'shl' and len(tokens) >= 2:
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"shl: operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} {tokens[1]} {tokens[1]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue
            if original_opcode == 'str' and len(tokens) >= 4:
                # str: tokens[1], tokens[2] 必须为寄存器，tokens[3] 可为立即数/常量/标签（不在此处严格验证）
                if tokens[1].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 1, tokens[1])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[1]),
                                f"str: first operand must be a register, got '{tokens[1]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                if tokens[2].lower() not in REGISTER_NAMES:
                    pos, plen = get_token_pos_len(original_raw, 2, tokens[2])
                    print_error(original_raw, pos if pos is not None else 0, plen if plen>0 else len(tokens[2]),
                                f"str: second operand must be a register, got '{tokens[2]}'",
                                "use registers: r0, r1, r2, r3",
                                idx, "error", input_filename)
                    sys.exit(1)
                new = f"{real_inst} {tokens[1]} {tokens[2]} {tokens[3]}"
                out.append({'text': new, 'original': original_raw, 'src_line': idx})
                continue

        # 保持原始操作数顺序（要求使用 opcode rs1 rs2 rd 风格）

        # 其他情况保持原样（小写）
        out.append({'text': line_lower, 'original': original_raw, 'src_line': idx})

    return out


expanded_instructions = preprocess_lines(lines)

for entry in expanded_instructions:
    line_lower = entry['text'].strip()

    # 结束
    if not line_lower:
        continue

    line_num_temp += 1

    # 跳过空行和注释行
    if line_lower == '' or line_lower[0] == ';':
        continue

    # 获取指令
    tokens = line_lower.split()

    # 忽略空行
    if len(tokens) == 0:
        continue

    # 检查是否是标签（以冒号结尾）
    if tokens[0].endswith(':'):
        label_name = tokens[0][:-1].lower()  # 去掉冒号
        labels[label_name] = instruction_count  # 标签地址 = 当前指令计数
        continue

    # 统计指令数（处理伪指令/扩展指令的多指令情况）
    opcode = tokens[0]
    if opcode == 'not':
        instruction_count += 3  # not 展开为三条指令，计数应一致
    elif opcode == 'sub':
        # 现在 sub 一律视作单条指令；形式 sub dst imm src 将在第二遍报错
        instruction_count += 1
    elif opcode in ['beq', 'blt']:
        instruction_count += 1  # beq/blt 生成1条指令
    else:
        instruction_count += 1  # 默认每条原始指令生成1条机器码

# 初始化第二遍扫描
line_number = 0
machine_code = []
line_to_address_map = {}  # 记录每一行对应的机器码地址
machine_code_address = 0  # 机器码地址计数器
for entry in expanded_instructions:
    line_lower = entry['text']
    original_line = entry['original']
    # 使用源文件的行号，便于错误映射
    line_number = entry['src_line']

    # 结束
    if not line_lower:
        continue

    # 跳过空行和注释行
    if line_lower == '' or line_lower[0] == ';':
        continue

    # 去除行内注释（entry['text'] 应已无注释，但保留以防）
    comment_idx = line_lower.find(';')
    if comment_idx != -1:
        line_lower = line_lower[:comment_idx].strip()

    if line_lower == '':
        continue

    # 获取指令
    tokens = line_lower.split()

    # 忽略空行
    if len(tokens) == 0:
        continue
    
    # 检查是否是标签定义
    if tokens[0].endswith(':'):
        # 这是一个标签定义，跳过处理
        continue
    
    # 操作码
    opcode = tokens[0]
    
    # 计算错误提示的起始位置（在处理常量和其他替换之前就设置）
    line_lower_for_find = original_line.lower()
    start_idx, _ = get_token_pos_len(original_line, 0, tokens[0])
    
    # 记录这一行对应的机器码地址
    line_to_address_map[line_number] = machine_code_address
    
    # 处理常量声明：const NAME VALUE
    if opcode == "const":
        if len(tokens) != 3:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"expected syntax: const NAME VALUE",
                       f"correct format: const IDENTIFIER NUMBER (example: const MASK 0xFF)",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        const_name = tokens[1].lower()
        const_value_str = tokens[2]
        
        # 解析常量值
        try:
            if const_value_str.startswith('0x') or const_value_str.startswith('0X'):
                const_value = int(const_value_str, 16)
            elif const_value_str.startswith('0b') or const_value_str.startswith('0B'):
                const_value = int(const_value_str, 2)
            else:
                const_value = int(const_value_str)
        except ValueError:
            const_pos, const_len = get_token_pos_len(original_line, 2, const_value_str)
            print_error(original_line, const_pos, const_len if const_len>0 else len(const_value_str), 
                       f"invalid constant value '{const_value_str}'",
                       "expected a decimal, hex (0x...) or binary (0b...) number",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        # 验证范围（0-255）
        if const_value < 0 or const_value > 255:
            const_pos, const_len = get_token_pos_len(original_line, 2, const_value_str)
            print_error(original_line, const_pos, const_len if const_len>0 else len(const_value_str), 
                       f"constant value {const_value} out of range [0, 255]",
                       "values must be between 0 and 255 (inclusive)",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        # 检查是否重复定义
        if const_name in constants:
            const_name_pos, const_name_len = get_token_pos_len(original_line, 1, const_name)
            print_error(original_line, const_name_pos, const_name_len if const_name_len>0 else len(const_name), 
                       f"constant '{const_name}' redefined",
                       f"previous definition was at line {constants[const_name]['line']}",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        # 存储常量
        constants[const_name] = {
            'value': const_value,
            'line': line_number,
            'used': False  # 跟踪是否被使用
        }
        
        # 常量声明不生成机器码，跳过后续处理
        continue
    
    # 特殊处理：beq/blt 分支伪指令（根据偏移正负选择加/减版本）
    if opcode == "beq" or opcode == "blt":
        if len(tokens) != 4:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"'{opcode}' requires exactly 3 operands",
                       f"Example: {opcode} r0 r1 +5",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        # 解析偏移量 - 检查是否是标签
        offset_str = tokens[3]
        offset = None
        
        # 检查是否是标签引用
        if offset_str.lower() in labels:
            # 是标签，解析为偏移量
            current_address = machine_code_address  # 当前机器码地址
            unsigned_offset, direction = resolve_label_offset(offset_str.lower(), current_address, original_line, line_number)
        else:
            # 是普通偏移量，解析为数值
            try:
                if offset_str.startswith('0x') or offset_str.startswith('0X'):
                    offset = int(offset_str, 16)
                elif offset_str.startswith('0b') or offset_str.startswith('0B'):
                    offset = int(offset_str, 2)
                else:
                    offset = int(offset_str)
            except ValueError:
                offset_pos, offset_len = get_token_pos_len(original_line, 3, offset_str)
                print_error(original_line, offset_pos, offset_len if offset_len>0 else len(offset_str), 
                           f"Invalid offset '{offset_str}'",
                           "Expected a decimal, hex (0x...) or binary (0b...) number or a label",
                           line_number, "error", input_filename)
                sys.exit(1)  # 修复：添加退出程序
        # 根据是标签还是立即数选择 a/s 变体
        if offset_str.lower() in labels:
            # 使用 resolve_label_offset 返回的无符号偏移和方向来选择变体
            offset = unsigned_offset
            if opcode == "beq":
                opcode = "beqa" if direction == 'a' else "beqs"
            else:
                opcode = "blta" if direction == 'a' else "blts"
        else:
            # 对于立即数偏移，必须为无符号正数且在 0..255 范围内；选择加法变体
            if offset < 0 or offset > 255:
                offset_pos, offset_len = get_token_pos_len(original_line, 3, offset_str)
                print_error(original_line, offset_pos, offset_len if offset_len>0 else len(offset_str),
                           f"offset {offset} out of range [0, 255]",
                           "offset must be a non-negative number between 0 and 255 (inclusive)",
                           line_number, "error", input_filename)
                sys.exit(1)
            if opcode == "beq":
                opcode = "beqa"
            else:
                opcode = "blta"

        tokens = [opcode, tokens[1], tokens[2], str(offset)]
    
    

    # 如果是伪指令 → 替换
    elif opcode in pseudo_map:
        original_opcode = opcode
        real_inst = pseudo_map[opcode]

        # 新增：伪指令操作数数量校验
        pseudo_op_count = {
            "mov": 2, "clr": 1, "inc": 1, "dec": 1, "shl": 1, "str": 3
        }
        if len(tokens) - 1 != pseudo_op_count.get(original_opcode, 0):
            print_error(original_line, start_idx, len(opcode), 
                       f"'{original_opcode}' expects {pseudo_op_count[original_opcode]} operands, got {len(tokens)-1}",
                       f"correct syntax: {original_opcode} ... (example: {original_opcode} r0)",
                       line_number, "error", input_filename)
            sys.exit(1)
        
        if original_opcode == "mov":
            # mov rs rd → addi rs 0 rd (rs是源，rd是目标)
            tokens = [real_inst, tokens[1], "0", tokens[2]]

        elif original_opcode == "clr":
            # clr rd → sub rd rd rd
            tokens = [real_inst, tokens[1], tokens[1], tokens[1]]

        elif original_opcode == "inc":
            # inc rd → addi rd 1 rd
            tokens = [real_inst, tokens[1], "1", tokens[1]]

        elif original_opcode == "dec":
            # dec rd → subi rd 1 rd
            tokens = [real_inst, tokens[1], "1", tokens[1]]
        
        elif original_opcode == "shl":
            # shl rd → add rd rd rd
            tokens = [real_inst, tokens[1], tokens[1], tokens[1]]
        
        elif original_opcode == "str":
            # str rs1 rs2 offset → store rs1 rs2 offset (操作数格式相同，无需转换)
            tokens = [real_inst, tokens[1], tokens[2], tokens[3]]
        
        opcode = real_inst

    # 计算错误提示的起始位置（必须在伪指令替换之后）
    line_lower_for_find = original_line.lower()
    start_idx, _ = get_token_pos_len(original_line, 0, tokens[0])
        
    # 特殊处理 NOT 伪指令（需要常量支持）
    if opcode == "not":
        # 约定: tokens = ["not", RD, RS]
        if len(tokens) != 3:
            print_error(original_line, start_idx, len(opcode),
                       f"'not' expects 2 operands, got {len(tokens)-1}",
                       "correct syntax: not DST_REG SRC_REG (example: not r1 r2)",
                       line_number, "error", input_filename)
            sys.exit(1)

        # 必须声明 NOT_MASK 常量
        if 'not_mask' not in constants:
            print_error(original_line, start_idx, len(opcode),
                       f"use of undeclared constant 'not_mask'",
                       "add 'const NOT_MASK 0xFF' before using NOT instruction",
                       line_number, "error", input_filename)
            sys.exit(1)

        rd = tokens[1]
        rs = tokens[2]
        not_mask_value = constants['not_mask']['value']
        constants['not_mask']['used'] = True

        # 选择一个临时寄存器（不等于 rs 或 rd）
        tmp_reg = None
        for r in ['r0', 'r1', 'r2', 'r3']:
            if r != rd.lower() and r != rs.lower():
                tmp_reg = r
                break
        if tmp_reg is None:
            print_error(original_line, start_idx, len(opcode),
                       "no available temporary register for 'not' expansion",
                       "ensure at least one register is free to use as temporary",
                       line_number, "error", input_filename)
            sys.exit(1)

        # 展开为三条指令，均遵循 tokens 规范 [opcode, rs1, rs2/imm, rd]
        # 1. clr tmp_reg  -> sub tmp tmp tmp (tmp = 0)
        tokens_step1 = ['sub', tmp_reg, tmp_reg, tmp_reg]

        # 2. addi tmp_reg NOT_MASK tmp_reg -> tmp = tmp + NOT_MASK = NOT_MASK
        tokens_step2 = ['addi', tmp_reg, str(not_mask_value), tmp_reg]

        # 3. sub tmp_reg rs rd -> rd = tmp - rs = NOT_MASK - rs
        tokens_step3 = ['sub', tmp_reg, rs, rd]

        # 替换常量并生成三条机器码
        tokens_step1, _ = replace_constants_in_tokens(tokens_step1, line_number, original_line)
        instr1 = generate_machine_code(tokens_step1, 'sub', line_number, original_line)
        machine_code.append((line_number, instr1, f"not expand: sub {tmp_reg} {tmp_reg} {tmp_reg}"))

        tokens_step2, _ = replace_constants_in_tokens(tokens_step2, line_number, original_line)
        instr2 = generate_machine_code(tokens_step2, 'addi', line_number, original_line)
        machine_code.append((line_number, instr2, f"not expand: addi {tmp_reg} {not_mask_value} {tmp_reg}"))

        tokens_step3, _ = replace_constants_in_tokens(tokens_step3, line_number, original_line)
        instr3 = generate_machine_code(tokens_step3, 'sub', line_number, original_line)
        machine_code.append((line_number, instr3, f"not expand: sub {tmp_reg} {rs} {rd}"))

        machine_code_address += 3
        continue
    
    # 在检查操作数之前，先替换其他常量
    tokens, replaced_positions = replace_constants_in_tokens(tokens, line_number, original_line)
    
    # 校验替换后的立即数范围
    for i in range(1, len(tokens)):
        token = tokens[i]
        try:
            imm_val = parse_immediate(token, allow_exit=False)
            if imm_val < MIN_IMMEDIATE_VALUE or imm_val > MAX_IMMEDIATE_VALUE:
                imm_pos, imm_len = get_token_pos_len(original_line, i, token)
                print_error(original_line, imm_pos, imm_len if imm_len>0 else len(token),
                           f"immediate value {imm_val} out of range [{MIN_IMMEDIATE_VALUE}, {MAX_IMMEDIATE_VALUE}]",
                           "values must be between 0 and 255 (inclusive)",
                           line_number, "error", input_filename)
                sys.exit(1)
        except ValueError:
            continue  # 非立即数，跳过
    
    # 如果是 not 指令，需要在此处生成机器码
    if opcode == 'not':
        # not 指令已被转换为 sub 指令，生成机器码
        instruction = generate_machine_code(tokens, 'sub', line_number, original_line)
        machine_code.append((line_number, instruction, original_line.strip()))
        # not 指令生成1条机器码
        machine_code_address += 1
        # 跳过后续处理，因为已经处理完成
        continue
    
    # 检查是否在应该使用寄存器的位置使用了常量
    # 对于运算指令和load指令：格式是 opcode rs1 imm/rs2 rd
    # rs1 (tokens[1]) 和 rd (tokens[3]) 必须是寄存器，不能是常量
    arithmetic_load_opcodes_check = {"add", "addi", "sub", "subi", "and", "andi", "or", "ori", "load"}
    branch_store_opcodes_check = {"beqa", "beqs", "blta", "blts", "store"}
    
    if opcode in arithmetic_load_opcodes_check or opcode == "nop":
        # 检查 rs1 (tokens[1]) 和 rd (tokens[3]) 是否是被替换的常量
        for pos in [1, 3]:
            if pos in replaced_positions:
                # 使用 token 索引定位原始 token
                const_pos, const_len = get_token_pos_len(original_line, pos)
                # 提取原始文本以供提示（若可用）
                if const_len > 0:
                    orig_text = original_line[const_pos:const_pos+const_len].strip()
                else:
                    orig_text = tokens[pos]
                print_error(original_line, const_pos, const_len if const_len>0 else len(orig_text), 
                           f"expected register, got constant '{orig_text}'",
                           "use a register name instead of a constant name",
                           line_number, "error")
                sys.exit(1)
    elif opcode in branch_store_opcodes_check:
        # 分支/store指令：opcode rs1 rs2 offset
        # 这里rs1和rs2都应该是寄存器
        for pos in [1, 2]:
            if pos in replaced_positions:
                const_pos, const_len = get_token_pos_len(original_line, pos)
                if const_len > 0:
                    orig_text = original_line[const_pos:const_pos+const_len].strip()
                else:
                    orig_text = tokens[pos]
                print_error(original_line, const_pos, const_len if const_len>0 else len(orig_text), 
                           f"expected register, got constant '{orig_text}'",
                           "use a register name instead of a constant name",
                           line_number, "error")
                sys.exit(1)

    # 不再自动交换操作数位置，操作数顺序应严格为: opcode RS1 RS2 RD

    # 自动补全立即数指令 i
    # 对于分支/存储类指令（opcode rs1 rs2 offset），跳过此处对立即数位置的自动检查
    branch_like = {"beq", "blt", "beqa", "beqs", "blta", "blts", "store"}
    if tokens[0] not in branch_like:
        try:
            if len(tokens) >= 3:
                # 自动纠正：对于可交换运算（add/and/or），如果写成了 imm reg 的顺序，自动交换为 reg imm
                try:
                    commutative_ops = {"add", "and", "or", "addi", "andi", "ori"}
                    if tokens[0] in commutative_ops and len(tokens) >= 3:
                        if is_immediate_str(tokens[1]) and not is_immediate_str(tokens[2]):
                            tokens[1], tokens[2] = tokens[2], tokens[1]
                except Exception:
                    pass

                # 先检查是否是负数
                imm_str = tokens[2]
                is_negative = False
                try:
                    if imm_str.startswith('0x') or imm_str.startswith('0X'):
                        imm_val = int(imm_str, 16)
                    elif imm_str.startswith('0b') or imm_str.startswith('0B'):
                        imm_val = int(imm_str, 2)
                    else:
                        imm_val = int(imm_str)
                    
                    if imm_val < 0:
                        is_negative = True
                except ValueError:
                    pass
                
                # 如果是 and/or 类指令且立即数为负，报错
                if is_negative and tokens[0] in ["and", "or"]:
                    imm_pos, imm_len = get_token_pos_len(original_line, 2, tokens[2])
                    print_error(original_line, imm_pos, imm_len if imm_len>0 else len(tokens[2]), 
                               "logical instructions (and/or) do not support negative immediates",
                               "use positive values only for AND/OR immediate instructions",
                               line_number, "error")
                    sys.exit(1)  # 修复：添加退出程序

                # 检查tokens[2]或tokens[3]是否是立即数
                imm_found_at = -1
                try:
                    # 检查tokens[2]
                    if tokens[2].startswith('0x') or tokens[2].startswith('0X'):
                        int(tokens[2], 16)
                        imm_found_at = 2
                    elif tokens[2].startswith('0b') or tokens[2].startswith('0B'):
                        int(tokens[2], 2)
                        imm_found_at = 2
                    else:
                        int(tokens[2])
                        imm_found_at = 2
                except ValueError:
                    try:
                        # 检查tokens[3]
                        if tokens[3].startswith('0x') or tokens[3].startswith('0X'):
                            int(tokens[3], 16)
                            imm_found_at = 3
                        elif tokens[3].startswith('0b') or tokens[3].startswith('0B'):
                            int(tokens[3], 2)
                            imm_found_at = 3
                        else:
                            int(tokens[3])
                            imm_found_at = 3
                    except ValueError:
                        pass  # 没有立即数
                
                if imm_found_at != -1:
                    # 仅接受立即数位于 tokens[2]（RS2/IMM），tokens[3] 必须为目标寄存器 RD
                    if imm_found_at == 3:
                        imm_pos, imm_len = get_token_pos_len(original_line, 3, tokens[3])
                        print_error(original_line, imm_pos, imm_len if imm_len>0 else len(tokens[3]),
                                   "immediate value found in destination position",
                                   "immediate must be the third operand (RS2/IMM); destination register must be last",
                                   line_number, "error", input_filename)
                        sys.exit(1)

                    # 有立即数（tokens[2] 是立即数），为不同指令选择立即数版本
                    if tokens[0] == "add":
                        tokens = ["addi", tokens[1], tokens[2], tokens[3]]
                    elif tokens[0] == "sub":
                        tokens = ["subi", tokens[1], tokens[2], tokens[3]]
                    elif tokens[0] == "and":
                        tokens = ["andi", tokens[1], tokens[2], tokens[3]]
                    elif tokens[0] == "or":
                        tokens = ["ori", tokens[1], tokens[2], tokens[3]]

                    # 更新 opcode
                    opcode = tokens[0]
                # 如果没有立即数，不转换，继续使用原始opcode

        except (ValueError, IndexError, TypeError):
            pass

    # 检查指令是否合法
    if opcode not in opcodes:
        print_error(original_line, start_idx, len(opcode), 
                   f"unknown opcode '{opcode}'",
                   "valid opcodes: add, addi, sub, subi, and, andi, or, ori, load, store, beqa, beqs, blta, blts, nop",
                   line_number, "error")
        sys.exit(1)

    # 检查操作数数量
    branch_store_opcodes = {"beqa", "beqs", "blta", "blts", "store"}
    
    if opcode == "nop":
        if len(tokens) != 1:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       "'nop' expects 0 operands, got 1",
                       "correct syntax: nop (no operands allowed)",
                       line_number, "error")
            sys.exit(1)
    elif opcode in branch_store_opcodes:
        # 如果第四个操作数是标签名（无论 opcode 是否已带 a/s 后缀），在此处解析为无符号偏移
        if len(tokens) == 4:
            target_token = tokens[3]
            if target_token.lower() in labels:
                current_address = machine_code_address
                unsigned_offset, direction = resolve_label_offset(target_token.lower(), current_address, original_line, line_number)
                # 依据方向选择 a/s 变体（即使用户已经写了 beqa/beqs，也以实际方向为准）
                if opcode.startswith('beq'):
                    opcode = 'beqa' if direction == 'a' else 'beqs'
                elif opcode.startswith('blt'):
                    opcode = 'blta' if direction == 'a' else 'blts'
                tokens[0] = opcode
                tokens[3] = str(unsigned_offset)

        # 验证操作数数量
        if len(tokens) != 4:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"'{opcode}' expects 3 operands, got {len(tokens)-1}",
                       f"correct syntax: {opcode} REG REG IMM (example: {opcode} r0 r1 10)",
                       line_number, "error")
            sys.exit(1)
    else:
        if len(tokens) != 4:
            print_error(original_line, 0, len(original_line.rstrip('\n')), 
                       f"'{opcode}' expects 3 operands, got {len(tokens)-1}",
                       f"correct syntax: {opcode} REG REG REG (example: {opcode} r0 r1 r2)",
                       line_number, "error")
            sys.exit(1)
    
    # 检查寄存器是否合法（跳过立即数和常量）
    for i in range(1, len(tokens)):
        # 尝试转换为整数，如果是数字则跳过
        try:
            # 支持十进制、十六进制、二进制
            if tokens[i].startswith('0x') or tokens[i].startswith('0X'):
                int(tokens[i], 16)
            elif tokens[i].startswith('0b') or tokens[i].startswith('0B'):
                int(tokens[i], 2)
            else:
                int(tokens[i])
            continue  # 这是立即数，跳过检查
        except ValueError:
            pass
        
        # 不是数字，应该是寄存器或常量
        # 如果看起来像一个立即数（但前面的数值解析失败），给出更具体的错误信息
        token_candidate = tokens[i]
        if (token_candidate.startswith('0x') or token_candidate.startswith('0X') or
            token_candidate.startswith('0b') or token_candidate.startswith('0B') or
            (token_candidate and (token_candidate[0].isdigit() or token_candidate[0] == '-'))):
            # 定位该 token 在原始行中的位置（按 token 索引定位更精确）
            token_pos, token_len = get_token_pos_len(original_line, i, token_candidate)
            # 具体解析失败，使用 parse_immediate 来确定是否格式错误
            try:
                _ = parse_immediate(token_candidate, line_number, original_line, allow_exit=False, error_pos=token_pos)
            except Exception:
                print_error(original_line, token_pos if token_pos is not None else 0, token_len if token_len>0 else len(token_candidate),
                           f"invalid immediate value '{token_candidate}'",
                           "valid formats: decimal (123), hex (0xFF), binary (0b10101010); ensure binary uses only 0/1 and hex uses 0-9/A-F",
                           line_number, "error", input_filename)
                sys.exit(1)

        if tokens[i].lower() not in REGISTER_NAMES:
            # 检查是否是未声明的常量
            const_name = tokens[i].lower()
            if const_name in [c.lower() for c in constants.keys()]:
                # 这是一个常量，但还没被替换（不应该发生，因为前面已经替换了）
                # 如果出现在这里，说明在应该使用寄存器的位置使用了常量名
                # 直接按 token 索引定位原始 token 的位置（更精确可靠）
                const_idx, const_len = get_token_pos_len(original_line, i, tokens[i])
                print_error(original_line, const_idx, const_len if const_len>0 else len(tokens[i]), 
                           f"expected register, got constant '{tokens[i]}'",
                           "use a register name instead of a constant name",
                           line_number, "error")
                sys.exit(1)
            else:
                # 直接按 token 索引定位原始 token 的位置
                reg_idx, reg_len = get_token_pos_len(original_line, i, tokens[i])
                # 如果看起来像寄存器名（以 r 开头），则给出更具体的寄存器名错误提示
                if tokens[i].lower().startswith('r'):
                    print_error(original_line, reg_idx, reg_len if reg_len>0 else len(tokens[i]), 
                               f"invalid register name '{tokens[i]}'",
                               "valid registers: r0, r1, r2, r3; check for typos or out-of-range registers",
                               line_number, "error")
                else:
                    print_error(original_line, reg_idx, reg_len if reg_len>0 else len(tokens[i]), 
                               f"invalid register or undeclared constant '{tokens[i]}'",
                               "valid registers: r0, r1, r2, r3; or declare constant with: const NAME VALUE",
                               line_number, "error")
                sys.exit(1)

    # 在生成机器码之前，强制检查算术/加载类指令的目标寄存器必须放在第4位（目标寄存器在最后）
    arithmetic_load_opcodes_check = {"add", "addi", "sub", "subi", "and", "andi", "or", "ori", "load"}
    if opcode in arithmetic_load_opcodes_check:
        # 目标寄存器应为 tokens[3]
        if len(tokens) < 4 or tokens[3].lower() not in REGISTER_NAMES:
            # 尽量定位问题位置
            line_lower_for_find = original_line.lower()
            # 查找第一个寄存器作为提示位置
            hint_pos = -1
            for i in range(1, len(tokens)):
                if tokens[i].lower() in REGISTER_NAMES:
                    hint_pos, hint_len = get_token_pos_len(original_line, i, tokens[i])
                    break
            if hint_pos == -1:
                hint_pos = 0
            print_error(original_line, hint_pos, len(original_line.rstrip('\n')),
                       "destination register must be the last operand",
                       "use the form: opcode RS1 RS2 RD (destination register as the last operand)",
                       line_number, "error", input_filename)
            sys.exit(1)

    # 生成机器码
    instruction = generate_machine_code(tokens, opcode, line_number, original_line)
    machine_code.append((line_number, instruction, original_line.strip()))

    # 更新机器码地址：默认每条指令生成1条机器码
    machine_code_address += 1

# 输出结果
print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Assembly complete. {len(machine_code)} instructions generated.{Colors.RESET}\n")

# 检查未使用的常量
unused_constants = [name for name, info in constants.items() if not info['used']]
if unused_constants:
    print(f"{Colors.YELLOW}Warning: Unused constants: {', '.join(unused_constants)}{Colors.RESET}")

# 输出机器码到二进制txt文件（新建文件，不覆盖原文件）
input_basename = input_filename.rsplit('.', 1)[0]
output_file = input_basename + '_machine.txt'

# 获取命令行参数（用于指定输出格式）
output_format = "binary"  # 默认输出格式
output_hex = False
output_bin = False

# 检查是否有 -o 参数指定输出格式
i = 1
while i < len(sys.argv):
    if sys.argv[i] in ("-o", "--output"):
        if i + 1 < len(sys.argv):
            output_format = sys.argv[i + 1]
            if output_format.endswith('.hex'):
                output_hex = True
            elif output_format.endswith('.bin'):
                output_bin = True
            else:
                output_file = input_basename + '_' + output_format + '.txt'
        break
    elif sys.argv[i] in ("-f", "--format"):
        if i + 1 < len(sys.argv):
            fmt = sys.argv[i + 1]
            if fmt == "hex":
                output_hex = True
                output_file = input_basename + '_machine.hex'
            elif fmt == "bin":
                output_bin = True
                output_file = input_basename + '_machine.bin'
            elif fmt == "binary":
                output_hex = False
                output_bin = False
                output_file = input_basename + '_machine.txt'
        break
    i += 1

try:
    # 文本输出（binary string 或 hex 文本）统一使用 UTF-8 编码写入
    if output_bin:
        # 二进制文件，使用二进制写入模式
        with open(output_file, 'wb') as out_f:
            for line_num, code, original in machine_code:
                byte1 = (code >> 8) & 0xFF  # 高8位
                byte2 = code & 0xFF         # 低8位
                out_f.write(bytes([byte1, byte2]))

        print(f"\n{Colors.GREEN}Machine code saved to: {output_file} (BIN format){Colors.RESET}")
    else:
        # 文本格式（默认为二进制字符串文本或十六进制文本），使用 UTF-8 编码写入
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for line_num, code, original in machine_code:
                binary_str = f"{code:016b}"
                if output_hex:
                    hex_str = f"{code:04X}"
                    out_f.write(f"{hex_str}\n")
                else:
                    out_f.write(f"{binary_str}\n")

                if not (output_bin or output_hex):  # 只在文本模式下打印详情
                    print(f"{Colors.CYAN}Line {line_num:3d}:{Colors.RESET} {Colors.WHITE}{original:30s}{Colors.RESET} -> {Colors.YELLOW}{binary_str}{Colors.RESET}")

        if output_hex:
            print(f"\n{Colors.GREEN}Machine code saved to: {output_file} (HEX format){Colors.RESET}")
        else:
            print(f"\n{Colors.GREEN}Machine code saved to: {output_file}{Colors.RESET}")

except Exception as e:
    print(f"{Colors.RED}Error writing output file: {e}{Colors.RESET}")
    sys.exit(1)
