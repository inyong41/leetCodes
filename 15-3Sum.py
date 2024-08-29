class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = list()
        p = list()
        z = 0
        for num in nums:
            if num < 0:
                if n.count(num) < 2:
                    n.append(num)
            elif num > 0:
                if p.count(num) < 2:
                    p.append(num)
            else:
                z = z + 1
        N = set(n)
        P = set(p)
        if z > 0:
            for num in N:
                if -num in P:
                    res.add((num, 0, -num))
            if z > 2:
                res.add((0, 0, 0))
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                s = -(n[i] + n[j])
                if s in P:
                    res.add(tuple(sorted([n[i], s, n[j]])))
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                s = -(p[i] + p[j])
                if s in N:
                    res.add(tuple(sorted([p[i], s, p[j]])))
        return [list(r) for r in res]