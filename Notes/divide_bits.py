
def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    
    while x >= y:
        while y_power > 1:
            y_power >>= 1
            power -= 1
            
        result += 1 << power
        x -= y_power
     return result 
     
#Time complexity is O(n), individual shifts and add operations O(1) time








