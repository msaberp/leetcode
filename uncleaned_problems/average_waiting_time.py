from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_sum = 0
        waiting_time = 0
        for customer in customers:
            if waiting_time == 0:
                waiting_time += customer[0]
            else:
                if waiting_time > customer[0]:
                    waiting_sum += waiting_time - customer[0]
                else:
                    waiting_time += customer[0] - waiting_time
            waiting_sum += customer[1]
            waiting_time += customer[1]

        return waiting_sum / len(customers)


if __name__ == '__main__':
    solution = Solution()
    customer_list = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
    result = solution.averageWaitingTime(customer_list)
    print(result)
