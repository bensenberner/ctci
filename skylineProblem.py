def getSkyline(raw_buildings):
    buildings = sorted({(x, y, z) for x, y, z in raw_buildings})
    res = set()
    for idx, (l, r, h) in enumerate(buildings):
        left_corner_above_all = True
        # loop through all buildings and confirm the left corner is above all
        # exit if you go past the current idx OR if you find a taller building
        for idx2, (l2, r2, h2) in enumerate(buildings):
            if idx == idx2: continue
            if l2 > l: break
            if l2 <= l <= r2 and h2 >= h:
                left_corner_above_all = False
                break

        if left_corner_above_all:
            res.add((l, h))

        # loop through all buildings and confirm the right edge is NOT within any.
        # exit once the left corner is past the current right corner
        right_corner_stands_alone = True
        right_corner_height = 0
        for idx3, (l3, r3, h3) in enumerate(buildings):
            if idx == idx3: continue
            if l3 > r: break
            if r < r3:
                if h3 < h:
                    right_corner_height = max(right_corner_height, h3)
                else:
                    right_corner_stands_alone = False
                    break
        if right_corner_stands_alone:
            res.add((r, right_corner_height))
    return sorted(res)

print(getSkyline(skl))