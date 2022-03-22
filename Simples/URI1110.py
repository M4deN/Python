#tentei fazer esse ex em C, notei que estava ficando grande de mais, fui vasculhar o meu github de estrtura de dados e notei que o havia feito ja em python para a disciplina
# estava usando fila para tentar resolver em C e então estava se tornando custoso como aprendemos em estrtura de dados a usar funções prontas do python, decidi fazer em python
#a logica de estrtura de dados e a mesma que aplicaria em C mas o custo de se fazer em python é muito menor
while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        l.append(i + 1)
    res = []
    while (len(l) > 1):
        res.append(l[0])
        l.pop(0)
        l.append(l[0])
        l.pop(0)

    print('Discarded cards: ', end='')
    for i in range(n - 1):
        print(res[i], end='')
        if (i != n - 2):
            print(', ', end='')
    print()
    print('Remaining card:', l[0])
