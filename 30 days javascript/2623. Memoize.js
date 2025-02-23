/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    const cache = {}
    
    return (...args)=> {
        const key = JSON.stringify(args)
        if (key in cache) {
            return cache[key]
        } else {
            cache[key] = fn(...args)
        }
        return cache[key]
    }
}

