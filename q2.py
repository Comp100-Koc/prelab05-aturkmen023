def remove_adjacent_duplicates(s):
    while True:
        
        result = ""
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                i += 2
            else:
                result += s[i]
                i += 1
        
        if result == s:
            break
        
        s = result
    
    final_result = s
    return final_result