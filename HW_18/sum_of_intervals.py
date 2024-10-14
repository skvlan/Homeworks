# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    sum=0
    intervals=sorted(intervals)
    a=intervals[0][0]
    b=intervals[0][1]
    sum += b - a
    if len(set(intervals)) == 1:
        return sum
    else:
        for i in intervals[1:]:
            if i[0] > b:
                sum += i[1] - i[0]
                a = i[0]
                b = i[1]
            elif i[0] >= a and i[1] <= b:
                continue
            else:
                sum += i[1] - b
                b=i[1]
    return sum