class Soulation():
    def fourSumCount(self,A,B,C,D):
        mapper = {}
        res = 0
        for i in A:
            for j in B:
                mapper[i + j] = mapper.get(i + j,0) + 1
        for i in C :
            for j in D:
                res += mapper.get(-1 * (i + j),0)
        return res

if __name__ == '__main__':
    s = Soulation()
    A = [1,2,3,4,5]
    B = [43,56,23,78,23]
    C = [32,46,23,-1,-33]
    D = [-11.-34,-13,-23,-130]
    f = s.fourSumCount
    print(f(A,B,C,D))