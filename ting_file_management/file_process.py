import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)
    if lines:
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        for o in instance.get_queue():
            if o["nome_do_arquivo"] == path_file:
                return None
        instance.enqueue(file)
        sys.stdout.write(str(file))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
