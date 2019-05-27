from annoy import AnnoyIndex
from copy import deepcopy
from src.Queue.Queue import site
from src.Similarity.Cal_VECTOR import key2vector
import jieba.analyse
import queue as Q

topK = 3


class search:
    def __init__(self):
        # 全遍历
        self.Dict = {1: '中心城北', 2: '中心城东', 3: '沙湾', 4: '横岗信义', 5: '横岗振业城', 6: '坂田佳兆业', 7: '坂田星河雅宝', 8: '中信龙盛', 9: '平湖', 10: '龙东', 11: '龙岗满京华', 12: '坂田六号路', 13: '坪地启创/慢充', 14: '布吉街道办', 15: '布吉文博宫', 16: '坪地汽车站', 17: '石岩丽枫', 18: '龙城大运', 19: '龙西', 20: '横岗安良', 21: '石岩文体中心', 22: '大鹏欢乐海湾', 23: '大鹏七星湾', 24: '白石汽车总站', 25: '爵悦公馆', 26: '布吉街道办站/慢充', 27: '金地龙城中央', 28: '坪地启创', 29: '沙湾大巴站', 30: '惠州市大亚湾霞涌', 31: '沙湾直流快充站', 32: '六号路直流快充站', 33: '坪地汽车站大巴桩', 34: '惠州南站', 35: '龙岗区宝昌利'}
        self.u = AnnoyIndex(topK * 22)
        self.u.load('test.ann')

    def run(self, key):
        temp = key.replace("充电", "")
        temp = temp.replace("站", "")
        # words = list(jieba.cut(temp))
        words = list(jieba.analyse.extract_tags(temp, 3))
        if len(words) > topK:
            words = words[0:topK]
        print(words)
        result = Q.PriorityQueue()

        # ---------------------------------------------- #
        def permutations(arr, position, end, res):
            if position == end:
                stri = ""
                for item in arr:
                    stri += str(item)
                vect = key2vector(stri)
                simi_id = self.u.get_nns_by_vector(vect, 4, include_distances=True)
                ids = simi_id[0]
                score = simi_id[1]
                for i, j in zip(ids, score):
                    result.put(site(self.Dict[i], 0.5 * (abs(1 - j)) + 0.5))
            else:
                for index in range(position, end):
                    arr[index], arr[position] = arr[position], arr[index]
                    permutations(arr, position + 1, end, res)
                    arr[index], arr[position] = arr[position], arr[index]

        # ---------------------------------------------- #
        permutations(words, 0, len(words), result)
        cnt = 0
        res = []
        while not result.empty():
            # name_set.add(result.get().get_site_name())
            temp = result.get().get_site_name()
            res.append(temp)
            cnt += 1
            if cnt == topK + 1:
                break

        l2 = sorted(set(res), key=res.index)
        return l2

# how to use
sc = search()
key1 = "中心城东坪地充电站"
key2 = "深圳文体中心充电站"
key3 = "沙湾充电站"
key4 = "坂田佳照业充电站"
key5 = "食盐文体中心充电站"
key6 = "石岩重心充电站"
key7 = "沙弯充电站"
print(sc.run(key1))
print(sc.run(key2))
print(sc.run(key3))
print(sc.run(key4))
print(sc.run(key5))
print(sc.run(key6))
print(sc.run(key7))
