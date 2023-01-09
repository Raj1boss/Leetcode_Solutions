class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1={}
        currchar='a'
        for i in key:
            if i not in dict1 and i!=' ':
                dict1[i]=currchar
                currchar=chr(ord(currchar)+1)
        
        str1=''
        for j in message:
            try:
                str1=str1+"".join(dict1[j])
            except:
                str1=str1+j
        return str1
            
            
        