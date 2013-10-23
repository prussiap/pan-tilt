$(document).ready(function(){
	var ws;
	console.log("ready");
	$("#open").click(function(evt) {
		evt.preventDefault();

		var host = $("#host").val();
		var port = $("#port").val();
		var uri = $("#uri").val();

		ws = new WebSocket("ws://" + host + ":" + port + uri);

		$(".angle").change(function(){
			var angle = $("input.angle").val();
			ws.send(angle);
		});

//		ws.onclose = function(evt) { alert("Connection closed"); };

		ws.onopen = function(evt) { 
			$("#host").css("background", "#00ff00"); 
			$("#port").css("background", "#00ff00"); 
			$("#uri").css("background", "#00ff00");
			console.log("openned");
		};
	});



});