#Import da função re (utilizada para verificar correspondencias entre strings exemplo: Re, rE, re e RE)
import re

#Criação das classes utilizadas no codigo:
class Aluno:
  def __init__(self, nome, cpf, peso, altura):
    self.nome = nome
    self.cpf = cpf
    self.peso = peso
    self.altura = altura
    self.status = False

class Exercicio:
  def __init__(self, nome, repeticoes, peso):
    self.nome = nome
    self.repeticoes = repeticoes
    self.peso = peso

#Variaveis Globais: (Os vetores utilizados para armazenar os dados de treinos e alunos)
cadAlunos = []
treinoAlunos = []

#Funções do codigo:

#Função para validação de CPF (PEGUEI DO SITE DO GOV)
def validar_cpf(cpf):
    cpf = ''.join(re.findall('\d', str(cpf)))

    if (not cpf) or (len(cpf) < 11):
        return False

    inteiros = list(map(int, cpf))
    novo = inteiros[:9]

    while len(novo) < 11:
        r = sum([(len(novo)+1-i)*v for i, v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)

    if novo == inteiros:
        return True

    return False

#Função para Calculo do IMC (Peso dividido por altura ao quadrado)
def calcula_imc(peso, altura):
    peso=float(peso)
    altura=float(altura)
    return ((peso/altura)/altura)*10000

#Função Para cadastro de alunos(ele chama com as variaveis n,c,p,a que são respectivamente nome, cpf, peso e altura)
#A função testa inicialmente se o cpf é valido, se o peso e altura são positivos diferentes de 0
#Caso as condições forem atendidas, cadastra o novo aluno e cria uma nova linha no vetor que armazena os treinos.

def cadastro_aluno(n, c, p, a):
    # Verificar se o CPF já existe
    for aluno in cadAlunos:
        if aluno.cpf == c:
            print("CPF já cadastrado. Tente novamente.")
            return
    
    if not validar_cpf(c):
        print("CPF inválido. Tente novamente.")
        return
    
    if not p.isdigit() or not a.isdigit():
        print("Peso e altura devem ser valores numéricos. Tente novamente.")
        return
    
    p = float(p)
    a = float(a)
    
    if p <= 0 or a <= 0:
        print("Peso e altura devem ser valores positivos. Tente novamente.")
        return
    
    novo = Aluno(n, c, p, a)
    cadAlunos.append(novo)
    treinoAlunos.append([])


#Função para cadastro de novos exercicios.
#Verifica se o nome do exercicio ja foi cadastrado inicialmente, e se não for cadastra o novo exercicio.
def insere_exercicio(idx_aluno, nome, rep, peso):
    for exercicio in treinoAlunos[idx_aluno]:
        if exercicio.nomeExercicio.lower() == nome.lower():
            print('Esse exercício já existe no treino do aluno. Tente novamente.')
            return
    
    novo_exercicio = Exercicio(nome, rep, peso)
    treinoAlunos[idx_aluno].append(novo_exercicio)
    print('Exercício inserido com sucesso!')

#Função para alterar exercicios já cadastrados.
#Primeiramente verifica se o Index do exercicio existe, se existir altera o exercicio.
#vou fazer algumas alterações nessa parte do codigo, para mostrar a lista dos exercicios com seus respectivos index.
def altera_exercicio(idx_aluno, idx_exercicio, nome, rep, peso):
    if idx_exercicio >= len(treinoAlunos[idx_aluno]):
        print('Índice de exercício inválido. Tente novamente.')
        return
    
    print(f'Você está prestes a alterar o exercício: {treinoAlunos[idx_aluno][idx_exercicio].nome}')
    confirmacao = input('Tem certeza que deseja alterar este exercício? (1 para Sim, 2 para Não): ')
    if confirmacao == '1':
        exercicio = treinoAlunos[idx_aluno][idx_exercicio]
        exercicio.nomeExercicio = nome
        exercicio.numRepeticoes = rep
        exercicio.pesoExercicio = peso
        print('Exercício alterado com sucesso!')
    else:
        print('Operação cancelada.')

#Função para exclusão de exercicio já cadastrado.
#Primeiramente verifica se o Index do exercicio existe, se existir exclue o exercicio
#vou fazer algumas alterações nessa parte do codigo, para mostrar a lista dos exercicios com seus respectivos index.

def exclui_exercicio(idx_aluno, idx_exercicio):
    if idx_exercicio >= len(treinoAlunos[idx_aluno]):
        print('Índice de exercício inválido. Tente novamente.')
        return
    
    print(f'Você está prestes a excluir o exercício: {treinoAlunos[idx_aluno][idx_exercicio].nome}')
    confirmacao = input('Tem certeza que deseja excluir este exercício? (1 para Sim, 2 para Não): ')
    if confirmacao == '1':
        treinoAlunos[idx_aluno].pop(idx_exercicio)
        print('Exercício excluído com sucesso!')
    else:
        print('Operação cancelada.')

#Função para Limpar toda a lista de exercicio do usuario solicitado.
def limpa_treino(idx_aluno):
    print('Você está prestes a excluir todos os exercícios deste aluno.')
    confirmacao = input('Tem certeza que deseja excluir todos os exercícios? (1 para Sim, 2 para Não): ')
    if confirmacao == '1':
        treinoAlunos[idx_aluno] = []
        print('Treino limpo com sucesso!')
    else:
        print('Operação cancelada.')


#Função para mostrar todos os treinos de um determinado usuario:
def mostra_treinos(idx_aluno):
    treinos = treinoAlunos[idx_aluno]
    mostra_aluno = cadAlunos[idx_aluno]
    print(f'Treinos do aluno {mostra_aluno.nome}: \n')
    for idx, treino in enumerate(treinos):
        print(f'Index: {idx}, Exercício: {treino.nome}, Repetições: {treino.repeticoes}, Peso: {treino.peso}\n')

#Função chamada na opção Gerenciamento de treino do menu principal
#Ela chama as funções construidas anteriormente.
#Há alguns erros que estou resolvendo, mas atualmente está funcional
def gerenciar_treino():
    opcoes = {
        '1': 'Incluir um novo exercício',
        '2': 'Alterar um exercício existente',
        '3': 'Excluir um exercício específico',
        '4': 'Excluir todos os exercícios',
        '0': 'Voltar'
    }

    while True:
        print('Escolha uma opção:')
        for opcao, descricao in opcoes.items():
            print(f'{opcao} - {descricao}')
        opcao = input().strip()

        if opcao not in opcoes:
            print('Opção inválida. Tente novamente.')
            continue

        if opcao == '0':
            break

        nome = input('Digite o nome ou o primeiro nome do aluno: ').strip()
        aluno, idx_aluno = escolher_aluno(nome)
        if aluno is None:
            print('Aluno não encontrado')
            continue

        mostra_treinos(idx_aluno)

        if opcao == '1':
            nome_exercicio = input('Digite o nome do exercício: ').strip()
            num_repeticoes = input('Digite o número de repetições: ').strip()
            peso_exercicio = input('Digite o peso utilizado no exercício: ').strip()
            if not num_repeticoes.isdigit() or not peso_exercicio.isdigit():
                print("Numero de repetições e peso devem ser um valor numérico. Tente novamente.")
                return            
            num_repeticoes = int(num_repeticoes)
            peso_exercicio = float(peso_exercicio)
            if num_repeticoes <= 0 or peso_exercicio<=0:
                print("Numero de repetições e peso devem um valor positivo. Tente novamente.")
                return
            insere_exercicio(idx_aluno, nome_exercicio, num_repeticoes, peso_exercicio)
        elif opcao == '2':
            idx_exercicio = input('Digite o índice do exercício que deseja alterar: ').strip()
            nome_exercicio = input('Digite o novo nome do exercício: ').strip()
            num_repeticoes = input('Digite o novo número de repetições: ').strip()
            peso_exercicio = input('Digite o novo peso utilizado no exercício: ').strip()
            if not num_repeticoes.isdigit() or not peso_exercicio.isdigit() or not idx_exercicio.isdigit():
                print("O Index do exercicio, numero de repetições e peso devem ser um valor numérico. Tente novamente.")
                return
            idx_exercicio=int(idx_exercicio)            
            num_repeticoes = int(num_repeticoes)
            peso_exercicio = float(peso_exercicio)
            if num_repeticoes <= 0 or peso_exercicio<=0:
                print("Numero de repetições e peso devem um valor positivo. Tente novamente.")
                return            
            altera_exercicio(idx_aluno, idx_exercicio, nome_exercicio, num_repeticoes, peso_exercicio)
        elif opcao == '3':
            idx_exercicio = input('Digite o índice do exercício que deseja excluir: ').strip()
            if not idx_exercicio.isdigit():
                print("O Index do exercicio deve ser um valor numérico. Tente novamente.")
                return
            idx_exercicio=int(idx_exercicio)            
            exclui_exercicio(idx_aluno, idx_exercicio)
        elif opcao == '4':
            limpa_treino(idx_aluno)

        # atualiza o status do aluno
        aluno.status = bool(treinoAlunos[idx_aluno])
        break


#Função de Buscar aluno, ela é utilizada para buscar no index o nome de um aluno, independente de caracteres maiusculos ou minusculos e independete se escreveu apenas o primeiro nome ou completo.

def buscar_aluno(nome):
    for i, aluno in enumerate(cadAlunos):
        if aluno.nome.lower() == nome.lower():
            return aluno, i
    return None, None
#Função para apresentar as opções de nomes semelhantes e o usuario escolher:
def escolher_aluno(nome):
    aluno, idx = buscar_aluno(nome)
    if aluno:
        return aluno, idx
    else:
        sugestoes = [a.nome for a in cadAlunos if nome in a.nome.lower()]
        if sugestoes:
            print(f'Aluno não encontrado. Você quis dizer: {", ".join(sugestoes)}?')
            for i, sugestao in enumerate(sugestoes):
                print(f"{i + 1}. {sugestao}")
            escolha = input(f"Selecione o número do aluno que você deseja consultar, ou 0 para cancelar:").strip()
            if escolha.isdigit() and 0 < int(escolha) <= len(sugestoes):
                aluno_sugerido, idx = buscar_aluno(sugestoes[int(escolha) - 1])
                return aluno_sugerido, idx
            else:
                 print('Operação cancelada.')
        else:
            print('Aluno não encontrado')
    return None, None

#função para consultar o aluno pelo nome, chamado no menu Inicial.
def consulta_aluno(nome):
    aluno, _ = escolher_aluno(nome)

    if aluno:
        imc = calcula_imc(aluno.peso, aluno.altura)
        print(f'Nome: {aluno.nome}, CPF: {aluno.cpf}, Peso: {aluno.peso}, Altura: {aluno.altura}, IMC: {imc:.2f}, Status: {"Ativo" if aluno.status else "Inativo"}')
    else:
        print('Operação cancelada.')



#Função para atualizar o cadastro de aluno.
def atualiza_cadastro():
    opcoes = {
        '1': 'alterar Nome',
        '2': 'alterar CPF',
        '3': 'alterar Peso',
        '4': 'Alterar Altura',
        '5': 'Alterar tudo',
        '0': 'Voltar'
    }

    while True:
        print('Escolha uma opção:')
        for opcao, descricao in opcoes.items():
            print(f'{opcao} - {descricao}')
        opcao = input().strip()

        if opcao not in opcoes:
            print('Opção inválida. Tente novamente.')
            continue

        if opcao == '0':
            break

        nome = input('Digite o nome ou o primeiro nome do aluno: ').strip()
        aluno, idx_aluno = escolher_aluno(nome)
        if aluno is None:
            print('Aluno não encontrado')
            continue

        if opcao == '1':
            novo_nome = input('Digite o nome para alteração: ').strip()
            aluno.nome = novo_nome
            print('Cadastro atualizado com sucesso!')

        elif opcao == '2':
            novo_cpf=input("Digite o novo CPF para alteração: ")
            for aluno in cadAlunos:
                if aluno.cpf == novo_cpf:
                    print("CPF já cadastrado. Tente novamente.")
                    return
            
            if not validar_cpf(novo_cpf):
                print("CPF inválido. Tente novamente.")
                return            
            print('Cadastro atualizado com sucesso!')
            
            aluno.cpf = novo_cpf

        elif opcao == '3':
            novo_peso = input("Digite o valor do novo peso em quilogramas: ")

            if not novo_peso.isdigit():
                print("Peso deve ser um valor numérico. Tente novamente.")
                return
            
            novo_peso = float(novo_peso)
            if novo_peso <= 0:
                print("Peso deve ser um valor positivo. Tente novamente.")
                return
            
            aluno.peso = novo_peso
            print('Cadastro atualizado com sucesso!')

        elif opcao == '4':
            nova_altura = input("Digite o valor da nova altura em centímetros: ")
            if not nova_altura.isdigit():
                print("Altura deve ser um valor numérico. Tente novamente.")
                return
            
            nova_altura = float(nova_altura)
            if nova_altura <= 0:
                print("Altura deve ser um valor positivo. Tente novamente.")
                return
            
            aluno.altura = nova_altura
            print('Cadastro atualizado com sucesso!')

        elif opcao=='5':
            novo_nome = input('Digite o nome para alteração: ').strip()
            novo_cpf = input("Digite o novo CPF para alteração: ")
            if novo_cpf==aluno.cpf:
                aluno.cpf = novo_cpf
            elif(novo_cpf!=aluno.cpf):
                for aluno in cadAlunos:
                    if aluno.cpf == novo_cpf:
                        print("CPF já cadastrado. Tente novamente.")
                        return
                if not validar_cpf(novo_cpf):
                    print("CPF inválido. Tente novamente.")
                    return

            novo_peso = input("Digite o valor do novo peso em quilogramas: ")
            if not novo_peso.isdigit():
                print("Peso deve ser um valor numérico. Tente novamente.")
                return
            
            novo_peso = float(novo_peso)
            if novo_peso <= 0:
                print("Peso deve ser um valor positivo. Tente novamente.")
                return

            nova_altura = input("Digite o valor da nova altura em centímetros: ")
            if not nova_altura.isdigit():
                print("Altura deve ser um valor numérico. Tente novamente.")
                return
            
            nova_altura = float(nova_altura)
            if nova_altura <= 0:
                print("Altura deve ser um valor positivo. Tente novamente.")
                return
            
            aluno.nome = novo_nome
            aluno.cpf = novo_cpf
            aluno.peso = novo_peso
            aluno.altura = nova_altura
            print('Cadastro atualizado com sucesso!')


#Função para excluir um aluno. (Ela exclue tanto no vetor dos alunos quanto dos treinos).
def excluir_aluno(nome):
    aluno, idx = escolher_aluno(nome)
    if aluno is None:
        return
    if idx is not None:
        print(f'Você está prestes a excluir o seguinte aluno:\nNome: {aluno.nome}, CPF: {aluno.cpf}, Peso: {aluno.peso}, Altura: {aluno.altura}')
        confirmacao = input("Tem certeza que deseja excluir este aluno? Digite 1 para confirmar, 2 para cancelar: ").strip()
        if confirmacao == '1':
            del cadAlunos[idx]
            del treinoAlunos[idx]
            print('Aluno excluído com sucesso!')
        else:
            print('Operação de exclusão cancelada.')
    else:
        print('Aluno não encontrado')

#Função que retorna um relatorio com todos os alunos que atendem aos parametros.
def relatorio_alunos(status):
    for idx, aluno in enumerate(cadAlunos):
        if status == 'todos' or (status == 'ativos' and aluno.status) or (status == 'inativos' and not aluno.status):
            numero_treinos = len(treinoAlunos[idx])
            imc = calcula_imc(aluno.peso, aluno.altura)
            print(f'Nome: {aluno.nome}, CPF: {aluno.cpf}, Peso: {aluno.peso}, Altura: {aluno.altura}, IMC: {imc:.2f}, Status: {"Ativo" if aluno.status else "Inativo"}, Número de Treinos: {numero_treinos}')

#Função do menu inicial.
def menu_principal():
    while True:
        print("Bem vindo ao sistema")
        print("1 - Cadastrar aluno")
        print("2 - Gerenciar treino")
        print("3 - Consultar aluno")
        print("4 - Atualizar cadastro do aluno")
        print("5 - Excluir aluno")
        print("6 - Relatório de alunos")
        print("0 - Sair do sistema")
        opcao = input("Escolha uma opção: ").strip()
        try:
            opcao = int(opcao)
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")
            continue

        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            cpf = input("Digite o CPF do aluno: ")
            peso = input("Digite o peso do aluno em quilogramas: ")
            altura = input("Digite a altura do aluno em centímetros: ")
            cadastro_aluno(nome, cpf, peso, altura)
        elif opcao == 2:
            gerenciar_treino()
        elif opcao == 3:
            nome = input("Digite o nome ou o primeiro nome do aluno para consulta: ").strip()
            consulta_aluno(nome)
        elif opcao == 4:
            atualiza_cadastro()
        elif opcao == 5:
            nome = input("Digite o nome do aluno para excluir o cadastro: ")
            excluir_aluno(nome)
        elif opcao == 6:
            status = input("Visualizar (todos, ativos, inativos): ")
            relatorio_alunos(status)
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

#Chamada da função do menu inicial.
menu_principal()

