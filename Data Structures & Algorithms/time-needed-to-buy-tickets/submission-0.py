from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)
        time = 0

        while queue:
            curr = queue.popleft()
            tickets[curr] -= 1
            time += 1
            if tickets[curr] == 0:
                if curr == k:
                    return time
            else:
                queue.append(curr)
        return time
