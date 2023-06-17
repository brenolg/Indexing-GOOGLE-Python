from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(dict)

    print(dict)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        deleted_file = instance.dequeue()
        print(
            f'Arquivo {deleted_file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        searched_file = instance.search(position)
        print(searched_file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
