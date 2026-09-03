from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = max(count.values())
        max_tasks = sum(1 for value in count.values() if value == max_count)
        part = (max_count - 1) * (n + 1) + max_tasks

        return max(len(tasks), part)