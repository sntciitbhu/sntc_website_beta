function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    console.log('id_token:  '+id_token)
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


    console.log("check if user exists");
    $.ajax({
        type: "GET",
        dataType: 'text',
        data: {'tokenid' : response},
        url: '/user',
        success:function(msg){
        if(!msg.exist)
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
        }
    });
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
