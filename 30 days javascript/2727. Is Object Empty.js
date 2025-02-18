/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
const isEmpty = (obj)=> {
    if(Object.keys(obj).length===0){
        return true
    }
    return false  
};