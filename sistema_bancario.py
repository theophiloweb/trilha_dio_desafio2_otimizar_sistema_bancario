from datetime import datetime
from random import randrange
import pytz


TZ_FORTALEZA = pytz.timezone('America/Fortaleza')
LIMITE_DIARI0 = 500
QTD_SAQUE_DIARIO = 3
saldo = 0
msg = []
dt_operacao = datetime.now(tz=TZ_FORTALEZA)
count = 0
users = []
banco_contas = []
agencia = '0001'



def criar_usuario(user):
    global users
    if user['cpf'] in [user['cpf'] for user in users]:
       return f'CPF {user["cpf"]} ja existe.'
    else:
       # Criando o usuário com a estrutura completa para possibilitar a criação da conta corrente
       user.update({'conta': [], 'saldo': 0, 'historico': []})
       users.append(user)
       print('Usário criado com sucesso.')
       return user
    
def criar_conta_corrente(cpf):  
    global banco_contas  
    prefixo = randrange(1000, 9999)
    dv = randrange(0, 9) 
    cpf_exist = [user for user in users if user['cpf'] == cpf]     
    if cpf_exist is not None:
       # Vou adicionar um registro de conta ao usuário na lista de contas      
       print('Criar conta e vincular ao usuário...')
       # vou usar o filter para verificar se  no banco_contas existe a conta
       conta = list(filter(lambda user: user['conta']['conta'] == f'{prefixo}-{dv}', banco_contas))          
       while not conta:
             prefixo = randrange(1000, 9999)
             dv = randrange(0, 9) 
             cpf_exist[0]['conta'].append({'agencia': agencia, 'conta': f'{prefixo}-{dv}'})            
             conta = list(filter(lambda user: user['conta'] == f'{prefixo}-{dv}', banco_contas))
             print(f'Conta criada com sucesso. O usuário possui {len(cpf_exist[0]["conta"])} conta(s).')
             return cpf_exist
          
    else:
        return 'CPF inválido.'      

def deposito(valor, conta):
    # Condição para saber se a QTD_OPERACOES_DIARIAS foi atingida       
    operacoes = {}
    contador = 0

    # Vou buscar a quantidade atual de operações por dia
    for user in users:

        # Filtrar uma conta da lista de contas
        search_account = [account for account in user['conta'] if account['conta'] == conta]
      
        if search_account[0]['conta'] == conta and len(user['historico']) > 0: 
           
           print('Conta encontrada. Vou realizar o depósito...')     
           print('Antes vou verificar o limite de operações por dia...')   
       
           for value in user['historico']:                            
               if value.get('dt_operacao') == dt_operacao.strftime("%d/%m/%Y"):
                  contador += 1

           if contador > 10:
              return 'Limite de operações por dia atingido. Tente amanhã. '

           else:                  
               # Adicionando o valor no dicionário
               print(f'Você tem ainda {10 - len(user["historico"])} operações, neste dia. Vou registrar o depósito...')                 
               operacoes = {'dt_operacao': dt_operacao.strftime("%d/%m/%Y"), 'valor': valor, 'tipo': 'deposito'}
               user['historico'].append(operacoes)
               user.update({'saldo': user['saldo'] + valor})                
               return extrato(user)
              
        elif search_account[0]['conta'] == conta and len(user['historico']) == 0:
            print('Você ainda nao tem um histórico. Vou registrar o depósito...')
            operacoes = {'dt_operacao': dt_operacao.strftime("%d/%m/%Y"), 'valor': valor, 'tipo': 'deposito'}
            user.update({'saldo': valor, 'historico': [operacoes]})     
            print(f'Você tem ainda {10 - len(user["historico"])} operações, neste dia. Vou registrar o depósito...')             
            return extrato(user)               
                         
        else:
            return 'Conta inválida.'       
    
    
    
def saque(conta, valor=0):
    # Vou realizar as mesmas operações que foram feitas no Depósito mas verificando se há saldo suficiente
    operacoes = {}
    contador = 0
    saldo = 0

    for user in users: # Vou percorrer a lista de dicionário users

         # Filtrar uma conta da lista de contas
        search_account = [account for account in user['conta'] if account['conta'] == conta]

        if search_account[0]['conta'] == conta and len(user['historico']) > 0: # Verificando se a conta existe
           
           print('Conta encontrada...')     
           print('Antes vou verificar o limite de operações por dia...')   
       
           for value in user['historico']:                            
               if value.get('dt_operacao') == dt_operacao.strftime("%d/%m/%Y"):
                  contador += 1

           if contador > 10:
              return 'Limite de operações por dia atingido. Tente amanhã. '

           else:     
               # Antes vou verificar se possui saldo suficiente
               saldo = user['saldo']  
               if saldo >= valor:           
                    # Adicionando o valor no dicionário
                    print(f'Você tem ainda {10 - len(user["historico"])} operações, neste dia. Vou registrar o saque...')                 
                    operacoes = {'dt_operacao': dt_operacao.strftime("%d/%m/%Y"), 'valor': valor, 'tipo': 'deposito'}
                    user['historico'].append(operacoes)
                    user.update({'saldo': user['saldo'] - valor})                
                    return extrato(user)
               else:
                    return 'Saldo insuficiente.'           
           
        else: # Vou retornar uma mensagem caso a conta seja inválida
            return 'Conta inválida.'      

def extrato(saldo, conta= None):  
    # Vou verificar se o paramentro é um dicionário ou uma string
    if type(conta) == dict:
        print(f'Extrato da conta {conta["nome"]}')
        print('-------------------------')  
        historico = conta['historico']        
        if len(historico) > 0:
            print('Opa, voce tem um historico...')
            for operacao in historico:
                for key, value in operacao.items():
                    print(f'{key} : {value}')  
            print('-------------------------') 
            print(f'Saldo disponível: {conta["saldo"]}')             
       
        
    if type(conta) == str:
         print(f'Extrato da conta {conta}')
         print('-------------------------')  
         historico = [operacao for operacao in users if operacao['conta'] == conta]
         if len(historico) > 0:
            print('Opa, voce tem um historico...')
            for operacao in historico:
                for key, value in operacao.items():
                    print(f'{key} : {value}')  
            print('-------------------------') 
            print(f'Saldo disponível: {conta["saldo"]}')               
                      


