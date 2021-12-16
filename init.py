register_file = [0] * 32

def binary(string):
    nr = 0
    for ch in string:
        nr = (ord(ch) - ord('a') + 10) + nr * 16
    binar = bin(nr)[2:]
    for i in range(32 - len(binar)):
        binar = '0' + binar
    return binar


def read_file(file_name):
    f = open(file_name, "r")
    f.readline()
    d = {}
    for line in f:
        adresa, code = line.split()
        if adresa[-1] == ":":
            adresa = adresa.replace(":", "")
        if code[0] == "<":
            pass
        else:
            b = binary(code)
            d[adresa] = b
    return d

def instruction_fetch(ip, d):
    return d[ip]

def dec_unsigned(string):
    rez = 0
    for ch in string:
        rez = ord(ch) - ord("0") + rez * 2
    return rez

def dec_signed(string):
    rez = 0
    for ch in string[:-1]:
        rez = ord(ch) - ord("0") + rez * 2
    rez -= int(string[-1]) * (2 ** (len(string) - 1))
    return rez

def instruction_decode(instr):
    def lui(string):
        register = string[7:12]
        imm = string[12:]
        return dec_unsigned(register), imm

    def addi(string):
        rd = string[7:12]
        rs1 = string[15:20]
        imm = string[20:32]
        return dec_unsigned(rd), dec_unsigned(rs1), imm

    def slli(string):
        rd = string[7:12]
        rs1 = string[15:20]
        shamt = string[20:25]
        return dec_unsigned(rd), dec_unsigned(rs1), dec_unsigned(shamt)

    def bne(string):
        #!!!!!!!!!!!!!!!!!!!!!
        return 0

    def beq(string):
        return 0

    def ori(string):
        rd = string[7:12]
        rs1 = string[15:20]
        imm = string[20:32]
        return dec_unsigned(rd), dec_unsigned(rs1), imm

    def ecall(string):
        return 0

    dicti = {("0010011", "000"):addi,("1100011","001"):bne,("1100011", "000"):beq, 
        ("0010011", "110"):ori, ("0110111",):lui, ("11000000000000000001000001110011",):"unimp", 
        ("00000000000000000000000001110011",):ecall, ("0010011", "001"):slli}

    if (instr,) in dicti:
        # apel de sistem, trebuie de vazut ce facem
        pass
    else:
        # extragem opcode-ul
        opcode = instr[-7:]
        if (opcode,) in dicti:
            dicti[(opcode,)](instr[::-1])
