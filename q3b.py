def add_binary(a, b):
    
    a = a[2:]
    b = b[2:]
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    
    while i >= 0 or j >= 0 or carry:
        
        if i >= 0:
            bit_a = ord(a[i]) - ord('0')
        else:
            bit_a = 0
            
        if j >= 0:
            bit_b = ord(b[j]) - ord('0')
        else:
            bit_b = 0
        
        total = bit_a + bit_b + carry      
        digit = total % 2
        carry = total // 2       
        result = chr(digit + ord('0')) + result
        
        i -= 1
        j -= 1
        
    k = 0
    while k < len(result) - 1 and result[k] == '0':
        k += 1
    
    result = result[k:]
    
    final_result = "0b" + result
    return final_result