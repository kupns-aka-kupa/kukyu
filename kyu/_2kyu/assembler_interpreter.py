import os
import io
import contextlib
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


class Program(metaclass=Compiler):
    stdout = io.StringIO()
    registers = {}
    labels = {}
    instructions = []
    pointer = 0
    stack = []

    def parse_op_line(self, line: str):
        s = line.partition(' ')
        yield getattr(self, s[0])
        args = list(map(str.strip, filter(None, s[2].partition(','))))
        if len(args) > 0:
            yield args[0]
        if len(args) > 2:
            yield int(args[2]) if args[2].isnumeric() else args[2]

    def __init__(self, text):
        for i, s in enumerate(program_text_escape(text)):
            if s.endswith(':'):
                self.labels[s.rstrip(':')] = i - len(self.labels) - 1
            else:
                self.instructions.append(tuple(self.parse_op_line(s)))

    def run(self):
        while self.pointer != -1:
            i, *args = self.instructions[self.pointer]
            print(args)
            i(*args)
            self.pointer += 1

        return self.stdout.getvalue()

    def mov(self, x, y):
        op.setitem(self.registers, x, self.registers[y] if y in self.registers else y)

    def add(self, x, y):
        self.registers[x] += self.registers[y] if y in self.registers else y

    def sub(self, x, y):
        self.add(x, -y)

    def inc(self, reg):
        self.add(reg, 1)

    def dec(self, reg):
        self.add(reg, -1)

    def mul(self, x, y):
        self.registers[x] *= self.registers[y] if y in self.registers else y

    def div(self, x, y):
        self.registers[x] //= self.registers[y] if y in self.registers else y

    def call(self, label):
        self.stack.append(self.pointer)
        self.pointer = self.labels[label]

    def ret(self):
        self.pointer = self.stack.pop()

    def jmp(self):
        pass

    def cmp(self):
        pass

    def jne(self):
        pass

    def je(self):
        pass

    def jge(self):
        pass

    def jg(self):
        pass

    def jle(self):
        pass

    def jl(self):
        pass

    def msg(self, *args, **kwargs):
        with contextlib.redirect_stdout(self.stdout):
            print(*args, **kwargs)

    def end(self):
        self.pointer = -2


def assembler_interpreter(program):
    return Program(program).run()
