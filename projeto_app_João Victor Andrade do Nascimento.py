'''
CRUD

HAMBURGUERIA




'''


print ('\n === Sitema de Hamburgueria === \n')


print ("1. Cadastro")
print ("2. Cardapio")
print ("3. Solicitar o Pedido")
print ("4. pagamento")
print ("5. Acompanhar o pedido")
print ("6. Cancelar o Pedido")
print ("0. Sair")

while True:

    escolha_menu = input("")
    if escolha_menu == '1':

        print("Cadastro do Cliente")
        nome_cliente = input("Digite o nome do cliente")
        telefone_ciente = input("digite o telefone do cliente")

    elif escolha_menu == '0':

        print("saindo do sistema")
        break



    else:
        print("opção inválida")