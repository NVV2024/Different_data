#Начало 25.06.2024 19:06
#Версия 26062024 13:13 - Финальная

import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм

    # создаем парсер XML. парсеру обязательно задаем кодировку
    parser = ET.XMLParser(encoding="utf-8")
    # превращаем исходный текстовый файл sample.xml в дерево XML
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()

    words_in_news = []
    news_list = []

    #Формируем списки новостей
    all_news_list = root.findall("channel/item")
    for news in all_news_list:
        #print(type(news.find('description').text))
        words_in_news.append(news.find('description').text.split())

    # Формируем список общего количества слов
    words_ = []
    i = 0
    j = 0

    while j < len(words_in_news):
        for k in words_in_news[j]:
            # Слова, где больше 6 символов. Проверка условия word_max_len=6
            if len(k) > word_max_len:
                words_.append(k)
        j += 1

    # Формируем список уникальных слов
    uniq_words = sorted(list(set(words_)), reverse=True)

    # Формируем словарь слов и их количество
    dict_words = {}
    for z, n in enumerate(uniq_words):
        dict_words[n] = words_.count(n)

    # Делаем сортировку списка слов по кол-ву упоменаний
    sorted_list = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    dict_sorted = dict(sorted_list)
    final_list = list(dict_sorted.keys())[:top_words_amt]

    return final_list

#read_xml('newsafr.xml')

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))