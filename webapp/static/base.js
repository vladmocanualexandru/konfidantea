function initDb(t) {
    if(confirm("Confirm database initialization?")) {
        $.post( $(t).attr("data-url") ,{}, function(){
            window.open($(t).attr("data-return-url"), "_self")
        })
    }
}