class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        f={}
        for i in arr:
            if i in f:
                f[i]=f[i]+1
            else:
                f[i]=1
            
        d=[]
        for i,v in f.items():
            d.append(v)
            
        srt_1=sorted(d)
        
        size=len(arr)
        idmax=len(srt_1)-1
        count=0
        while size>len(arr)//2:
            size=size-srt_1[idmax]
            idmax=idmax-1
            count=count+1
        return count
            
        
                
        
       