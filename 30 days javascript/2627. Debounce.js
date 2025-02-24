const debounce = (fn, t)=> {
    var deb;
    return (...args)=> {
        clearTimeout(deb);
        deb = setTimeout(() =>{fn(...args)}, t);
    }
};