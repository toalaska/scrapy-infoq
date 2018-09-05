# coding=utf-8
import pymongo
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

mongo_uri = "127.0.0.1"
mongo_db = "infoq"
collection_name = "presentation"
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]
tab = db[collection_name]

import os, codecs
import jieba
from collections import Counter
from pyecharts import WordCloud


def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    name = []
    value = []
    for (k, v) in c.most_common(100):
        # print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))
        print k, v
        name.append(k.split(".")[0])
        value.append(v)

    draw(name, value)


def draw(name, value):
    wordcloud = WordCloud(title="infoq热词", width=800, height=600)
    # 'circle', 'cardioid', 'diamond', 'triangle-forward',            'triangle', 'pentagon', 'star'
    wordcloud.add("", name, value, word_size_range=[20, 100],shape="triangle-forward")
    wordcloud.render("words.html")


if __name__ == '__main__':

    titles = []
    urls=[]
    for x in tab.find():
        titles.append(x['title'])
        urls.append('<p><a target="_blank" href="http://www.infoq.com%s">%s</a></p>' % (x['url'],x['title']))

    txt = ",".join(titles)
    get_words(txt)

    with open("index.html","w") as f:
        f.write("\n".join(urls))
