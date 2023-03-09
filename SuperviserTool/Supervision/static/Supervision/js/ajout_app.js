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
        $PathScenario = $('#scenario_path');
        $PathResultat = $('#res_path');
        $SubmitJmx = $('#SubmitNewJmx');
        $JmxName = $('#name_scenario');

    //Action à faire quand on valide le formulaire
    //PréRemplissage des input pour les path
    $PathScenario.val('/home/fourbasse/scripts/JMETER/scenarios/')
    $PathResultat.val('/home/fourbasse/scripts/JMETER/resultats/')


    // Envoi des données concernant la nouvelle application a ajouter
    $submit.on('click',function(){
        // On récupère les différentes valeurs
        let app=$('#inputappname').val();
        let host=$('#selectHost option:selected').val();
        let JMX=$('#selectJMX option:selected').val();

        // On vérifie que les données ont bien été saisies
        if (host == null || app == null || JMX == null){
            $.alert({
                title: 'Alert!',
                content: 'Formulaire saisit incorrect',
            });
        }
        else{
            // On crée un dict a envoyer via ajax
            let data={};

            data["Application"]=app;
            data["hostname"]=host;
            data["JMX"]=JMX;
            
            //On formatte bien les données pour l'envoi vers la view qui va ajouter la nouvelle machine en base
            json=JSON.stringify(data);

            // on récup le coockie sinon ca marche pas
            let csrftoken=getCookie('csrf-token');
            // paramétrage avant l'appel AJAX
            $.ajaxSetup({
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('Csrf-Token', csrftoken);
                },
                         cache: false
            });

            //Appel Ajax
            $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                url: "/supervision/add_app_bdd/",
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

    // envoi data pour ajouter le nouveau scénario
    $SubmitJmx.on('click',function(){
        let jmx_name = $JmxName.val()+$('#basic-addon2').text();
        let jmx_path_scenario = $PathScenario.val();
        let jmx_path_resu = $PathResultat.val()

        // Creation data à envoyer dans l'AJAX
        let data = {};

        data["name"] = jmx_name;
        data["path_scenario"] = jmx_path_scenario;
        data["path_resu"] = jmx_path_resu;

        //On formatte bien les données pour l'envoi vers la view qui va ajouter la nouvelle machine en base
        json=JSON.stringify(data);

        // on récup le coockie sinon ca marche pas
        let csrftoken=getCookie('csrf-token');
        // paramétrage avant l'appel AJAX
        $.ajaxSetup({
            beforeSend: function(xhr) {
                xhr.setRequestHeader('Csrf-Token', csrftoken);
            },
                     cache: false
        });

        //Appel Ajax
        $.ajax({
            headers: { "X-CSRFToken": csrftoken },
            url: "/supervision/add_jmx_bdd/",
            type: "POST",
            cache: false,
            content_type: "application/json",
            data: json,
            success: function(response){
            console.log(response);
                $.alert({
                    title: 'Success',
                    content: 'Ajout réussit',
                });
                $('#addJMX').modal('hide');
            }
        });
        
    });
});