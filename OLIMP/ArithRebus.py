from itertools import zip_longest


def replace_all(s, d):
    res = ""
    for elem in s:
        res += str(d[elem])
    return res


def foo(n, d, expr_alf, A, B, C, res):
    nums = ''.join(set("0123456789") - set(expr_alf.values()))

    # если все цифры назначены
    if all(expr_alf.values()) or len(d) == n:

        AA = replace_all(A, expr_alf)
        BB = replace_all(B, expr_alf)
        CC = replace_all(C, expr_alf)

        if AA[0] == "0" or BB[0] == "0" or CC[0] == "0":
            return

        expr = f"{AA}+{BB}=={CC}"
        if eval(expr):
            res.append(expr.replace("==", "="))
        return

    # если это буква суммы
    if n % 3 == 2:
        # количество складываемых символов от каждого слова
        l = (n + 1) // 3

        # например: ЛО + ЩЕ = МА (mod 100), то есть пытаемся назначить букву M
        s_a, s_b = replace_all(A[-l:], expr_alf), replace_all(B[-l:], expr_alf)
        ans = str((int(s_a) + int(s_b)))[-l:]

        cor_C = ans[0]
        # если буква не назначена и цифра полученная в результате сложения доступна
        if (expr_alf[d[n]] is None) and (cor_C in nums):
            expr_alf[d[n]] = cor_C
            foo(n + 1, d, expr_alf.copy(), A, B, C, res)

        # если буква назначена и совпадает с правильной
        elif expr_alf[d[n]] == cor_C:
            foo(n + 1, d, expr_alf, A, B, C, res)

        # если буква назначена, но неправильно или не назначена и недоступна
        elif (expr_alf[d[n]] is None and cor_C not in nums) or (expr_alf[d[n]] != cor_C):
            return

    else:
        # если буквы нет или она уже назначена, то переходим к следующей
        if d[n] == "" or not (expr_alf[d[n]] is None):
            foo(n + 1, d, expr_alf, A, B, C, res)

        # если буква не назначена, то ставим ей в соответствие все возможные варианты
        elif expr_alf[d[n]] is None:
            for i in nums:
                expr_alf[d[n]] = i
                foo(n + 1, d, expr_alf.copy(), A, B, C, res)


res = []
expr = input()

a, b, ans = expr.split('+')[0], *expr.split('+')[1].split('=')
expr_alf = {i: None for i in set(a) | set(b) | set(ans)}

k = 0
d = {}
for A, B, C in zip_longest(reversed(a), reversed(b), reversed(ans)):
    d[k], d[k + 1], d[k + 2] = A if A else "", B if B else "", C if C else ""
    k += 3
foo(0, d, expr_alf, a, b, ans, res)
res.sort()
print(*res, sep='\n')