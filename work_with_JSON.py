# Версия от 18:00 - 17.06.2024

import json
from pprint import pprint


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм

    words_in_news = []
    # news_list = {}
    count = 0
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        # pprint(json_data.values())
    news_list = json_data['rss']['channel']['items']

    for i in range(len(news_list)):
        words_in_news.append(news_list[i]['description'].split())
        # print(type(words_in_news))
        # print(len(words_in_news))
    # print(len(words_in_news))

    # Формируем список слов и словарь уникального списка слов
    words_ = []
    dict_words = {}
    j = 0
    while j < len(words_in_news):
        # print(words_in_news[j])
        for k in words_in_news[j]:
            # print(len(k))
            # Слова, где больше 6 символов. Проверка условия word_max_len=6
            if len(k) >= word_max_len:
                # print(k)
                words_.append(k)
        j += 1
    # print(words_)
    # print(len(words_))
    uniq_words = sorted(set(words_))
    # print(uniq_words)
    # print(type(uniq_words), len(uniq_words))

    for z, n in enumerate(uniq_words):
    # print(z, n)
        #print(z, n, words_.count(n))
        dict_words[n] = words_.count(n)

    {k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1])}
    print(dict_words)


    # Формируем пустой словарь уникальных слов
    # for uniq_words in words_:
    #     dict_words.setdefault(uniq_words, 1)
    # print(dict_words)
    #print(words_.count("ноября"))
    # Считаем кол-во уникальных слов в новостях

    return


read_json('newsafr.json')

# if __name__ == '__main__':
#     print(read_json('newsafr.json'))
