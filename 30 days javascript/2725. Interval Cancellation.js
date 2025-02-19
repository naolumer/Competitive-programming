const cancellable = (fn, args, t)=> {
    fn(...args)

    const cancelFn = ()=> clearTimeout(timer)

    const timer = setInterval(()=>{
        fn(...args)
    },t) 
    return cancelFn  
};