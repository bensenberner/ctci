from collections import defaultdict
## BEELLMMNaNAN
def findFlights(cities, source, max_num_stops):
    d = {city: float('inf') for city in cities.keys()}
    queue = [(source, 0, 0)]
    while queue:
        curr, flight_time, num_stops = queue.pop(0)
        if num_stops > max_num_stops:
            continue
        d[curr] = min(d[curr], flight_time) if curr in d else flight_time
        if curr not in cities: continue
        for new_city in cities[curr]:
            queue.append((new_city, flight_time + cities[curr][new_city], num_stops + 1))
    return d

t = {
        "NY": { "SF": 69, "LA": 4},
        "LA": { "NY": 72, "SEA": 22, "SF": 42}
    }

print(findFlights(t, "NY", 2))
