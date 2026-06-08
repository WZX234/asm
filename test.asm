;  测试文件
ADD R1 R2 R3			; 正常
SUB R2 1 R1				; 测试自动补i
AND R2 0b01010101 R0	; 进制转换
CLR R1					; 伪指令
STORE R0 R0 0			; 写内存		
FUCK YOU				; 乱写
