class Solution:
    def fractionToDecimal(self,numerator,denominatior):
        n, remainder = divmod(abs(numerator),abs(denominatior)) #divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
        sign =''
        if(numerator // denominatior < 0):
            sign ='-'
        res = [str(n),'.']
        seen = []
        while(remainder not in seen):
            seen.append(remainder)
            n, remainder = divmod((remainder * 10),abs(denominatior))
            res.append(str(n))
        index = seen.index(remainder)
        res.insert(index + 2,'(') #第二个元素插入(
        res.append(')')
        return sign + "".join(res).replace('(0)','').rstrip('.') # 字符串拼接 Python rstrip() 删除 string 字符串末尾的指定字符，默认为空白符 

if __name__ == '__main__':
    s = Solution()
    l = s.fractionToDecimal
    numerator =2
    denominatior =3
    print(l(numerator,denominatior))
