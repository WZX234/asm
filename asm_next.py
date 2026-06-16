import sys

version = "build 3000"

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

# 报错输出
def print_error(filename, original_line, error_pos, error_len, line_number, message, error_type="error", hint=None):
    """
    Args:
        filename: 文件地址
        original_line: 原始代码行
        error_pos: 错误位置的起始索引(从0开始)
        error_len: 错误部分的长度
        line_number: 行号
        message: 错误消息
        error_type: 错误类型
        hint: 可选的修复建议
    """
    print(f"{CYAN}Traceback (most recent call last):{RESET}")
    print(f"  {CYAN}File \"{filename}\", line {line_number}{RESET}")
    print(f"    {WHITE}{original_line.rstrip('\n')}{RESET}")
    pos = max(0, error_pos)
    mark_len = max(1, error_len)
    print("    " + " " * pos + f"{RED}{'^' * mark_len}{RESET}")
    print(f"{RED}{error_type}: {WHITE}{message}{RESET}")
    if hint:
        print(f"{CYAN}Note: {WHITE}{hint}{RESET}")
    sys.exit(1)

# 获取参数
parameters = sys.argv[1:]

if len(parameters) == 0:
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
    print(f"  {CYAN}Assembler {BOLD}{version}{RESET}{YELLOW}")
    input(f"{WHITE}Press Enter to exit...{RESET}")
    sys.exit(0)

# 版本信息
if "-v" in parameters or "--version" in parameters:
    print(f"{YELLOW}Assembler {BOLD}{version}{RESET}{YELLOW}")
    print("Assembler for Next-Gen Assembly Language")
    print(f"Usage: python asm_next.py <file>{RESET}")
    sys.exit(0)

# 帮助信息
if "-h" in parameters:
    print(f"""{CYAN}
Usage: python script.py <input_file>
Read and process target text file.
 Arguments:
    input_file      Path to target text file (required)
 Options:
    -h, --help      Show this help message and exit
 Error Cases:
    1. No file argument provided
    2. Target file not found
    3. File cannot decode as UTF-8 text
    4. Permission denied when reading file
For more content, please refer to \'README.md\'.{RESET}
    """)
    sys.exit(0)

# 尝试读取文件
try:
    with open(parameters[0], 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"{RED}Error: File \'{parameters[0]}\' does not exist!{RESET}")
    sys.exit(1)
except UnicodeDecodeError:
    print(f"{RED}Error: File \'{parameters[0]}\' is not a text file!{RESET}")
    sys.exit(1)
except PermissionError:
    print(f"{RED}Error: Permission denied when reading file \'{parameters[0]}\'!{RESET}")
    sys.exit(1)
except OSError:
    print(f"{RED}Error: OSError when reading file \'{parameters[0]}\'!{RESET}")
    sys.exit(1)
except Exception:
    print(f"{RED}Unknow Error{RESET}")
    sys.exit(1)

# 操作码
opcodes = {
    "add"  : "0000",
    "addi" : "0001",
    "sub"  : "0010",
    "subi" : "0011",
    "and"  : "0100",
    "andi" : "0101",
    "or"   : "0110",
    "ori"  : "0111",
    "load" : "1000",
    "store": "1001",
    "beqa" : "1010",
    "beqs" : "1011",
    "blta" : "1100",
    "blts" : "1101",
    "nop"  : "1110",
}

# 寄存器
regs = {
    "r0": "00",
    "r1": "01",
    "r2": "10",
    "r3": "11",
}

# 立即数映射
imm_map = {
    # addi rd, rs, imm / load rd, offset(rs)
    "addi": 2,
    "subi": 2,
    "andi": 2,
    "ori": 2,
    "add": 2,
    "sub": 2,
    "and": 2,
    "or": 2,
    "load": 2,
    # store rs, offset(rd) / beqa rs, rt, imm
    "store": 3,
    "beqa": 3,
    "beqs": 3,
    "blta": 3,
    "blts": 3,
}

# 负数指令切换表
neg_op_switch = {
    "addi": "subi",
    "subi": "addi",
    "beqa": "beqs",
    "beqs": "beqa",
    "blta": "blts",
    "blts": "blta",
}

instructions = []
line_num = 0

for oline in lines:

    line_num += 1

    # 去掉换行
    line = oline.rstrip("\n")

    # 截断分号注释
    comment_pos = line.find(';')
    if comment_pos != -1:
        line = line[:comment_pos]

    # 去除首尾空白，空行直接跳过
    clean_line = line.strip()
    if not clean_line:
        continue

    # 转小写并分词
    tokens = line.lower().split()

    # 获取指令操作码
    opcode = tokens[0]

    # 获取立即数位置
    imm_idx = imm_map.get(opcode)

    # 检测立即数并交换位置
    try:
        int(tokens[imm_idx], 0)
    except ValueError:
        if opcode in ("add", "addi", "sub", "subi", "and", "andi", "or", "ori", "load"):
            tokens[1], tokens[2] = tokens[2], tokens[1]
        elif opcode == "store":
            tokens[2], tokens[3] = tokens[3], tokens[2]
    
    # 处理立即数
    if imm_idx is not None:
        imm = tokens[imm_idx]
        imm_sign = 1 if imm[0] == '-' else None
        imm = bin(abs(int(imm, 0)))[2:].zfill(8) # 转八位二进制
    else:
        imm = None
        imm_sign = None
    
    # 立即数指令没有加i, 自动加i
    if opcode in ("add", "sub", "and", "or") and imm is not None:
        print(f"{YELLOW}[Warning] Auto fixed: {opcode} → {opcode}i{RESET}")
        opcode = opcode + "i"
    
    # 若立即数为负, 则将可以切换的指令切换为对应的负数指令
    if imm_sign and opcode in neg_op_switch:
        opcode = neg_op_switch[opcode]

    if opcode in ("add", "sub", "and", "or"):
        instruction = opcodes[opcode] + regs[tokens[3]] + regs[tokens[1]] + regs[tokens[2]] + "000000"
        print(f"{CYAN}Line   {line_num}: {WHITE}{oline[:-3]}{RESET}  -> {YELLOW}{instruction}{RESET}")
        instructions.append(instruction + "\n")
        
    elif opcode in ("addi", "subi", "andi", "ori", "load"):
        instruction = opcodes[opcode] + regs[tokens[3]] + regs[tokens[1]] + imm
        print(f"{CYAN}Line   {line_num}: {WHITE}{oline[:-3]}{RESET}  -> {YELLOW}{instruction}{RESET}")
        instructions.append(instruction + "\n")

    elif opcode in ("store", "beqa", "beqs", "blta", "blts"):
        instruction = opcodes[opcode] + imm[:2] + regs[tokens[2]] + regs[tokens[1]] + imm[2:]
        print(f"{CYAN}Line   {line_num}: {WHITE}{oline[:-3]}{RESET}  -> {YELLOW}{instruction}{RESET}")
        instructions.append(instruction + "\n")
    
    elif opcode == "nop":
        instruction = opcodes[opcode] + "000000000000"
        print(f"{CYAN}Line   {line_num}: {WHITE}{oline[:-3]}{RESET}  -> {YELLOW}{instruction}{RESET}")
        instructions.append(instruction + "\n")
    
    else:
        print_error(parameters[0], oline, 0, len(opcode), line_num, f"unknown opcode \'{opcode}\'", "SyntaxError", "valid opcodes: add, addi, sub, subi, and, andi, or, ori, load, store, beqa, beqs, blta, blts, nop")

# 保存文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(instructions)
# 完成
print(f"{WHITE}Done!{RESET}")
sys.exit(0)