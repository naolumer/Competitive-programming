def maxChunksToSorted(arr):
    max_seen = 0
    chunks = 0

    for index,num in enumerate(arr):
        max_seen = max(max_seen,num)
        if max_seen == index:
            chunks+=1
    return chunks
# print(maxChunksToSorted([1,0,2,3,4])) 
    