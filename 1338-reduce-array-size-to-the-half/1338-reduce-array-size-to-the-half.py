class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict1={}
        for i in arr:
            if i in dict1:
                dict1[i]=dict1[i]+1
            else:
                dict1[i]=1

        new_1=[]
        for i,v in dict1.items():
            new_1.append(v)

        srt_1=sorted(new_1)
        
        
        size=len(arr)
        idmax=len(srt_1)-1
        count=0
        while size>len(arr)//2:
            size=size-srt_1[idmax]
            idmax-=1
            count+=1

        return count