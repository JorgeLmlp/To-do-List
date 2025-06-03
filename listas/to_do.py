import os
import sqlite3

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')
conn.commit()


def adicionar_tarefa(descricao):
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao,))
    conn.commit()
    print("Tarefa adicionada com sucesso!\n")


def listar_tarefas():
    cursor.execute('SELECT id, descricao FROM tarefas')
    tarefas = cursor.fetchall()
    if not tarefas:
        print("Sua lista está vazia.\n")
    else:
        print("Tarefas:")
        for id, descricao in tarefas:
            print(f"{id}. {descricao}")
        print()


def remover_tarefa(id):
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    print("Tarefa removida com sucesso!\n")


tarefas = []


escolha = 0
while escolha != 4:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("-" * 10 + " MENU " + "-" * 10)
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar a sua lista")
    print("4 - Sair do aplicativo")
    print("-" * 26)

    try:
        escolha = int(input("Digite sua escolha --> "))
    except ValueError:
        print("digite um número válido!")
        input("Tecle Enter para continuar...")
        continue

    if escolha == 1:
        tarefa = input("Digite uma tarefa: ")
        adicionar_tarefa(tarefa)
        input("Tecle Enter para continuar...")

    elif escolha == 2:
        listar_tarefas()
        id_remover = input(
            "Digite o ID da tarefa para remover (ou 0 para cancelar): ")

        if id_remover == '0':
            print("Remoção cancelada.\n")
        elif id_remover.isdigit():
            remover_tarefa(int(id_remover))
        else:
            print("ID inválido!\n")

        input("Tecle Enter para continuar...")

    elif escolha == 3:
        listar_tarefas()
        input("Tecle Enter para continuar...")

    elif escolha == 4:
        print("Saindo do aplicativo...")

    else:
        print("Opção inválida.")
        input("Tecle Enter para continuar...")
conn.close()
