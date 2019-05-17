def get_remap_table_for_remap_range(num_bins, MAXIMUM):
    result = []
    MAXIMUM = float(MAXIMUM)
    for i in range(num_bins):
        lower_range = i * (MAXIMUM/num_bins)
        upper_range = (i + 1) * (MAXIMUM/num_bins)
        result.append([lower_range, upper_range, i+1])
    return result

def print_remap_ranges(remap_range):
    for item in remap_range:
        print('{}.) [{}, {}]'.format(item[2], item[0], item[1]))

print_remap_ranges(get_remap_table_for_remap_range(10, 14653.2))
print("")
print_remap_ranges(get_remap_table_for_remap_range(20, 14653.2))
print("")
print_remap_ranges(get_remap_table_for_remap_range(150, 14653.2))