def exists_word(word, instance):
    result = list()

    for i in range(len(instance)):
        file = instance.search(i)
        file_name = file["nome_do_arquivo"]

        info = {
            'palavra': word,
            'arquivo': file_name,
            'ocorrencias': list()
        }
        for line in file['linhas_do_arquivo']:
            if word.lower() in line.lower():
                info['ocorrencias'].append({
                    'linha': file['linhas_do_arquivo'].index(line) + 1
                })
        if info["ocorrencias"]:
            result.append(info)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
