import os
import io
import contextlib
import ast
import operator as op


class Compiler(type):
    def __new__(mcs, cls_name, superclasses, attribute_dict):
        return type.__new__(mcs, cls_name, superclasses, attribute_dict)


def program_text_escape(text: str):
    for line in text.splitlines():
        r = line.split(';')[0].strip()
        if not r:
            continue
        yield r


class Reg:
    def __init__(self, name, registers):
        self.name = name
        self.registers = registers

    def get(self):
        return self.registers.get(self.name)


class Const:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class Program:
    def parse_op_line(self, line: str):
        s = line.partition(' ')
        yield getattr(self, s[0])

        tree = ast.parse(s[2].strip())
        for b in ast.walk(tree):
            if isinstance(b, ast.Continue):
                yield Reg('continue', self.registers)
            if isinstance(b, ast.Constant):
                yield Const(b.value)
            elif isinstance(b, ast.Name):
                yield Reg(b.id, self.registers)
            elif isinstance(b, ast.Str):
                yield b.s

    def __init__(self, text):
        self.stdout = io.StringIO()
        self.registers = {}
        self.labels = {}
        self.instructions = []
        self.pointer = 0
        self.stack = []
        self.compare = 0

        for i, s in enumerate(program_text_escape(text)):
            if s.endswith(':'):
                self.labels[s.rstrip(':')] = i - len(self.labels) - 1
            else:
                self.instructions.append(tuple(self.parse_op_line(s)))

    def run(self):
        try:
            while self.pointer != -1:
                i, *args = self.instructions[self.pointer]
                i(*args)
                self.pointer += 1
        except IndexError:
            return -1

        return self.stdout.getvalue()

    def mov(self, reg, val):
        self.registers[reg.name] = val.get()

    def add(self, reg, val):
        self.registers[reg.name] += val.get()

    def sub(self, reg, val):
        self.registers[reg.name] -= val.get()

    def inc(self, reg):
        self.registers[reg.name] += 1

    def dec(self, reg):
        self.registers[reg.name] -= 1

    def mul(self, reg, val):
        self.registers[reg.name] *= val.get()

    def div(self, reg, val):
        self.registers[reg.name] //= val.get()

    def call(self, label):
        self.stack.append(self.pointer)
        self.jmp(label)

    def ret(self):
        self.pointer = self.stack.pop()

    def jmp(self, label):
        self.pointer = self.labels[label.name]

    def cmp(self, left, right):
        self.compare = left.get() - right.get()

    def jne(self, label):
        if self.compare != 0:
            self.jmp(label)

    def je(self, label):
        if self.compare == 0:
            self.jmp(label)

    def jge(self, label):
        if self.compare >= 0:
            self.jmp(label)

    def jg(self, label):
        if self.compare > 0:
            self.jmp(label)

    def jle(self, label):
        if self.compare <= 0:
            self.jmp(label)

    def jl(self, label):
        if self.compare < 0:
            self.jmp(label)

    def msg(self, *args, **kwargs):
        with contextlib.redirect_stdout(self.stdout):
            for a in args:
                print(a.get(), **kwargs, end='')

    def end(self):
        self.pointer = -2


def assembler_interpreter(program):
    return Program(program).run()
