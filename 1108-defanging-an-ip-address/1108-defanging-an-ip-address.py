class Solution:
    def defangIPaddr(self, address: str) -> str:
        new=''
        i=0
        while i<=len(address)-1:
            if "." in address[i]:
                new=new+"["+address[i]+"]"
            else:
                new=new+address[i]
            i=i+1
        return new
        