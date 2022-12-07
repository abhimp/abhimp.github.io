---
layout: system
title: Tricks
menutype: system
menu_order: 40
---

### Embed all the font to a PDF

``$ gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sOutputFile=<Output.pdf> -f <Input.pdf>``


### Send msg with Whatsapp without saving contact

<form id="wacon">
<b> Phone number with ISD code </b>
<input type="number" name=phone />
<input type=submit value="Send Msg">
</form>
<script>
$("#wacon").submit(function(){
    var formdata = $(this).serializeArray()
    var num = null
    formdata.forEach(element => {
        if(element['name'] == "phone"){
            num = element["value"]
        }
    });
    num = num.replace(/\D/g,'');
    if(num == false || num == null || num == "") {
            return false
    }
    if(num.length < 10) {
        alert("Enter Valid Number")
        return false
    }
    if(num.length == 10){
        num = "91" + num
    }
    window.open("http://api.whatsapp.com/send?phone="+num, "_blank")
    return false
})  
</script>
