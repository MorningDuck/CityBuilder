#numbers

import random


count = 0

a = b = c = d = total = 0

maxi = 0

out = "==================\n\nBusinessmen: %d(%0.2f)\nCreators:    %d(%0.2f)\nArtists:     %d(%0.2f)\nConsumers:   %d(%0.2f)\n\n==================="

while count < 10000:
    while(1):
        ethic = random.randint(0,1)
        creat = random.randint(0,1)
        if ethic == 1:
            if creat == 0:
                if a <= maxi:
                    a += 1
                    break
                if a > maxi:
                    maxi = a
            elif creat == 1:
                if b <= maxi:
                    b += 1
                    break
                if b > maxi:
                    maxi = b
        elif ethic == 0:
            if creat == 1:
                if c <= maxi:
                    c += 1
                    break
                if c > maxi:
                    maxi = c
            elif creat == 0:
                if d <= maxi:
                    d += 1
                    break
                if d > maxi:
                    maxi = d
    total += 1

    count += 1
    
    print('\nCount: %d'%count)
    print("Maximum:  %d"%maxi)
    print(out%(a,a/total,b,b/total,c,c/total,d,d/total))

    if count %50 == 0:
        input()

    
