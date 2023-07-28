#Exercício 25:
#Elabore um programa com um menu que permita
#ao utilizador escolher escrever uma lista de
#compras, ler a lista de compras e sair


def lerficheiro():
    ficheiro=open("Lista.txt",'r')
    lista=[]
    lista=ficheiro.readlines()
    ficheiro.close
    return lista

def escreverficheiro(lista):
    ficheiro=open("Lista.txt", 'w') #w serve para colocar o ficheiro em modo escrita 
    for item in lista:
        ficheiro.write(item)
    ficheiro.close
    
lista2=lerficheiro()
    
while True:
    print("*************************************************")
    opcao = int (input ("\n 1 - ler ficheiros \n 2 - escrever no ficheiro \n 3 - sair"))
    print("*************************************************")
    
    if opcao==1:
        for item in lista2:
            print(item)
            
    elif opcao==2:
        c=input("qual o item a adicionar")
        lista2.append(c)
        
    elif opcao==3:
        escreverficheiro(lista2)
        break
    else:
        print ("opção incorreta")
        
