from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    n = len(id_list)
    table = [[0]*n for _ in range(n)]

    cntdict = dict()
    for v in id_list:
        cntdict[v] = 0
    
    accuselist = [[] for _ in range(n)]

    for v in report:
        s = v.split()





    return answer






print(solution(["muzi", "frodo", "apeach", "neo"],	
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))