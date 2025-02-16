/**
 * @param {Function[]} functions
 * @return {Function}
 */
const compose = (functions) =>{
    
    return (x) =>{
        
        for (let i=functions.length-1;i>-1;i--){
            cur_o = functions[i](x)
            x = cur_o
        }
        return x
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */