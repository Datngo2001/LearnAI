def chiaHetCho5(nums):
    chiahet = []
    for num in nums:
        if (num % 5) == 0 : 
            chiahet.append(num)
    return chiahet

arr = [1,2,6,3,5,7,5,10]

arr = chiaHetCho5(arr)

print(arr)