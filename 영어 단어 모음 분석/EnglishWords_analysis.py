# 필요한 패키지 import하기
from operator import itemgetter
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 단어와 빈도수 데이터가 담긴 파일 한 개를 불러온 후, (단어,빈도수) 꼴의 튜플로
# 구성된 리스트를 반환하는 함수 - 코퍼스 파일을 읽어 리스트로 변환함
def import_corpus(filename):
    corpus = []
    with open(filename) as file:
        for line in file:
            word, num = line.split(',')
            num = int(num.replace('\n',''))
            corpus.append((word, num))
    return corpus

print(import_corpus("D:\구민지\Copus_AnalysisbyPython\영어 단어 모음 분석\corpus.txt"))
