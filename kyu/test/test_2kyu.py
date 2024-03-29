import unittest
from .._2kyu.regular_expression___check_if_divisible_by_0b111__7_ import solution
from .._2kyu.assembler_interpreter import assembler_interpreter


class AsmInterpreterTestCase(unittest.TestCase):

    def test_first_program(self):
        program = '''
        ; My first program
        mov  a, 5
        inc  a
        call function
        msg  '(5+1)/2 = ', a    ; output message
        end

        function:
            div  a, 2
            ret
        '''

        self.assertEqual(assembler_interpreter(program), '(5+1)/2 = 3')

    def test_factorial(self):
        program_factorial = '''
        mov   a, 5
        mov   b, a
        mov   c, a
        call  proc_fact
        call  print
        end

        proc_fact:
            dec   b
            mul   c, b
            cmp   b, 1
            jne   proc_fact
            ret

        print:
            msg   a, '! = ', c ; output text
            ret
        '''

        self.assertEqual(assembler_interpreter(program_factorial), '5! = 120')

    def test_fibonacci(self):
        program_fibonacci = '''
        mov   a, 8            ; value
        mov   b, 0            ; next
        mov   c, 0            ; counter
        mov   d, 0            ; first
        mov   e, 1            ; second
        call  proc_fib
        call  print
        end

        proc_fib:
            cmp   c, 2
            jl    func_0
            mov   b, d
            add   b, e
            mov   d, e
            mov   e, b
            inc   c
            cmp   c, a
            jle   proc_fib
            ret

        func_0:
            mov   b, c
            inc   c
            jmp   proc_fib

        print:
            msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
            ret
        '''

        self.assertEqual(assembler_interpreter(program_fibonacci), 'Term 8 of Fibonacci series is: 21')

    def test_mod(self):
        program_mod = '''
        mov   a, 11           ; value1
        mov   b, 3            ; value2
        call  mod_func
        msg   'mod(', a, ', ', b, ') = ', d        ; output
        end

        ; Mod function
        mod_func:
            mov   c, a        ; temp1
            div   c, b
            mul   c, b
            mov   d, a        ; temp2
            sub   d, c
            ret
        '''

        self.assertEqual(assembler_interpreter(program_mod), 'mod(11, 3) = 2')

    def test_gcd(self):
        program_gcd = '''
        mov   a, 81         ; value1
        mov   b, 153        ; value2
        call  init
        call  proc_gcd
        call  print
        end

        proc_gcd:
            cmp   c, d
            jne   loop
            ret

        loop:
            cmp   c, d
            jg    a_bigger
            jmp   b_bigger

        a_bigger:
            sub   c, d
            jmp   proc_gcd

        b_bigger:
            sub   d, c
            jmp   proc_gcd

        init:
            cmp   a, 0
            jl    a_abs
            cmp   b, 0
            jl    b_abs
            mov   c, a            ; temp1
            mov   d, b            ; temp2
            ret

        a_abs:
            mul   a, -1
            jmp   init

        b_abs:
            mul   b, -1
            jmp   init

        print:
            msg   'gcd(', a, ', ', b, ') = ', c
            ret
        '''

        self.assertEqual(assembler_interpreter(program_gcd), 'gcd(81, 153) = 9')

    def test_fail(self):
        program_fail = '''
        call  func1
        call  print
        end

        func1:
            call  func2
            ret

        func2:
            ret

        print:
            msg 'This program should return -1'
        '''

        self.assertEqual(assembler_interpreter(program_fail), -1)

    def test_power(self):
        program_power = '''
        mov   a, 2            ; value1
        mov   b, 10           ; value2
        mov   c, a            ; temp1
        mov   d, b            ; temp2
        call  proc_func
        call  print
        end

        proc_func:
            cmp   d, 1
            je    continue
            mul   c, a
            dec   d
            call  proc_func

        continue:
            ret

        print:
            msg a, '^', b, ' = ', c
            ret
        '''

        self.assertEqual(assembler_interpreter(program_power), '2^10 = 1024')


class Kata2TestCase(unittest.TestCase):

    def test_check_divisible_by_7(self):
        for num in range(0, 101):
            self.assertEqual(solution(num), num % 7 == 0)


if __name__ == '__main__':
    unittest.main()
