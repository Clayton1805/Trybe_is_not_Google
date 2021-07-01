import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return None

    try:
        with open(path_file) as file:
            return [o.split("\n")[0] for o in file.readlines()]
    except FileNotFoundError:
        sys.stderr.write(
            "Arquivo statics/arquivo_nao_existe.txt não encontrado\n"
        )
        return None
