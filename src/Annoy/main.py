from annoy import AnnoyIndex

from src.Queue.Queue import site
from src.Similarity.Cal_VECTOR import key2vector
import time
import jieba.analyse
import random
import queue as Q


f = 66  # 需要加载的向量的维度　　
t = AnnoyIndex(f)  # 初始化一个索引

# 全遍历
Dict = {}
with open('synonyms_vector.txt','r',encoding='gbk') as f:
    count = 0
    for line in f:
        result = line.split()
        count += 1
        word = result[0]
        Dict[count] = word
        vector = list(map(eval, result[1:]))  # 需要将txt中的str格式vec转化为float格式
        t.add_item(count, vector)
t.build(10)  # 建立基于二叉树的近似查找索引文件
t.save('test.ann')
# print(Dict)



