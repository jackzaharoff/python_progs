import threading


def selection_sort(int_list):
    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list)):
            if int_list[i] > int_list[j]:
                # tuple packing and unpacking in action to swap two values
                int_list[i], int_list[j] = int_list[j], int_list[i]
    print('Selection sort thread finished.')


def insertion_sort(int_list):
    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list)):
            if int_list[i] > int_list[j]:
                temp = int_list[j]
                for k in range(j, i, -1):
                    int_list[k] = int_list[k - 1]
                int_list[i] = temp
    print('Insertion sort thread finished.')


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(int_list):
    """
    Classic merge sort algorithm when an array is split in two while the the left and right arrays become of
    length one, which means they are already sorted. Then the remaining work is done by the merge function.
    """
    if len(int_list) <= 1:
        return int_list
    else:
        middle = int(len(int_list) / 2)
        left = int_list[:middle]
        right = int_list[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
    return merge(left, right)


def print_merge_sort_result(int_list):
    """
    I am sure there is a better way to do this, but for the purposes of this illustration it works fine.
    """
    merge_sort(int_list)
    print('Merge sort thread finished.')


def main():
    """
    To illustrate that for sufficiently large n merge sort is faster than
     selection and insertion sort. Merge sort has O(nlog(n)) while insertion and selection sort
     have O(n**2) running time.
    """
    for n in range(1000, 11000, 1000):
        int_list = [n for n in range(n, 0, -1)]  # this is the worst case when the array is sorted in reverse order
        thread_selection_sort = threading.Timer(1, selection_sort, (int_list[:],))
        # threading.Thread(target=selection_sort, args=(int_list[:],))
        thread_insertion_sort = threading.Timer(1, insertion_sort, (int_list[:],))
        # threading.Thread(target=insertion_sort, args=(int_list[:],))
        thread_merge_sort = threading.Timer(1, print_merge_sort_result, (int_list[:],))
        # threading.Thread(target=merge_sort, args=(int_list[:],))
        thread_insertion_sort.start()
        thread_selection_sort.start()
        thread_merge_sort.start()
    print('Main thread finished.')


if __name__ == '__main__':
    main()