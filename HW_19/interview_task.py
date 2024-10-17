
def max_depth(heights):
    n = len(heights)

    if n < 3:
        return 0

    max_depth = 0

    for i in range(1, n-1):                                           # написав за 30 хвилин та думав як це вирішити
        left_max = max(heights[:i])
        right_max = max(heights[i+1:])
        water_level = min(left_max, right_max)

        if water_level > heights[i]:
            depth = water_level - heights[i]
            max_depth = max(depth, max_depth)

    return max_depth

heights = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
print(max_depth(heights))                                            # додумав і дописав до кінця приблизно за 55 звилин

