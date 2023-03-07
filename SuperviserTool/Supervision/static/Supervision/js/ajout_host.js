//fonction pour récupérer le coockie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
    var $submit = $('#validatebtn');
/*  TODO : REGEX pour check si l'input mis correspond bien a une adresse IP
    let n = 0;
    //compteur pour compter les numéros
    $input_ip.on("change paste keyup",function(){
        reg1 = new RegExp('([0-9]{1,3})');
        n += 1;
        
        let value = $(this).val();
        console.log(value);
        if (n == 3  ){
            if (reg1.test(value)){
                $(this).css('color','green');
            }
            else{
                $(this).css('color','red');
            }
        }
    }); */

    //Action à faire quand on valide le formulaire

    $submit.on('click',function(){
        let hostname=$('#inputhostname').val();
        let ip=$('#input_ip').val();
        let os=$('#selectOS option:selected').val();
        let typeserver=$('#selectServ option:selected').val();
        regexp = new RegExp('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$');

        if (hostname == null || !ip.match(regexp) || os == "" || typeserver == "" ){
            $.alert({
                title: 'Alert!',
                content: 'Formulaire saisit incorrect',
            });
        }
        else{
            let data={};
            data["hostname"]=hostname;
            data["ip"]=ip;
            data["os"]=os;
            data["server"]=typeserver;
            
            //On formatte bien les données pour l'envoi vers la view qui va ajouter la nouvelle machine en base
            json=JSON.stringify(data);
            console.log(json);

            // on récup le coockie sinon ca marche pas
            let csrftoken=getCookie('csrf-token');

            $.ajaxSetup({
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('Csrf-Token', csrftoken);
                },
                         cache: false
            });

            $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                url: "/supervision/add_host_bdd/",
                type: "POST",
                content_type: "application/json",
                data: json,
                success: function(response){
                console.log(response);
                    $.alert({
                        title: 'Success',
                        content: 'Ajout réussit',
                    });
                }
            });
            
        }
    });
});