/**
 * @param {number} n
 * @return {Function} counter
 */
const createCounter =(n)=> {
    return () =>{
       return n++;
    } 
};

