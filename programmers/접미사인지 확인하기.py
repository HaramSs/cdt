def solution(my_string, is_suffix):
    answer = 0
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    return 0

print(solution("banana", "ana"))