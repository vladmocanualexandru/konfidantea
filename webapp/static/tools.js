const KEY_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

function generateKey(){
    let key = ""

    for (let i=0; i<32; i++) {
        key += KEY_CHARS[Math.floor((Math.random()*KEY_CHARS.length))]
    }

    $("#kgKeyTA").val(key)
}

function encrypt(t) {
    $.post( $(t).attr("data-url") ,{content:$("#eContentTA").val(), key:$("#eKeyTA").val()}, function(data){
        $("#eECTA").val(data)
    })
}

function decrypt(t) {
    $.post( $(t).attr("data-url") ,{content:$("#eContentTA").val(), key:$("#eKeyTA").val()}, function(data){
        $("#eECTA").val(data)
    })
}