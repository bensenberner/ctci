# given a list of appointment requests, maximize the number of minutes booked
def maxMassageMins(durations):
    using = notusing = 0
    for duration in durations:
        using, notusing = notusing + duration, max(using, notusing)
    return max(using, notusing)

def recursive(durations):
    if not durations: return 0
    return max(durations[0] + recursive(durations[2:]), recursive(durations[1:]))

arr = [30,15,60,75,45,15,15,45]
print(recursive(arr))
