# -*- coding: utf-8 -*-
#project:LeetCode191
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: 273.整数转换英文表示.py
#time: 2019/9/15 12:02
class Solution:
    words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety","Hundred"]
    def numberToWords(self, num):
        if num == 0:
            return self.words[0]
        index = 1
        result = ""
        flag = 1
        while num>0:
            last = num % 1000
            if last == 0:
                flag = 0
            else:
                flag = 1
            if flag:
                if index == 2:
                    result = "Thousand " + result
                elif index == 3:
                    result = "Million " + result
                elif index == 4:
                    result = "Billion " + result
            if last < 100:
                result = self.two(last) + result
            else:
                result = self.three(last) + result
            index += 1
            num = num//1000
        return result[:len(result)-1]

    def two(self,num):
        if num == 0:
            return ''
        if num<20:
            return self.words[num] + " "
        else:
            return self.words[num//10+18] + ' '+ self.two(num%10)

    def three(self,num):
        return self.words[num//100] +" "+ "Hundred " + self.two(num%100)




if __name__ == '__main__':
    s = Solution()
    num = 200000
    print(s.numberToWords(num))