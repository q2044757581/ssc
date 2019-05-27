from src.soundshapecode import ssc
from src.soundshapecode.ssc import getHanziStrokesDict, getHanziStructureDict, getHanziSSCDict
from src.soundshapecode.variant_kmp import VatiantKMP
from src.soundshapecode.ssc_similarity.compute_ssc_similarity import computeSSCSimilaruty
import jieba.analyse
SSC_ENCODE_WAY = 'ALL'  # 'ALL','SOUND','SHAPE'
# SSC_ENCODE_WAY = 'SOUND'  # 'ALL','SOUND','SHAPE'
topK = 3


def decode(str1):
    getHanziStrokesDict()
    getHanziStructureDict()
    # generateHanziSSCFile()#生成汉子-ssc映射文件
    getHanziSSCDict()
    # text = jieba.analyse.extract_tags(str1,topK)
    # if len(text) < topK:
    text = jieba.cut(str1)
    text = list(text)[0:topK]
    # text = jieba.analyse.extract_tags(str1, topK)
    res = []
    for t in text:
        res += ssc.getSSC(t, SSC_ENCODE_WAY)
    return res


def key2vector(key):
    vector = []
    res = decode(key)

    for rs in res:
        for r in rs:
            if '9' >= r >= '0':
                vector.append(int(r))
            else:
                vector.append(int(ord(r)))
    global topK
    '''
    if len(vector) >= topK * 22:
        vector = vector[0:topK * 22]
    else:
        length = len(vector)
        # print("before ", len(vector))
        # print(int(topK*22/length)-1)
        for i in range(int(topK*22/length)-1):
            vector += vector[0:length]
            # vector = vector[0:] + [0 for i in range(topK * 22 - len(vector))]
        vector += vector[:topK*22 - len(vector)]
    '''
    sum = 0
    for i in vector:
        sum += i
    avg = int(sum / len(vector))
    if len(vector) >= topK * 22:
        vector = vector[0:topK * 22]
    else:
        vector = vector + [avg for i in range(topK * 22 - len(vector))]

    # print(int(topK*22/length))
    # print("after ", len(vector))
    # print(len(vector))
    return vector


def decode2vector():
    case = []
    file = open("../Similarity/stations.txt", "r", encoding="gbk")
    for line in file:
        temp = line.replace("充电站", "")
        # print(temp)
        case.append(temp)
    f = open('../Annoy/synonyms_vector.txt', 'w')
    for cs in case:
        stri = ""
        stri += str(cs)
        stri = stri.strip('\n')
        vector = key2vector(str(cs))
        for v in vector:
            stri += " " + str(v)
        f.write(stri + "\n")

    f.close()

# decode2vector()







