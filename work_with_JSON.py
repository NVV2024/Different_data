import json
from pprint import pprint


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    words_dict = []
    words_tupl = ()
    words_in_news = []
    #news_list = {}
    count = 0
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        #pprint(json_data.values())

    news_list = json_data['rss']['channel']['items']
    # print(type(news_list), len(news_list))
    # print(news_list)
    for i in range(len(news_list)):
        words_in_news = news_list[i]['description'].split()
        #print(len(words_in_news))
        #words_str = row['description'].split()
        #print(words_str, type(words_str)) 
        uniq_words = sorted(set(words_in_news))
        #print(len(uniq_words))
        pass
    print(len(uniq_words[0]))
    print(len(words_in_news[0]))

    # for w in uniq_words:
    #     #print(w)
    #     pass
    #     print(words_str)
    # print(len(words_str), type(words_str))

    return

read_json('newsafr.json')

# if __name__ == '__main__':
#     print(read_json('newsafr.json'))