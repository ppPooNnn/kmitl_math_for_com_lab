Instructor = ['Witchaya','Teera','Suntana']
Sales = ['Mini','Honda','Toyota']

Instructor_prefs = {
    'Witchaya' : ['Honda','Mini','Toyota'],
    'Teera' : ['Mini','Toyota','Honda'],
    'Suntana' : ['Mini','Honda','Toyota']
}

Sales_prefs = {
    'Mini' : ['Witchaya','Teera','Suntana'],
    'Honda' : ['Suntana','Teera','Witchaya'],
    'Toyota' : ['Witchaya','Teera','Suntana']
}

def com_sci_garage():
    instructor_free = list(Instructor)

    sales_pair = {
        'Witchaya' : '',
        'Teera' : '',
        'Suntana' : ''
    }

    key_list = list(sales_pair.keys())

    while len(instructor_free) > 0:
        for instructor in key_list:
            for sales in Instructor_prefs[instructor]:

                if sales not in list(sales_pair.values()):
                    sales_pair[instructor] = sales
                    instructor_free.remove(instructor)
                    break

                elif sales in list(sales_pair.values()):
                    current_pair = list(sales_pair.keys())[list(sales_pair.values()).index(sales)]
                    sales_prefs_list = Sales_prefs.get(sales) 

                    if (sales_prefs_list.index(instructor) < sales_prefs_list.index(current_pair)):
                        sales_pair[instructor] = sales
                        instructor_free.remove(instructor)


                        sales_pair[current_pair] = ''
                        instructor_free.append(current_pair)
                        break

    for instructor in sales_pair.keys():
        print(f"{instructor} buys the {sales_pair[instructor]} car")

com_sci_garage()