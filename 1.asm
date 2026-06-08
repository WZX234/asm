; 示例汇编程序：实现简单的数值运算 + 条件分支 + 访存操作
; 注释以分号开头，支持十进制/十六进制/二进制立即数

; ==================== 常量定义（支持十进制/十六进制/二进制） ====================
const MAX_VAL 255       ; 十进制常量
const MASK 0xFF         ; 十六进制常量
const STEP 0b00000001   ; 二进制常量（步长1）

; ==================== 标签定义（用于分支跳转） ====================
start:                  ; 程序入口标签
    mov r0 r1         ; 伪指令：mov → 等价于 addi r0 0 r1（r1 = r0 + 0）
    clr r2              ; 伪指令：clr → 等价于 sub r2 r2 r2（清空r2）
    inc r1              ; 伪指令：inc → 等价于 addi r1 1 r1（r1 += 1）
    
    ; 算术指令（寄存器/立即数版本）
    add r1 r2 r3        ; r3 = r1 + r2（寄存器版本）
    addi r3 STEP r3     ; r3 += STEP（立即数版本，常量替换后为 addi r3 1 r3）
    sub r3 r1 r2        ; r2 = r3 - r1（寄存器版本）
    subi r2 5 r2        ; r2 -= 5（立即数版本）
    and r1 MASK r3      ; r3 = r1 & MASK（常量替换后为 and r1 255 r3）
    andi r3 0x0F r3     ; r3 &= 0x0F（十六进制立即数）
    or r2 r3 r1         ; r1 = r2 | r3（寄存器版本）
    ori r1 0b10 r1      ; r1 |= 2（二进制立即数）
    
    ; 访存指令
    load r0 r1 r2       ; 从内存地址 (r0 + r1) 加载数据到 r2
    store r0 r2 10      ; 将 r2 存储到内存地址 (r0 + r2 + 10)
    
    ; 分支指令（基于标签跳转，汇编器自动计算偏移）
    beqa r1 r2 loop     ; 若 r1 == r2，跳转到 loop 标签（无符号相等分支）
    blta r1 r3 exit     ; 若 r1 < r3（无符号），跳转到 exit 标签
    
loop:                   ; 循环标签
    dec r3              ; 伪指令：dec → 等价于 subi r3 1 r3（r3 -= 1）
    blts r3 0 exit      ; 若 r3 < 0（有符号），跳转到 exit 标签
    beqs r3 MAX_VAL loop; 若 r3 == MAX_VAL（常量替换后255），跳回 loop
    
exit:                   ; 退出标签
    nop                 ; 空指令（占位/结束）