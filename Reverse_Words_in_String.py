class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        res= ""
        for i in range(len(t)-1,-1,-1):
            if t[i]:
                print(t[i])
                res=res+t[i] +" "
               
        return res[0:-1]
        