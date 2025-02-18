/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
const chunk = (arr, size)=> {
    const chunk = [];
    let i = 0;
    while (i<arr.length) {
        const chunked = arr.slice(i,i+size);
        chunk.push(chunked);
        i = i+size
    }
    return chunk

    
};