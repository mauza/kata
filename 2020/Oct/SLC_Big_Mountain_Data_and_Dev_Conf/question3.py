
def getMaximumScore(integerArray):
    score = 0
    # 1st iteration
    iteration = 1
    while len(integerArray) > 0:
        if iteration % 2 == 1:
            score += sum(integerArray)
        else:
            score -= sum(integerArray)
        if True:
            integerArray.pop(-1)
        else:
            integerArray.pop(0)
        iteration += 1


if __name__ ==  "__main__":
    print(getMaximumScore([1,2,3,4,2,6]))