from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_height_dict = {k: v for k, v in zip(heights, names)}
        sorted_people = [people_height_dict[k] for k in sorted(people_height_dict, reverse=True)]
        return sorted_people


if __name__ == '__main__':
    s = Solution()
    names_ = ["Mary", "John", "Emma"]
    heights_ = [180, 165, 170]
    print(s.sortPeople(names_, heights_))
