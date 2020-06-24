def is_even(preset_num, ttl_even, ttl_not_even):
    if preset_num == 0:
        print(f'A number {preset_num} is made up of {ttl_even + ttl_not_even} '
              f'numbers and has {ttl_even} even and {ttl_not_even} odd numbers.')
    else:
        tmp = preset_num % 10
        if tmp % 2 == 0:
            ttl_even += 1
        else:
            ttl_not_even += 1
        tmp_num = tmp_num // 10
        return is_even(tmp_num, ttl_even, ttl_not_even)


is_even((input('Enter the number: ')), 0, 0)
