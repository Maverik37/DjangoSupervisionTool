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

function get_user(){
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let endpoint = document.getElementById('btn_connexion').getAttribute('data-url');
    json= {};
    json["username"] = username;
    json["password"] = password;
    
    let csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr) {
                xhr.setRequestHeader('Csrf-Token', csrftoken);
            },
            cache: false
    });
 
  $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        url: endpoint,
        type: "post",
        data: JSON.stringify(json),
    });

    console.log(username+" / "+password+" / "+endpoint)
};