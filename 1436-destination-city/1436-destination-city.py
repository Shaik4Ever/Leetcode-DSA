class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        d={}
        for i in paths:
            d[i[0]]=i[1]
        for i in d.values():
            if i not in d:
                return i
