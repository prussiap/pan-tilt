$(document).ready(function(){
	var ws;
	ws = new WebSocket("ws://localhost:8888/ws");

	ws.onopen = function(evt) { 
		$(".angle").css("background", "#00ff00"); 
		alert("Connection openned!");
	};

	$(".angle").change(function(){
		var angle = $("input.angle").val();
		ws.send(angle);
	});

	
});