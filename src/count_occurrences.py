import requests

def count_word_occurrences(url, word_to_count):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        # Conte as ocorrências da palavra desejada
        count_word = content.lower().count(word_to_count)

        print(f'A palavra "{word_to_count}" apareceu {count_word} vezes na página.')
        return count_word
    else:
        print(f'Erro ao acessar a página: {response.status_code}')
        return None

# EXEMPLOS DE USO

# Substitua a palavra e a URL que deseja verificar. Neste exemplo é o comando if
word_to_count = 'if'
url = 'https://github.com/nathanborror/django-basic-apps/blob/master/basic/blog/models.py'
count_result = count_word_occurrences(url, word_to_count)

# função def
word_to_count = 'def'
url = 'https://github.com/nathanborror/django-basic-apps/blob/master/basic/blog/models.py'
count_result = count_word_occurrences(url, word_to_count)

# class
word_to_count = 'class'
url = 'https://github.com/nathanborror/django-basic-apps/blob/master/basic/blog/models.py'
count_result = count_word_occurrences(url, word_to_count)