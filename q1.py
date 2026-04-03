def longest_palindromic_substring(s):
    max_len = 0
    start_index = 0
    
    for i in range(len(s)):
        for k in range(i + 1, len(s)):
            
            left = i
            right = k
            is_pal = True
            
            while left < right:
                if s[left] != s[right]:
                    is_pal = False
                    break
                left += 1
                right -= 1
            
            if is_pal:
                curr_len = k - i + 1
                
                if curr_len >= 2 and curr_len > max_len:
                    max_len = curr_len
                    start_index = i
    
    if max_len == 0:
        result = ""
    else:
        result = s[start_index:start_index + max_len]
    
    return result