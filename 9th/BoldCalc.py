class Expression:
    vars = {}

    def __init__(self, expr):
        self.expr = expr.replace(' ', '')

        try:
            t = self.parse()

            if t != "":
                print(t)

        except Exception as err:
            print(err.args[0])



    def parse(self):

        if self.expr.startswith('#'):
            return ""

        if "=" in self.expr:
            if self.expr.count("=") > 1:
                raise SyntaxError("Syntax error")

            t = self.expr.split('=')

            if t[0].isidentifier():

                res = self.execute_expr(t[1])
                Expression.vars["_" + t[0]] = res
                return ""

            else:
                raise SyntaxError("Assignment error")

        else:

            res = self.execute_expr(self.expr)
            return res


    def execute_expr(self, e):
        ops = ['+', '-', '*', '/', '%', ')', '(']
        start = 0
        expr = []
        for i, v in enumerate(e):
            if v in ops:
                var = e[start:i]
                if var.isdigit():
                    expr.append(var)
                elif var:
                    if ("_" + var) in self.vars:
                        expr.append("_" + var)
                    elif var.isidentifier():
                        raise NameError("Name error")
                    else:
                        raise SyntaxError("Syntax error")
                expr.append(v)
                start = i + 1
            else:
                var = e[start:]
                if var.isdigit():
                    expr.append(var)
                elif var:
                    if ("_" + var) in self.vars:
                        expr.append("_" + var)
                    elif var.isidentifier():
                        raise NameError("Name error")
                    else:
                        raise SyntaxError("Syntax error")

        try:
            print(expr)
            res = eval("".join(expr).replace('/', '//'), Expression.vars)

            return res

        except Exception:
            raise RuntimeError('Runtime error')








if __name__ == '__main__':
    import sys

    s = sys.stdin.read().split('\n')
    prog = ""
    for line in s:
        if line:
            prog += f"Expression('{line}')\n"
    exec(prog)
    # print(Expression.vars.keys())
    # print(Expression.vars.values())
