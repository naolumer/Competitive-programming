/**
 * @param {Function} fn
 * @return {Function}
 */
const once = (fn)=> {
    let count =1
    return (...args)=>{
        if (count===1){
            count++
            return fn(...args)
        }
        return undefined   
    }
};