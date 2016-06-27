class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:         print 'left',left,right,p;generate(p + '(', left-1, right)
            if right > left: print 'right',left,right,p;generate(p + ')', left, right-1)
            if not right:    print 'not',left,right,p,parens;parens += p,
            return parens
        return generate('', n, n)

s = Solution()
print s.generateParenthesis(3)
