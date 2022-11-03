def countingValleys(steps, path):
    valley_count = sea_level = 0
    dic = {'U' : 1, 'D' : -1}
    
    for i in path:
        sea_level += dic[i]
        if sea_level == 0 and i == 'U':
            valley_count += 1
    return valley_count 
