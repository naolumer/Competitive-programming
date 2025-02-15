/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
const reduce = (nums, fn, init)=> {

    if (!nums){
        return init
    }
    let val = init
    for (let i = 0;i<nums.length;i++){
        cur_val = fn(val,nums[i])
        val = cur_val
    }
    return val
};