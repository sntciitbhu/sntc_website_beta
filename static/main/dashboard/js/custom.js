var auth2;

  gapi.load('auth2',function(){
    auth2 = gapi.auth2.init({
            client_id: '230326381758-a6egb1esqcqml0iv8uccm7jknriq0cjr.apps.googleusercontent.com',
            scope: 'profile'
        });

    auth2.then(checkUser);

  });

  function checkUser()
  {

    if(auth2.isSignedIn.get())
    {
      var user = auth2.currentUser.get();
      console.log(user);
      console.log(auth2.currentUser.get().getBasicProfile());
      var profile = auth2.currentUser.get().getBasicProfile();
      document.getElementById("profile-image").src = profile.getImageUrl();
    }
    else
    {
      window.location.replace('/login')
    }

  }

  function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      $.ajax({
        type: "GET",
        dataType: 'text',
        data: {'action' : 'logout'},
        url: '/user',
        success:function(msg){
          console.log('User signed out.');
          window.location.replace('/');
        }
    });


    });
    }

  window.setTimeout(function() {
      $(".alert").fadeTo(500, 0).slideUp(500, function(){
          $(this).remove(); 
      });
  }, 2000);

