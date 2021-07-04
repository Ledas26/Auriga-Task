# order:
# red, yellow, green, yellow, red
# or
# red, yellow, green with arrow, green, yellow, red

lights = [] #array of lights
with open('data.txt') as f:     
    for line in f:
        lights.append(line.replace("\n","")) #moving data to array

for i in range(1, len(lights)): #comparing lights 

    if lights[i] == '0,0,1,0': #when lights[i] - green
        if lights[i-1] == '0,1,0,0' or lights [i-1] == '0,0,0,1' or lights[i-1] == '0,0,0,0' or lights [i-1] == '0,0,1,0': 
            #previous light should be yellow, green with arrow, no light is on or also green
            continue
        else:
            quit("Traffic light is working wrong") 
    if lights[i] == '1,0,0,0': #when lights[i] - red
        if lights[i-1] == '0,1,0,0' or lights [i-1] == '1,0,0,0':
            #previous light should be yellow or also red
            continue
        else:
            quit("Traffic light is working wrong") 
    if lights[i] == '0,1,0,0': #when lights[i] - yellow
        if lights[i-1] == '1,0,0,0' or lights [i-1] == '0,0,0,1' or lights[i-1] == '0,0,0,0' or lights[i-1] == '0,0,1,0' or lights [i-1] == '0,1,0,0':
            #previous light should be red, green with arrow, no light is on, green or also yellow
            continue
        else:
            quit("Traffic light is working wrong") 
    if lights[i] == '0,0,0,1': #when lights[i] - green with arrow
        if lights[i-1] == '0,1,0,0' or lights [i-1] == '0,0,0,1' or lights [i-1] == '0,0,0,0':
            #previous light should be yellow, green with arrow or no light is on
            continue
        else:
            quit("Traffic light is working wrong") 
    if lights[i] == '0,0,0,0': #when lights[i] - no light is on
        if lights[i-1] == '0,0,1,0' or lights [i-1] == '0,0,0,1' or lights [i-1] == '0,0,0,0':
            #previous light should be green, green with arrow or no light is on
            continue
        else:
            quit("not valid") 

print("Traffic light is working correctly") 