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
    return peso / altura ** 2

#Função Para cadastro de alunos(ele chama com as variaveis n,c,p,a que são respectivamente nome, cpf, peso e altura)
#A função testa inicialmente se o cpf é valido, se o peso e altura são positivos diferentes de 0
#Caso as condições forem atendidas, cadastra o novo aluno e cria uma nova linha no vetor que armazena os treinos.
def cadastro_aluno(n, c, p, a):
    if not validar_cpf(c):
        print("CPF inválido. Tente novamente.")
        return
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
    
    exercicio = treinoAlunos[idx_aluno][idx_exercicio]
    exercicio.nomeExercicio = nome
    exercicio.numRepeticoes = rep
    exercicio.pesoExercicio = peso
    print('Exercício alterado com sucesso!')

#Função para exclusão de exercicio já cadastrado.
#Primeiramente verifica se o Index do exercicio existe, se existir exclue o exercicio
#vou fazer algumas alterações nessa parte do codigo, para mostrar a lista dos exercicios com seus respectivos index.

def exclui_exercicio(idx_aluno, idx_exercicio):
    if idx_exercicio >= len(treinoAlunos[idx_aluno]):
        print('Índice de exercício inválido. Tente novamente.')
        return
    
    treinoAlunos[idx_aluno].pop(idx_exercicio)
    print('Exercício excluído com sucesso!')

#Função para Limpar toda a lista de exercicio do usuario solicitado.
def limpa_treino(idx_aluno):
    treinoAlunos[idx_aluno] = []
    print('Treino limpo com sucesso!')

#Função chamada na opção Gerenciamento de treino do menu principal
#Ela chama as funções construidas anteriormente.
#Há alguns erros que estou resolvendo, mas atualmente está funcional
def gerenciar_treino():

    #declaração das opções.
    opcoes = {
        '1': 'Incluir um novo exercício',
        '2': 'Alterar um exercício existente',
        '3': 'Excluir um exercício específico',
        '4': 'Excluir todos os exercícios',
        '0': 'Voltar'
    }
    #Inicio do codigo propriamente dito, onde valida se a escolha que vc fez está nas opções, e lhe repassa para a opção escolhida.
    while True:
        print('Escolha uma opção:')
        for opcao, descricao in opcoes.items():
            print(f'{opcao} - {descricao}')
        opcao = input().strip()

        if opcao not in opcoes:
            print('Opção inválida. Tente novamente.')
            continue
        #Se a opção estiver entre 0 e 5 pede o nome do aluno que você vai alterar,excluir ou adicionar um treino.
        if opcao>0 and opcao<5:
            nome = input('Digite o nome ou o primeiro nome do aluno: ').strip()
            aluno, idx_aluno = buscar_aluno(nome)

        #Verificação de existencia do nome dito anteriormente.
        #Se o nome está incompleto apresenta uma sugestão.
            if aluno is None:
                sugestoes = [a.nome for a in cadAlunos if nome in a.nome.lower()]
                if sugestoes:
                    print(f'Aluno não encontrado. Você quis dizer: {", ".join(sugestoes)}?')
                else:
                    print('Aluno não encontrado')
                continue

        if opcao == '1':
            nome_exercicio = input('Digite o nome do exercício: ').strip()
            num_repeticoes = int(input('Digite o número de repetições: ').strip())
            peso_exercicio = float(input('Digite o peso utilizado no exercício: ').strip())
            insere_exercicio(idx_aluno, nome_exercicio, num_repeticoes, peso_exercicio)
        elif opcao == '2':
            idx_exercicio = int(input('Digite o índice do exercício que deseja alterar: ').strip())
            nome_exercicio = input('Digite o novo nome do exercício: ').strip()
            num_repeticoes = int(input('Digite o novo número de repetições: ').strip())
            peso_exercicio = float(input('Digite o novo peso utilizado no exercício: ').strip())
            altera_exercicio(idx_aluno, idx_exercicio, nome_exercicio, num_repeticoes, peso_exercicio)
        elif opcao == '3':
            idx_exercicio = int(input('Digite o índice do exercício que deseja excluir: ').strip())
            exclui_exercicio(idx_aluno, idx_exercicio)
        elif opcao == '4':
            limpa_treino(idx_aluno)
        elif opcao == '0':
            break
        # atualiza o status do aluno
        aluno.status = bool(treinoAlunos[idx_aluno])
        break

#Função de Buscar aluno, ela é utilizada para buscar no index o nome de um aluno, independente de caracteres maiusculos ou minusculos e independete se escreveu apenas o primeiro nome ou completo.

def buscar_aluno(nome):
    nome = nome.lower()
    for idx, aluno in enumerate(cadAlunos):
        if nome == aluno.nome.lower().split()[0]:
            return aluno, idx
    return None, None

#função para consultar o aluno pelo nome, chamado no menu Inicial.
def consulta_aluno(nome):
    aluno, _ = buscar_aluno(nome)
    if aluno:
        imc = calcula_imc(aluno.peso, aluno.altura)
        print(f'Nome: {aluno.nome}, CPF: {aluno.cpf}, Peso: {aluno.peso}, Altura: {aluno.altura}, IMC: {imc:.2f}, Status: {"Ativo" if aluno.status else "Inativo"}')
    else:
        sugestoes = [aluno.nome for aluno in cadAlunos if nome in aluno.nome.lower()]
        if sugestoes:
            print(f'Aluno não encontrado. Você quis dizer: {", ".join(sugestoes)}?')
        else:
            print('Aluno não encontrado')

#Função para atualizar o cadastro de aluno.
def atualiza_cadastro(nome, c, p, a):
    aluno, _ = buscar_aluno(nome)
    if aluno:
        aluno.cpf = c
        aluno.peso = p
        aluno.altura = a
        print('Cadastro atualizado com sucesso!')
    else:
        print('Aluno não encontrado')

#Função para excluir um aluno. (Ela exclue tanto no vetor dos alunos quanto dos treinos).
def excluir_aluno(nome):
    _, idx = buscar_aluno(nome)
    if idx is not None:
        del cadAlunos[idx]
        del treinoAlunos[idx]
        print('Aluno excluído com sucesso!')
    else:
        print('Aluno não encontrado')
#Função que retorna um relatorio com todos os alunos que atendem aos parametros.
def relatorio_alunos(status):
    for aluno in cadAlunos:
        if status == 'todos' or (status == 'ativos' and aluno.status) or (status == 'inativos' and not aluno.status):
            print(f'Nome: {aluno.nome}, Status: {"Ativo" if aluno.status else "Inativo"}')

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
            peso = float(input("Digite o peso do aluno: "))
            altura = float(input("Digite a altura do aluno: "))
            cadastro_aluno(nome, cpf, peso, altura)
        elif opcao == 2:
            gerenciar_treino()
        elif opcao == 3:
            nome = input("Digite o nome ou o primeiro nome do aluno para consulta: ").strip()
            consulta_aluno(nome)
        elif opcao == 4:
            nome = input("Digite o nome do aluno para atualizar o cadastro: ")
            cpf = input("Digite o novo CPF do aluno: ")
            peso = float(input("Digite o novo peso do aluno: "))
            altura = float(input("Digite a nova altura do aluno: "))
            atualiza_cadastro(nome, cpf, peso, altura)
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

