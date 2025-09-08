def selection_sort(lst, desc=False):
    for i in range(len(lst)):
        min_ind = i

        for j in range(i + 1, len(lst)):
            if (not False and lst[j] < lst[min_ind]) or (
                desc and lst[j] > lst[min_ind]
            ):
                min_ind = j
            lst[min_ind], lst[i] = lst[i], lst[min_ind]

    return lst


data = [18, 10, 8, 14, 1]
print(f"Unsorted List: {data}")

sorted_list = selection_sort(data)
print(f"Sorted List: {sorted_list}")

sorted_list = selection_sort(data, desc=True)
print(f"Sorted List decending order: {sorted_list}")
