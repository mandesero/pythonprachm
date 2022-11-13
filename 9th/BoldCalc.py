import sys


class Calculator:
    vars = {}

    def __init__(self):
        self.buff = [s.replace(" ", "") for s in sys.stdin.read().split('\n') if not s.startswith('#') and len(s) != 0]
        self.parse()

    def parse(self):
        for cmd in self.buff:
            try:
                if "=" in cmd:

                    if cmd.count("=") > 1:
                        raise SyntaxError

                    var, expr = cmd.split('=')
                    if var.isidentifier():
                        res = self.execute_expr(expr)
                        self.vars["_" + var] = res
                    else:
                        raise AttributeError

                else:
                    print(self.execute_expr(cmd))

            except AttributeError:
                print("Assignment error")
            except SyntaxError:
                print('Syntax error')
            except TypeError:
                print('Syntax error')
            except NameError:
                print('Name error')
            except Exception:
                print('Runtime error')

    def execute_expr(self, expr):
        ops = "+-*/%()"
        if "()" in expr or "**" in expr or "//" in expr or "." in expr:
            raise SyntaxError

        start = 0
        e = []
        for i, v in enumerate(expr):
            if v in ops:
                var = expr[start: i]
                if var:
                    if var.isidentifier():
                        var = "_" + var

                        if v == "(":
                            raise SyntaxError

                        if var not in self.vars:
                            raise NameError
                    elif not var.isdigit():
                        raise SyntaxError

                    e.append(var)
                e.append(v)
                start = i + 1
        else:
            var = expr[start:]
            if var:
                if var.isidentifier():
                    var = "_" + var
                e.append(var)
        res = eval("".join(e).replace('/', '//'), self.vars)
        return res


if __name__ == '__main__':
    Calculator()
