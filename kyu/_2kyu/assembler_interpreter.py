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


class Reg:
    def __get__(self, obj, objtype=None):
        return obj.registers.get(self)

    def __set__(self, obj, value):
        obj.registers[self] = value


class Program(metaclass=Compiler):
    stdout = io.StringIO()
    registers = {}
    labels = {}
    instructions = []
    pointer = 0
    stack = []
    compare = 0

    def parse_op_line(self, line: str):
        s = line.partition(' ')
        yield getattr(self, s[0])
        args = list(map(str.strip, filter(None, s[2].split(','))))
        if len(args) > 0:
            yield args[0].strip('\'')
        if len(args) > 1:
            if s[0] != 'msg':
                setattr(Program, args[0], Reg())
            if args[1].isnumeric():
                yield int(args[1])
            else:
                yield args[1].strip('\'')
        if len(args) > 2:
            for a in args[2:]:
                yield a.strip('\'')

    def __init__(self, text):
        for i, s in enumerate(program_text_escape(text)):
            if s.endswith(':'):
                self.labels[s.rstrip(':')] = i - len(self.labels) - 1
            else:
                self.instructions.append(tuple(self.parse_op_line(s)))

    def run(self):
        while self.pointer != -1:
            i, *args = self.instructions[self.pointer]
            print(i.__name__, ' '.join(map(str, args)))
            i(*args)
            self.pointer += 1

        return self.stdout.getvalue()

    def mov(self, reg, val):
        setattr(self, reg, getattr(self, val) if isinstance(val, str) else val)

    def add(self, reg, val):
        self.mov(reg, getattr(self, reg) + (getattr(self, val) if isinstance(val, str) else val))

    def sub(self, reg, val):
        self.add(reg, -(getattr(self, val) if isinstance(val, str) else val))

    def inc(self, reg):
        self.add(reg, 1)

    def dec(self, reg):
        self.add(reg, -1)

    def mul(self, reg, val):
        self.mov(reg, getattr(self, reg) * getattr(self, val) if isinstance(val, str) else val)

    def div(self, reg, val):
        self.mov(reg, getattr(self, reg) // getattr(self, val) if isinstance(val, str) else val)

    def call(self, label):
        self.stack.append(self.pointer)
        self.jmp(label)

    def ret(self):
        self.pointer = self.stack.pop()

    def jmp(self, label):
        self.pointer = self.labels[label]

    def cmp(self, left, right):
        self.compare = getattr(self, left) - (getattr(self, right) if isinstance(right, str) else right)

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
                if hasattr(self, a):
                    print(getattr(self, a), **kwargs, end='')
                else:
                    print(a, **kwargs, end='')

    def end(self):
        self.pointer = -2


def assembler_interpreter(program):
    return Program(program).run()
