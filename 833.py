class Solution:
    def findReplaceString(self, S, indexes,sources, targets):
        result = ''
        if len(indexes) == 0:
            return S
        data = {}
        for index in range(0,len(indexes)):
            data[index] = indexes[index]
        data = sorted(data.items(),key=lambda item:item[1],reverse= True)
        print(data)
        for item in data:
            if S[item[1]:item[1]+ len(sources[item[0]])] == sources[item[0]]:
                S = S[:item[1]] + targets[item[0]] + S[item[1]+len(sources[item[0]]):]
        return S

if __name__ == '__main__':
    s = Solution()
    S = "vmokgggqzp"
    indexes = [3,5,1]
    sources = ["kg","ggq","mo"]
    targets = ["s","so","bfr"]
    print(s.findReplaceString(S,indexes,sources,targets))

