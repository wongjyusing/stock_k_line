var json = (function() {
    var result;
    $.ajax({
        type:'GET',
        url:'http://127.0.0.1:8888',
        dataType:'json',
        async:false,
        success:function(data){
            result = data;
        }
    });
    return result;
})();

console.log(json)
