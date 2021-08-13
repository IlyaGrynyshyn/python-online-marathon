def double_string(data):
    count = 0
    for x in data:
        if any(x + y in data for y in data):
            count += 1
    return count


data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data))
