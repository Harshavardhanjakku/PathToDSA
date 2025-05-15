l=[]
class Solution:
    def func(self):
        l.append(1)
        self.func()
obj=Solution()
print(obj.func())