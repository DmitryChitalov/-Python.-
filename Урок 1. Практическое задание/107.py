try:
    user_data_1 = int(input('Enter the 1st side of the triangle: '))
    user_data_2 = int(input('Enter the 2nd side of the triangle: '))
    user_data_3 = int(input('Enter the 3rd side of the triangle: '))
    triangle_side_max = 0
    triangle_side_a = 0
    triangle_side_b = 0
    if (user_data_1 + user_data_2) > user_data_3 \
    and (user_data_1 + user_data_3) > user_data_2 \
    and (user_data_2 + user_data_3) > user_data_1:
        if user_data_1 == user_data_2 == user_data_3:
            print('Triangle with preset sides - equilateral.')
        else:
            if user_data_1 > user_data_2 > user_data_3:
                triangle_side_max = user_data_1
                triangle_side_a = user_data_2
                triangle_side_b = user_data_3
            elif user_data_2 > user_data_1 > user_data_3:
                triangle_side_max = user_data_2
                triangle_side_a = user_data_1
                triangle_side_b = user_data_3
            else:
                triangle_side_max = user_data_3
                triangle_side_a = user_data_1
                triangle_side_b = user_data_2
            if triangle_side_max ** 2 == triangle_side_a ** 2 + triangle_side_b ** 2:
                print('Triangle with preset sides - rectangular.')
            elif triangle_side_max ** 2 < triangle_side_a ** 2 + triangle_side_b ** 2:
                print('Triangle with preset sides - angular.')
            else:
                print('Triangle with given sides - obtuse.')
    else:
        print('Triangle with preset sides impossible')
except TypeError:
    print('Unsupported data type. Please try numbers.')
