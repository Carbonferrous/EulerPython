count = 1
for hun in range(0, 3):
    left = 200 - 100 * hun
    for fif in range(0, left//50 + 2):
        left -= 50 * fif
        for twen in range(0, left//20 + 2):
            left -= 20 * twen
            for ten in range(0, left//10 + 2):
                left -= 10 * ten
                for five in range(0, left//5 + 2):
                    left -= 5 * five
                    for two in range(0, left//2 + 2):
                        left -= 2 * two
                        if left >= 0:
                            count += 1
                            #print(hun, fif, twen, ten, five, two, left)
                        left += 2 * two
                    left += 5 * five
                left += 10 * ten
            left += 20 * twen
        left += 50 * fif
    left += 100 * hun
print(count)
