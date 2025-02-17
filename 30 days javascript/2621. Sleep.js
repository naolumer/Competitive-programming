/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    const ans = await new Promise(resolve=> setTimeout(resolve,millis))
    return ans
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */