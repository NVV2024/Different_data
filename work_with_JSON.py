# Версия от 18:00 - 17.06.2024

import json
from pprint import pprint


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм

    words_in_news = []
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    news_list = json_data['rss']['channel']['items']

    # for i in range(len(news_list)):
    #     words_in_news.append(news_list[i]['description'].split())

    # Формируем список общего количества слов
    words_ = []
    dict_words = {}
    j = 0
    while j < len(words_in_news):
        words_in_news.append(news_list[j]['description'].split())
        for k in words_in_news[j]:
            # Слова, где больше 6 символов. Проверка условия word_max_len=6
            if len(k) > word_max_len:
                words_.append(k)
        j += 1

    #Формируем список уникальных слов
    uniq_words = sorted(list(set(words_)), reverse=True)
    #uniq_words.sort(reverse=True)

    #Формируем словарь слов и их количество
    for z, n in enumerate(uniq_words):
        dict_words[n] = words_.count(n)

    #Делаем сортировку списка слов по кол-ву упоменаний
    sorted_list = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    dict_sorted = dict(sorted_list)
    final_list = list(dict_sorted.keys())[:top_words_amt]
    #print(list(dict_sorted.keys())[:top_words_amt])

    return final_list

#read_json('newsafr.json')

if __name__ == '__main__':
    print(read_json('newsafr.json'))