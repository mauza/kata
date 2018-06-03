count = 1

for b in range (101):
    for c in range(41):
        for d in range(21):
            for e in range(11):
                for f in range(5):
                    for g in range(3):
                        if (b*2 + c*5 + d*10 + e*20 + f*50 + g*100) <= 200:
                            count += 1
print(count)