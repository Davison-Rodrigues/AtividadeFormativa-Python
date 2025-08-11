import json

def salvar_json(nome_arquivo, lista):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)

def carregar_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def listar(lista, nome_modulo):
    if len(lista) == 0:
        print(f"=== lista de {nome_modulo} vazia ===")
    else:
        print(f"{nome_modulo} cadastrados:")
        for item in lista:
            print(item)

def excluir(lista, chave, nome_modulo, nome_arquivo):
    codigo = int(input(f"digite o código do(a) {nome_modulo} para excluir: "))
    item_excluir = None
    for item in lista:
        if item[chave] == codigo:
            item_excluir = item
            break
    if item_excluir is None:
        print(f"{nome_modulo} não encontrado!")
    else:
        lista.remove(item_excluir)
        salvar_json(nome_arquivo, lista)
        print(f"{nome_modulo} excluído com sucesso!")

def editar(lista, chave, campos, nome_modulo, nome_arquivo):
    codigo = int(input(f"digite o código do(a) {nome_modulo} para editar: "))
    for item in lista:
        if item[chave] == codigo:
            for campo in campos:
                valor = input(f"digite o novo {campo}: ")
                item[campo] = int(valor) if valor.isdigit() else valor
            salvar_json(nome_arquivo, lista)
            print(f"{nome_modulo} atualizado com sucesso!")
            return
    print(f"{nome_modulo} não encontrado!")

def incluir(lista, chave, campos, nome_modulo, nome_arquivo, validar_duplicado=False):
    for i in range(3):
        codigo = int(input(f"digite o código do(a) {nome_modulo}: "))
        if validar_duplicado and any(item[chave] == codigo for item in lista):
            print("código já existente, tente novamente.")
            continue
        novo = {chave: codigo}
        for campo in campos:
            valor = input(f"digite o(a) {campo}: ")
            novo[campo] = int(valor) if valor.isdigit() else valor
        lista.append(novo)
        print(f"{nome_modulo} adicionado com sucesso!")
    salvar_json(nome_arquivo, lista)

def f_menu_principal():
    print("---- menu principal ----")
    print("(1) estudantes")
    print("(2) disciplinas")
    print("(3) professores")
    print("(4) turmas")
    print("(5) matrículas")
    print("(0) sair")
    return int(input("selecione a opção desejada: "))

def f_menu_secundario(modulo):
    print(f"---- menu de operações - {modulo} ----")
    print("(1) incluir")
    print("(2) listar")
    print("(3) atualizar")
    print("(4) excluir")
    print("(5) voltar ao menu principal")
    return int(input("selecione a opção desejada: "))

#Aqui vai ficar arquivos e listas
dados = {
    "estudantes": {
        "arquivo": "estudantes.json",
        "lista": carregar_json("estudantes.json"),
        "chave": "cod_est",
        "campos": ["nome", "cpf"]
    },
    "disciplinas": {
        "arquivo": "disciplinas.json",
        "lista": carregar_json("disciplinas.json"),
        "chave": "cod_disc",
        "campos": ["nome"]
    },
    "professores": {
        "arquivo": "professores.json",
        "lista": carregar_json("professores.json"),
        "chave": "cod_prof",
        "campos": ["nome", "cpf"]
    },
    "turmas": {
        "arquivo": "turmas.json",
        "lista": carregar_json("turmas.json"),
        "chave": "cod_turma",
        "campos": ["cod_prof", "cod_disc"],
        "validar_duplicado": True
    },
    "matriculas": {
        "arquivo": "matriculas.json",
        "lista": carregar_json("matriculas.json"),
        "chave": "cod_turma",
        "campos": ["cod_est"],
        "validar_duplicado": True
    }
}

while True:
    menu = f_menu_principal()
    if menu == 0:
        print("saindo...")
        break

    modulos = {
        1: "estudantes",
        2: "disciplinas",
        3: "professores",
        4: "turmas",
        5: "matriculas"
    }

    if menu in modulos:
        modulo = modulos[menu]
        info = dados[modulo]

        while True:
            menu_s = f_menu_secundario(modulo)
            if menu_s == 1:
                incluir(info["lista"], info["chave"], info["campos"], modulo, info["arquivo"], info.get("validar_duplicado", False))
            elif menu_s == 2:
                listar(info["lista"], modulo)
            elif menu_s == 3:
                editar(info["lista"], info["chave"], info["campos"], modulo, info["arquivo"])
            elif menu_s == 4:
                excluir(info["lista"], info["chave"], modulo, info["arquivo"])
            elif menu_s == 5:
                break
            else:
                print("opção inválida.")
    else:
        print("opção inválida.")

print("---Fim da Aplicação----")