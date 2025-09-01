import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        # 1. Approach Explanation:
        # The key insight is that we want to maximize the *average* pass ratio. This means we should assign extra students to classes where they'll make the biggest impact on the pass ratio.  The impact is the difference between the new pass ratio and the old pass ratio if we add a student to that class.
        # We use a max-heap (priority queue) to keep track of the classes that benefit the most from an extra student.  The heap is ordered by the *negative* of the change in pass ratio, because Python's heapq is a min-heap.
        # We iterate `extraStudents` times:
        #   - Pop the class with the biggest potential impact from the heap.
        #   - Add a student to that class.
        #   - Recompute the impact and push the updated class back onto the heap.
        # Finally, we calculate the average pass ratio.

        # 2. Code Solution:
        pq = []
        for passed, total in classes:
            # Calculate the change in pass ratio if we add a student.
            delta = float(passed + 1) / (total + 1) - float(passed) / total
            # Push the negative of the delta, along with the passed and total values, onto the heap.
            heapq.heappush(pq, (-delta, passed, total))

        for _ in range(extraStudents):
            # Pop the class with the highest potential impact.
            neg_delta, passed, total = heapq.heappop(pq)
            # Add a student to that class.
            passed += 1
            total += 1
            # Recompute the impact.
            delta = float(passed + 1) / (total + 1) - float(passed) / total
            # Push the updated class back onto the heap.
            heapq.heappush(pq, (-delta, passed, total))

        # Calculate the average pass ratio.
        total_ratio = 0
        for neg_delta, passed, total in pq:
            total_ratio += float(passed) / total

        return total_ratio / len(classes)

        # 3. Time and Space Complexity:
        # - Time Complexity: O(N + K * log N), where N is the number of classes and K is the number of extra students.
        #   - O(N) to initialize the heap.
        #   - O(K * log N) to perform K heap operations (pop and push).
        # - Space Complexity: O(N) to store the heap.

        # 4. Constraints and Edge Cases:
        # - `1 <= classes.length <= 105`: The solution iterates through the classes once, which handles the upper bound on the number of classes.
        # - `classes[i].length == 2`: The code expects a 2D array, validated through the use of passed, total.
        # - `1 <= passi <= totali <= 105`: Ensures no division by zero and valid inputs.
        # - `1 <= extraStudents <= 105`: Handled by the loop that executes extraStudents times.
        # - Edge case: If classes is empty, then it will give a division by zero error. Can be fixed by checking `if not classes: return 0` at start of the function

        # 5. Key Parts Explanation:
        # - `heapq`: Used for implementing the priority queue.
        # - `delta = float(passed + 1) / (total + 1) - float(passed) / total`: Calculates the change in pass ratio.
        # - `heapq.heappush(pq, (-delta, passed, total))`: Pushes the negative of the delta onto the heap to simulate a max-heap.

        # 6. Optimizations:
        # - Using a heap efficiently finds the class with the biggest impact.
        # - Calculating the change in pass ratio incrementally avoids redundant calculations.
