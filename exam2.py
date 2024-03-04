def replace_duplicate_chars(string, k):
    result = ""
    seen_chars = []

    for i, char in enumerate(string):
        if char in seen_chars:
            print(i)
            print(char)
            result += "-"
        else:
            result += char
        # 更新已经出现过的字符集合
        seen_chars.append(char)
        print(seen_chars)
        # 移除超过k个位置之前的字符
        if i >= k:
            seen_chars.remove(string[i - k])

    return result

input_str = "abcdefaxc"
k = 10
output_str = replace_duplicate_chars(input_str, k)
print(output_str)

input_str = "abcdefaxcqwertba"
k = 10
output_str = replace_duplicate_chars(input_str, k)
print(output_str)