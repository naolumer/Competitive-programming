Array.prototype.groupBy = function(fn) {
    let result = {};

    this.forEach(x => {
        if (result[fn(x)]) result[fn(x)].push(x);
        else result[fn(x)] = [x];
    });

    return result;
};