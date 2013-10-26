$(document).ready(function(){
	var ws;

	ws = new WebSocket("ws://localhost:8888/ws");

	$(function() {
	   $( "#vertical-slider" ).slider({
	   	 orientation: "vertical",
	     value:90,
	     min: 0,
	     max: 180,
	     step: 15,
	     slide: function( event, ui ) {
	       $( "input.vertical-angle" ).val( "vertical-" + ui.value );
			ws.send(ui.value);
	     }
	   });
	
//	   $( "#amount" ).val( "$" + $( "#slider" ).slider( "value" ) );
	});

	$(function() {
	   $( "#horizontal-slider" ).slider({
	     value:90,
	     min: 0,
	     max: 180,
	     step: 15,
	     slide: function( event, ui ) {
	       $( "input.horiz-angle" ).val( "horiz-" + ui.value );
			ws.send(ui.value);
	     }
	   });
	});

	ws.onopen = function(evt) { 
		$(".angle").css("background", "#00ff00"); 
		alert("Connection openned!");
	};


});

/* Potential Stringify code

websocket.send(JSON.stringify({
  id: "client1"
}));

*/