def most_common():
    print("imput your numbers")
    print("when you are done with your set press enter")
    print("----------------------------------------------")
    add_list = input("input a number ")
    test_list = [add_list]
    while add_list != "":
        add_list = input("input a number ")
        test_list.append(add_list)
    print ("Original list : " + str(test_list))
    max = 0
    res = test_list[0]
    for i in test_list:
        freq = test_list.count(i)
        if freq > max:
            max = freq
            res = i
    print ("Most frequent charicter is : " + str(res))