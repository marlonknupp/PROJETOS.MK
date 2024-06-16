def funcao_principal():
    print('executando a funcao principal')

    def funcao_interna():
        print('executando funcao interna')
    def funcao_interna2():
        print('executando funcao interna2')


    funcao_interna()
    funcao_interna2()

funcao_principal()



