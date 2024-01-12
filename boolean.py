saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta

print(pode_executar_saque)

# -------------------------------------------

codigo_seguranca = '458'
codigo_seguranca_cadastro = '458'

pode_efeturar_pagamento = codigo_seguranca == codigo_seguranca_cadastro

print(pode_efeturar_pagamento)
