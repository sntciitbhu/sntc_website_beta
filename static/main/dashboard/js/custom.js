var auth2;

function onLoad() {
  console.log("onload")
  gapi.load('auth2', function () {
    auth2 = gapi.auth2.init({
      client_id: '230326381758-a6egb1esqcqml0iv8uccm7jknriq0cjr.apps.googleusercontent.com',
      scope: 'profile'
    });

    auth2.then(checkUser, signOut);

  });
}

function checkUser() {
  var instance = gapi.auth2.getAuthInstance();

  if (instance.isSignedIn.get()) {
    var user = instance.currentUser.get();
    console.log(user);
    console.log(instance.currentUser.get().getBasicProfile());
    var profile = instance.currentUser.get().getBasicProfile();
    document.getElementById("profile-image").src = profile.getImageUrl();
  } else {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      $.ajax({
        type: "GET",
        dataType: 'text',
        data: {
          'action': 'logout'
        },
        url: '/user',
        success: function (msg) {
          console.log('User signed out.');
          window.location.replace('/login');
        }
      });


    });

  }
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    $.ajax({
      type: "GET",
      dataType: 'text',
      data: {
        'action': 'logout'
      },
      url: '/user',
      success: function (msg) {
        console.log('User signed out.');
        window.location.replace('/');
      }
    });


  });
}

window.setTimeout(function () {
  $(".alert").fadeTo(500, 0).slideUp(500, function () {
    $(this).remove();
  });
}, 2000);


$("#edit-profile").on('click',function(){
  $(this).hide();
  var instance = gapi.auth2.getAuthInstance();

  if (instance.isSignedIn.get()) {
    var user = instance.currentUser.get();
    var expire = user.getAuthResponse().expires_in;

    if(expire<600)
      response = user.reloadAuthResponse();
    else
      response = user.getAuthResponse();

    console.log(response.id_token)
  }
  else{
    console.log("user signed out")
    return false
  }
  $('#id_token').val(response.id_token);
  $('#sub_clubs')
  $("#save-profile, #cancel-profile").show();
  $("#profile fieldset" ).prop("disabled",false);
});


$("#cancel-profile").on('click',function(){
  $("#edit-profile").show();
  $("#save-profile, #cancel-profile").hide();
  $("#profile fieldset" ).prop("disabled",true);
  $('#profile-form').trigger("reset");
});


$("#profile-form").submit(function(){
  var clubs = [];
  console.log("submit");
  $("#sub-clubs-checkbox input:checkbox[name=clubs]:checked").each(function(){
    clubs.push($(this).val());
    console.log(clubs)

});
$("#sub_clubs").val(clubs);
return true
});