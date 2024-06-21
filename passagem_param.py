def mensagem(nome):
    print('Executando nome...')
    return f"Oi {nome}"


def mensagem_longa(nome):
    print('Executando mensagem longa...')
    return f"Olá {nome}, tudo bem com você?"

def executar(funcao):
    print('Executando "executar."')
    return funcao("Luiza")

print (executar(mensagem))
print (executar(mensagem_longa))