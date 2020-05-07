$(".more").on('click', function () {
  document.getElementById("mySidenav").style.width = "100%";
  $(".mobile-nav").css("display","none");
  $(".mobile-nav-toggle").css("display","none");
  $(".mobile-nav-overly").css("display","none");

});

  
  /* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    $(".mobile-nav").css("display","block");
    $(".mobile-nav-toggle").css("display","block");
  }


  // var events = [
//   {'Date': new Date(2016, 6, 7), 'Title': 'Doctor appointment at 3:25pm.'},
//   {'Date': new Date(2016, 6, 18), 'Title': 'New Garfield movie comes out!', 'Link': 'https://garfield.com'},
//   {'Date': new Date(2016, 6, 27), 'Title': '25 year anniversary', 'Link': 'https://www.google.com.au/#q=anniversary+gifts'},
// ];

var events = [
    {'Date': new Date(2020, 6, 1), 'Title': 'Doctor appointment at 3:25pm.', 'Link': function(){console.log('Reminder!');}},
    {'Date': new Date(2020, 6, 7), 'Title': 'New Garfield movie comes out!', 'Link': function(){alert("Better not miss the movie!");}},
    {'Date': new Date(2020, 6, 11), 'Title': '25 year anniversary', 'Link': function(){console.debug(document.getElementById('foo'));}},
    {'Date': new Date(2020, 4, 3), 'Title': '25 year anniversary', 'Link': function(){console.debug(document.getElementById('foo'));}},
 
];
  
  
  var settings={
    Color: '#111',                //(string - color) font color of whole calendar.
    LinkColor: '#999',            //(string - color) font color of event titles.
    NavShow: true,                //(bool) show navigation arrows.
    NavVertical: false,           //(bool) show previous and coming months.
    DateTimeShow: true,           //(bool) show current date.
    DateTimeFormat: 'dd, mmm, yyyy',  //(string - dateformat) format previously mentioned date is shown in.
    DatetimeLocation: '',         //(string - element) where to display previously mentioned date, if not in default position.
    EventClick: '',               //(function) a function that should instantiate on the click of any event. parameters passed in via data link attribute.
    EventTargetWholeDay: false,   //(bool) clicking on the whole date will trigger event action, as opposed to just clicking on the title.
    DisabledDays: [],             //(array of numbers) days of the week to be slightly transparent. ie: [1,6] to fade Sunday and Saturday.
  }
  
  var element = document.getElementById('caleandar');
  caleandar(element, events, settings);
  
  var angleStart = -360;

  
  // jquery rotate animation
  function rotate(li,d) {
      $({d:angleStart}).animate({d:d}, {
          step: function(now) {
              $(li)
                 .css({ transform: 'rotate('+now+'deg)' })
                 .find('img')
                    .css({ transform: 'rotate('+(-now)+'deg)' });
          }, duration: 0
      });
  }
  
  // show / hide the options
  function toggleOptionsopen(s) {
      $(s).addClass('open');
      var li = $(s).find('li');
      var deg = $(s).hasClass('half') ? 180/(li.length-1) : 360/li.length;
      for(var i=0; i<li.length; i++) {
          var d = $(s).hasClass('half') ? (i*deg)-90 : i*deg;
          $(s).hasClass('open') ? rotate(li[i],d) : rotate(li[i],angleStart);
      }
  }

  function toggleOptionsclose(s) {
    $(s).removeClass('open');
    var li = $(s).find('li');
    var deg = $(s).hasClass('half') ? 180/(li.length-1) : 360/li.length;
    for(var i=0; i<li.length; i++) {
        var d = $(s).hasClass('half') ? (i*deg)-90 : i*deg;
        $(s).hasClass('open') ? rotate(li[i],d) : rotate(li[i],angleStart);
    }
}
  
  // $('.selector button').click(function(e) {
  //     toggleOptions($(this).parent());
  // });

  $(window).on('scroll', function() {
    var cur_pos = $(this).scrollTop() + 400;
    var menu = $('.selector')

    $('.featured').each(function() {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();
      if (cur_pos >= top && cur_pos <= bottom) {
          toggleOptionsopen(menu);
          $('.featured .tab-content').show();
        }
      else{
        toggleOptionsclose(menu);
        $('.featured .tab-content').hide();

      }
    });
  });

  setTimeout(function() { toggleOptionsopen('.selector'); }, 100);