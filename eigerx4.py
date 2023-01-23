def count_max_elements(input, max_number=0, instance_counter=0, instance_counter_curr=0):
    print(input)
    if (len(input))==0 :
        print("(%d; %d)" % (max_number, instance_counter))
        return
    else:
        n=input.pop(0)
        if n == 0:
            print("(%d; %d)" % (max_number, instance_counter))
            return
        if n > max_number:
            max_number = n
            instance_counter_curr = 1
        elif n == max_number:
            instance_counter_curr += 1
        instance_counter = max_number(instance_counter, instance_counter_curr)
        count_max_elements(input, max_number, instance_counter, instance_counter_curr)

numbers = [1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0]
count_max_elements(numbers)