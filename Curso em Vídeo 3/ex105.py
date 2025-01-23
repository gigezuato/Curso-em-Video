def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    quant = maior = menor = soma = 0
    for valor in n:
        quant += 1  # len(n)
        soma += valor  # sum(n)
        if quant == 1:
            maior = menor = valor  # maior = max(n) e menor = min(n)
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
    media = round(soma / len(n), 2) 
    dados = {
        'total': quant,
        'menor': menor,
        'maior': maior,
        'media': media,
    }
    if sit:
        if media <= 5:
            dados['situação'] = 'RUIM'
        elif 5 <= media < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'BOA'
    return dados


resp = notas(5.5, 4.5, 6.5)
print(resp)