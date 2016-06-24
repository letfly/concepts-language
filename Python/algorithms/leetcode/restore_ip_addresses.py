class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []

        s_len = len(s)

        for i in [1,2,3]:
            for j in [i+1,i+2,i+3]:
                for k in [j+1,j+2,j+3]:
                    if k >= s_len:
                        continue
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if self.check_valid([s1,s2,s3,s4]):
                        new_string = s1 + "." + s2 + "." + s3 + "." + s4
                        answer.append(new_string)
                    print answer

        return answer

    def check_valid(self,str_list):
        for s in str_list:
            if s[0] == "0" and s != "0":
                return False
            if int(s) > 255:
                return False

        return True

s = Solution()
print s.restoreIpAddresses("25525511135")
