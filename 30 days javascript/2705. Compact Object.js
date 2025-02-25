/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
const compactObject =(obj)=> {

    
    if (Array.isArray(obj)){
        let result = []
        for (let element of obj){
            if (element){
                if (Array.isArray(element) || typeof element=="object"){
                    result.push(compactObject(element))
                }
                else {
                    result.push(element)
                }
            }
        }
    return result
    } else {
        let result = {}
        for (let key in obj){
            if (obj[key]){
                if (Array.isArray(obj[key]) || typeof obj[key]=="object"){
                    result[key]=compactObject(obj[key])
                }
                else {
                    result[key]= obj[key]
                }
            }
        }
    return result
    }  
};