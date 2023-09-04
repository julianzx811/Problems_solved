def minimumBribes2(q):
    movements = 0
    for indexx, value in enumerate(q[::-1]):
        index = len(q) - 1 - indexx
        if q[index] != index + 1:
            if q[index - 1] == index + 1:
                q[index - 1], q[index] = q[index], q[index - 1]
                movements += 1
            elif q[index - 2] == index + 1:
                q[index], q[index - 1], q[index - 2] = (
                    q[index - 2],
                    q[index],
                    q[index - 1],
                )
                movements += 2
            else:
                print("Too chaotic")
                return
    print(movements)


arr = [2, 1, 5, 3, 4]
arr2 = [2, 5, 1, 3, 4]
arr3 = [5, 1, 2, 3, 7, 8, 6, 4]
arr4 = [1, 2, 5, 3, 7, 8, 6, 4]
print(minimumBribes2(arr4))
# print(minimumBribes(arr2))
