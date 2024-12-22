
def chunked(array,size):

    chunk = []
    i=0
    while i<len(array):

        chunked = array[i:i+size]
        chunk.append(chunked)
        i = i + size
    return chunk

print(chunked([8,5,3,2,6],6))