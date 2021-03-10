import math

mdy = [int(i) for i in input().split('-')]

jan_or_feb = mdy[0] == 1 or mdy[0] == 2

k = mdy[1]
m = mdy[0] + 10 if jan_or_feb else mdy[0] - 2
C = mdy[2] // 100
Y = mdy[2] % 100 - 1 if jan_or_feb else mdy[2] % 100
W = (k + math.floor(2.6 * m - 0.2) - 2 * C + Y + math.floor(Y / 4) + math.floor(C / 4)) % 7

print({ 0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"}.get(W))