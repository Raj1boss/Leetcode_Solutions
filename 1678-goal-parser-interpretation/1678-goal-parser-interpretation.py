class Solution:
    def interpret(self, command: str) -> str:
        new_str=''
        i=0
        while i<=len(command)-1:
            if "(" in command[i] and ")" in command[i+1]:
                new_str=new_str+'o'
                i=i+1
            else:
                new_str=new_str+command[i]
                new_str=new_str.replace('(',"").replace(')',"")
            i=i+1
        return new_str