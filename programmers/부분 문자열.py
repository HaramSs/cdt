def solution(str1, str2):
    answer = 0
    if str1 in str2:
        return 1
    else:
        return 0
    return answer

print(solution("abc", "aabcc"))