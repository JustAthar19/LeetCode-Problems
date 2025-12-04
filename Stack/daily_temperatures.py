
temperatures = [73,74,75,71,69,72,76,73]

# Brute Force
def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = []
    for i in range(n):
        count = 1
        j = i + 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                break
            count += 1
            j += 1
        count = 0 if j == n else count
        res.append(count)
    return res