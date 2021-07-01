def exists_word(word, instance):
    """Aqui irá sua implementação"""
    list_return = list()
    for file_obj in instance.get_queue():
        d = {
            "palavra": word,
            "arquivo": file_obj["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index, line in enumerate(file_obj["linhas_do_arquivo"]):
            number_line = index + 1
            word_lower = word.lower()
            line_lower = line.lower()
            if word_lower in line_lower:
                d["ocorrencias"].append({"linha": number_line})
        if d["ocorrencias"]:
            list_return.append(d)
    return list_return


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
