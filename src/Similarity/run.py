from src.soundshapecode import ssc
from src.soundshapecode.ssc import getHanziStrokesDict, getHanziStructureDict, getHanziSSCDict
from src.soundshapecode.variant_kmp import VatiantKMP
from src.soundshapecode.ssc_similarity.compute_ssc_similarity import computeSSCSimilaruty
import jieba.analyse
SIMILARITY_THRESHOLD = 0.8
topK = 10
SSC_ENCODE_WAY = 'ALL'  # 'ALL','SOUND','SHAPE'
# SSC_ENCODE_WAY = 'SOUND'  # 'ALL','SOUND','SHAPE'

# 计算单字相似度
def Similarity_between_word(str1, str2):
    getHanziStrokesDict()
    getHanziStructureDict()
    # generateHanziSSCFile()#生成汉子-ssc映射文件
    getHanziSSCDict()
    chi_word1_ssc = ssc.getSSC(str1, SSC_ENCODE_WAY)
    print(chi_word1_ssc)
    chi_word2_ssc = ssc.getSSC(str2, SSC_ENCODE_WAY)
    print(chi_word2_ssc)
    return computeSSCSimilaruty(chi_word1_ssc[0],chi_word2_ssc[0],SSC_ENCODE_WAY)

# 计算词语相似度
def Similarity_between_word2(str1, str2):
    getHanziStrokesDict()
    getHanziStructureDict()
    # generateHanziSSCFile()#生成汉子-ssc映射文件
    getHanziSSCDict()
    text1 = jieba.analyse.extract_tags(str1, topK)
    text2 = jieba.analyse.extract_tags(str2, topK)

    chi_word1_ssc = []
    for text in text1:
        chi_word1_ssc.append(ssc.getSSC(text, SSC_ENCODE_WAY))
    print(chi_word1_ssc)
    chi_word2_ssc = []
    for text in text2:
        chi_word2_ssc.append(ssc.getSSC(text, SSC_ENCODE_WAY))
    print(chi_word2_ssc)
    '''
    res = []

    importance = 1.0
    for i in range(len(chi_word1_ssc)):
        sum = 0.0
        importance = 1.0
        for i in range(min(len(text), len(sample))):
            sum += importance * string_similar(text[i], sample[i])
            importance /= 2.0
        res.append(sum)
    print(res)
    re1 = map(res.index, heapq.nlargest(topK, res))
    print(list(re1))
    '''
str1 = "狼人"
str2 = "浪人"
print(Similarity_between_word2(str1,str2))
