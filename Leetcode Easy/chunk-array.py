
def chunked(array,size):

    chunk = []   # array to store chunked arrays
    i=0
    while i<len(array):

        chunked = array[i:i+size]
        chunk.append(chunked)
        i = i + size
    return chunk