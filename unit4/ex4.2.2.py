def parse_ranges(ranges_string):
    ranges_list= ranges_string.split(',')
    first_generator= ([x.split('-')[0],x.split('-')[1]] for x in ranges_list)
    for start, stop in first_generator:
        for num in range(int(start), int(stop)+1):
            yield num
print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))

