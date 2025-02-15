/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
const map = (arr, fn)=> {

    new_arr = arr.map((item,i)=>{
        return fn(item,i)
    })
    return new_arr
    
};