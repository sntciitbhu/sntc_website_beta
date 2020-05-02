// var events = [
//   {'Date': new Date(2016, 6, 7), 'Title': 'Doctor appointment at 3:25pm.'},
//   {'Date': new Date(2016, 6, 18), 'Title': 'New Garfield movie comes out!', 'Link': 'https://garfield.com'},
//   {'Date': new Date(2016, 6, 27), 'Title': '25 year anniversary', 'Link': 'https://www.google.com.au/#q=anniversary+gifts'},
// ];

var events = [
  {'Date': new Date(2020, 6, 1), 'Title': 'Doctor appointment at 3:25pm.', 'Link': function(){console.log('Reminder!');}},
  {'Date': new Date(2020, 6, 7), 'Title': 'New Garfield movie comes out!', 'Link': function(){alert("Better not miss the movie!");}},
  {'Date': new Date(2020, 6, 11), 'Title': '25 year anniversary', 'Link': function(){console.debug(document.getElementById('foo'));}},
];


var settings={
  Color: '#999',                //(string - color) font color of whole calendar.
  LinkColor: '#333',            //(string - color) font color of event titles.
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
