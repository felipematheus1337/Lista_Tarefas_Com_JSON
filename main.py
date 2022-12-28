import json
import os

tarefas = []
tarefas_backup = []

caminho_arquivo = os.getcwd()
caminho_arquivo += '/tarefas.json'


def ler_tarefa(tarefas_list):
    if len(tarefas_list) <= 0:
        print("\n Não há tarefas adicionadas!")
    else:
        for tarefa in tarefas_list:
            print(f'\n {tarefa}')


def desfazer_tarefa(tarefas_list):
    if len(tarefas_list) <= 0:
        raise Exception("Não é possível desfazer uma lista de tarefas vazia")
    else:
        tarefas_list.pop()


def refazer_tarefa(tarefas_list):
    if len(tarefas_list) <= 0:
        raise Exception("Não é possível refazer uma lista de tarefas vazia")
    else:
        tarefas_list.append(tarefas_backup[len(tarefas_backup) - 1])


def adicionar_tarefa(tarefas_list):
    tarefas_list.append(entrada)
    tarefas_backup.append(entrada)
    ler_tarefa(tarefas_list)


def save_tarefa_to_json(tarefas_list):
    with open(caminho_arquivo, 'w+') as arquivo:
        json.dump(
            tarefas_list,
            arquivo,
            ensure_ascii=False,
            indent=2
        )


while True:
    print('\n Comandos: listar, desfazer, refazer, exit para sair')
    entrada = input('\n Digite uma tarefa ou comando: ')
    if entrada == 'listar':
        ler_tarefa(tarefas)
    elif entrada == 'desfazer':
        desfazer_tarefa(tarefas)
    elif entrada == 'refazer':
        refazer_tarefa(tarefas)
    elif entrada == 'exit':
        save_tarefa_to_json(tarefas)
        break
    else:
        adicionar_tarefa(tarefas)
