def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return True

        elif total < target:
            left += 1

        else:
            right -= 1

    return False
arr=list(map(int,input("Enter array elements:").split()))
target=int(input("Enter target:"))
print(pair_sum(arr,target))