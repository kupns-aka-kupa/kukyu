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
    op = []

    def parse_op_line(self, line: str):
        return getattr(self, line.split()[0])

    def __init__(self, text):
        for i, s in enumerate(program_text_escape(text)):
            if s.endswith(':'):
                self.labels[s.rstrip(':')] = i
            else:
                self.op += self.parse_op_line(s)

        print(self.op)

    def load(self, register):
        return self.registers.get(register)

    def call(self):
        pass

    def ret(self):
        pass

    def run(self):
        for o in self.op:
            o
        return self.stdout.getvalue()


    def mov(self):
        pass

    def inc(self):
        pass

    def dec(self):
        pass

    def add(self):
        pass

    def sub(self):
        pass

    def mul(self):
        pass

    def div(self):
        pass

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

    def call(self):
        pass

    def ret(self):
        pass

    def msg(self, *args, **kwargs):
        with contextlib.redirect_stdout(self.stdout):
            print(*args, **kwargs)

    def end(self):
        pass


def assembler_interpreter(program):
    return Program(program).run()
