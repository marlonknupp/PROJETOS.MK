def envia_email(nome, email):
    print (f'email enviado para {nome}, dono do email {email}')

# envia email.

    return  'Email enviado'

pessoas = [
    {
        'nome': 'Felipe',
        'email':'lipezin@gmail.com'
    },
    {
        'nome': 'gabriele',
        'email': 'gabriele@gmail.com'
    },
    {
        'nome': 'joao',
        'email': 'joaozinho@gmail.com'
    },
]
for pessoa in pessoas:
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])
   