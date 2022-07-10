$(function()
{
    $('#create').click(function(){
        var valor1 = document.getElementById("NAME").value;
        var valor2 = document.getElementById("DESCRIP").value;
        var valor3 = document.getElementById("DATE").value;
        var valor4 = document.getElementById("HORA").value;
        var valor5 = document.getElementById("ZONA").value;
        var valor6 = document.getElementById("UBIC").value;
        var valor7 = document.getElementById("EMAIL").value;
        var valor8 = document.getElementById("FRECUENCI").value;
        var valor9 = document.getElementById("MEET").value;
        $.ajax({
            type: "POST",
            url:'http://127.0.0.1:8085/newevent',
            data:JSON.stringify({
                "NAME":valor1,"DESCRIP":valor2,"DATE":valor3,"HORA":valor4,"ZONA":valor5,"UBIC":valor6,"EMAIL":valor7,"FRECUENCI":valor8,"MEET":valor9
            }),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function(){
                alert("EVENTO CREADO");
            }
        })
        
    })
})