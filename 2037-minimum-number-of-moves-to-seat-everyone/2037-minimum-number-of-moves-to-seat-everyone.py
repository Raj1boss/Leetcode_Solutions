class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        for i,j in zip(sorted(seats),sorted(students)):
            return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))
            
        