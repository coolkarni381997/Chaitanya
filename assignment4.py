test_cases = int(input())

for k in range(test_cases):
    no_caves = int(input())
    cave_radiation = str(input())
    c_power = cave_radiation.split(" ")
    c_level = [0 for i in range(no_caves)]

    health_zombies = str(input())
    h_level = health_zombies.split(" ")

    for i in range(0,len(c_power)):
        c_power[i] = int(c_power[i])
        h_level[i] = int(h_level[i])

    h_level.sort(reverse=True)
    abcd = len(c_power)
    for i in range(0,len(c_level),2):
        if(i+1>=len(c_level)):
            c_level[i] += c_power[abcd - 1]
            abcd -= 1
        else:
            c_level[i] += c_power[abcd - 1]
            c_level[i + 1] += c_power[abcd - 1]
            abcd -= 1

    if(set(c_level) == set(h_level)):
        print("YES")
    else:
        print("NO")

    # for i in range(0,len(c_power)):
    #     for j in range(i-c_power[i],i+c_power[i]+1):
    #         if(j<0 or j>len(c_power)-1):
    #             continue
    #         else:
    #             c_level[j] = c_level[j] + 1

    # flag = 0
    # for i in range(0, len(c_level)):
    #     if(c_level[i] == h_level[i]):
    #         continue
    #     else:
    #         flag = 1
    #         break
    #
    # if(flag == 0):
    #     print("YES")
    # else:
    #     print("NO")