import collections
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:

    deque = collections.deque()
    cost = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        c = city.lower()
        if c in deque:
            cost +=1
            deque.remove(c)
            deque.append(c)
        else:
            cost += 5
            if len(deque) < cacheSize:
                deque.append(c)
            else:
                deque.popleft()
                deque.append(c)

    return cost

size = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju","Pangyo", "Seoul"]
cities3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco","Seoul","Rome","Paris","jeju","NewYork","Rome"]
cities4 = ["Jeju", "Pangyo", "NewYork", "newyork"]
cities5 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print (solution (size, cities))

