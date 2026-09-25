class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        n=len(start)
        
        room=0
        max_rooms=0
        i,j=0,0
        
        while i<n:
            if start[i]<end[j]:
                room+=1
                max_rooms=max(max_rooms,room)
                i+=1
            else:
                room-=1
                j+=1
        return max_rooms
