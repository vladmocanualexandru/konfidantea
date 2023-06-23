function initDb(t) {
    if(confirm("Confirm db init?")) {
        $.post( $(t).attr("data-url") ,{}, function(){
            window.location.reload()
        })
    }
}