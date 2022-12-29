class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data=[]
        for i in range(len(names)):
            max_1=max(heights)
            index_v=heights.index(max_1)
            heights.pop(index_v)
            data.append(names[index_v])
            names.pop(index_v)
        return data
        