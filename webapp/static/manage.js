function deleteSecret(t) {
    if (confirm("Confirm delete secret?")) {
        $.post( $(t).attr("data-url") ,{id:$(t).attr("data-secret-id")}, function(){
            window.location.reload()
        })
    }
}