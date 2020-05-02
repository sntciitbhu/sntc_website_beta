function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
    var expire = googleUser.getAuthResponse().expires_in;
    // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    console.log('id_token:  '+id_token)
    console.log('time:   '+ expire)
    check_userexists(id_token,profile)
}
  
  
function check_userexists(response,profile){
    var card = document.getElementById('flipbox');
    var frontcard = document.getElementById('front-card');
    var back = document.getElementById('back-page');
    var auth = document.getElementById('id_token');
    var name = document.getElementById('name');
    var email = document.getElementById('email');
    var e_mail = document.getElementById('e-mail');
    var img = document.getElementById('profile-img');
    document.getElementById("loader").style.display = "block";
    $.ajax({
        type: "GET",
        dataType: 'text',
        data: {'tokenid' : response, 'action' : 'login'},
        url: '/user',
        success:function(msg){
            val = JSON.parse(msg);
            console.log(val.exists);
            if(!val.exists)
            {
                card.classList.toggle('flip');
                frontcard.classList.add("disabledbutton");
                back.classList.remove("disabledbutton");
                auth.value = response;
                name.value = profile.getName();
                email.value = profile.getEmail();
                e_mail.value = profile.getEmail();
                img.src = profile.getImageUrl();
            }
            else
            {
                window.location.replace('/dashboard')
            }
        }
    });
}

window.onload = function(e){
    signOut();
    console.log("signout");
}

function signOut() {
var auth2 = gapi.auth2.getAuthInstance();
auth2.signOut().then(function () {
    console.log('User signed out.');
});
}

var card = document.getElementById('flipbox');
var frontcard = document.getElementById('front-card');
var back = document.getElementById('back-page');
var auth = document.getElementById('auth_token')


    document.getElementById('button-new').addEventListener('click', function() {
    card.classList.toggle('flip');frontcard.classList.add("disabledbutton");back.classList.remove("disabledbutton");
    auth.value= "dsjakfbcsdkhcfs";
}, false);
