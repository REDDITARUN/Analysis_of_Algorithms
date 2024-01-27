

def readcnp():
    citylist = []  
    while True:
        try:
            forline = input() 
            city, population = map(int, forline.split())  
            citylist.append((city, population))  
        except EOFError:  
            break
    return citylist  

def sortcbyp(citylist):
    def ms(arr):
        if len(arr) <= 1:
            return arr  

        middlepointer = len(arr) // 2
        left = arr[:middlepointer]
        right = arr[middlepointer:]

        result = []  
        lidx = 0 
        ridx = 0 

        left = ms(left)  
        right = ms(right)  

        while lidx < len(left) and ridx < len(right):
            if left[lidx][1] <= right[ridx][1]:
                result.append(left[lidx])  
                lidx += 1
            else:
                result.append(right[ridx])  #
                ridx += 1

        result.extend(left[lidx:])  
        result.extend(right[ridx:])  

        return result  

    sorted_cities = ms(citylist)

    for city in sorted_cities:
        print(f"{city[0]} {city[1]}")  

citylist = readcnp()  
sortcbyp(citylist)  
