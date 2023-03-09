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
        $SubmitOS = $('#SubmitOS');
        $SubmitServer = $('#SubmitServer');
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
        //Vérification si les formulaires sont bien saisis
        if (hostname == null || !ip.match(regexp) || os == "" || typeserver == "" ){
            $.alert({
                title: 'Alert!',
                content: 'Formulaire saisit incorrect',
            });
        }
        else{
            //formattage des donénes à envoyer 
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

    // action quand on utilise le bouton pour ajouter un nouvel OS
    $SubmitOS.on('click',function(){
        let name = $('#OsName').val();
        let version = $('#OsVersion').val();

        // Vérification
        if (name == null || version == null){
            $.alert({
                title: 'Alert!',
                content: 'Formulaire saisit incorrect',
            });
        }
        else{
            //Création dictionnaire
            let data={};
            
            data["OS"] = name;
            data["version"] = version;

            //Conversion en format json
            json=JSON.stringify(data);
            console.log(json)
            //Acquisition du csrftoken
            let csrftoken=getCookie('csrf-token');

            $.ajaxSetup({
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('Csrf-Token', csrftoken);
                },
                         cache: false
            });

            $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                url: "/supervision/add_os_bdd/",
                type: "POST",
                content_type: "application/json",
                data: json,
                success: function(response){
                console.log(response);
                    $.alert({
                        title: 'Success',
                        content: 'Ajout réussit',
                    });
                    $('#addOS').modal('hide');
                }
            });
        }
    });

    $SubmitServer.on('click',function(){
        let name = $('#ServerName').val();
        let version = $('#ServerVersion').val();

        // Vérification
        if (name == null || version == null){
            $.alert({
                title: 'Alert!',
                content: 'Formulaire saisit incorrect',
            });
        }
        else{
            //Création dictionnaire
            let data={};
            
            data["Server"] = name;
            data["Version"] = version;

            //Conversion en format json
            json=JSON.stringify(data);
            console.log(json)
            //Acquisition du csrftoken
            let csrftoken=getCookie('csrf-token');

            $.ajaxSetup({
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('Csrf-Token', csrftoken);
                },
                         cache: false
            });

            $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                url: "/supervision/add_server_bdd/",
                type: "POST",
                content_type: "application/json",
                data: json,
                success: function(response){
                console.log(response);
                    $.alert({
                        title: 'Success',
                        content: 'Ajout réussit',
                    });
                    $('#addServer').modal('hide');
                }
            });
        }
    })
});