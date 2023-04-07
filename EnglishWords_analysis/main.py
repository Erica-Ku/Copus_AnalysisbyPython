# 필요한 패키지 import하기
from operator import itemgetter
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 단어와 빈도수 데이터가 담긴 파일 한 개를 불러온 후 (단어,빈도수) 꼴의 튜플로
# 구성된 리스트를 반환하는 함수 - 파일을 읽어 리스트로 변환함
def import_corpus(filename):
    corpus = []
    with open(filename) as file:
        for line in file:
            word, num = line.split(',')
            num = int(num.replace('\n', ''))
            corpus.append((word, num))
    return corpus


# print(import_corpus("corpus.txt"))

# (단어, 빈도수) 꼴의 튜플들을 담고 있는 리스트의 형태로 주어지는 코퍼스의 데이터 중 특정 접두사로 시작하는
# 단어 데이터만 뽑은 리스트를 반환하는 함수
def filter_by_prefix(corpus, prefix):
    tmp = list(filter(lambda word: word[0].startswith(prefix), corpus))
    return tmp


# result1 = import_corpus("corpus.txt")


# print(filter_by_prefix(result1, "qu"))

# 코퍼스의 데이터 중 가장 빈도가 높은 number개의 데이터만 반환하는 함수
def most_frequent_words(corpus, number):
    tmp = sorted(corpus, key=lambda fre: fre[1], reverse=True)[:number]
    return tmp


# print(most_frequent_words(result1, 5))

# 단어별 사용 빈도를 보여주는 막대 그래프를 작성하는 함수
def draw_frequency_graph(corpus):
    pos = range(len(corpus))
    words = [tup[0] for tup in corpus]
    freqs = [tup[1] for tup in corpus]
    font = fm.FontProperties(fname="./NanumBarunGothic.ttf")
    plt.bar(pos, freqs, align="center")
    plt.xticks(pos, words, rotation="vertical", fontproperties=font)
    plt.title("단어별 사용 빈도", fontproperties=font)
    plt.ylabel("빈도", fontproperties=font)
    plt.tight_layout()
    plt.savefig("graph.png")


# result2 = most_frequent_words(result1, 5)
# draw_frequency_graph(result2)

def main(prefix=""):
    corpus = import_corpus("corpus.txt")
    prefix_words = filter_by_prefix(corpus, prefix)
    top_ten = most_frequent_words(prefix_words, 10)
    draw_frequency_graph(top_ten)


if __name__ == '__main__':
    main(prefix="head")