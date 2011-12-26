$(document).ready(function() {
	alert('11111111есть ответ');
	var options = {
		//target: '#results',
		//dataType: json,
		beforeSubmit:checkInfo,
		success:compliteJson,
	};
	$('#contactForm').ajaxForm(options);
	alert('есть отdddddddddddddddddddddddddddddвет');
});

function compliteJson(response) {
	alert(wwwwwwwwwwwwww);
	if (response.status == 'Ok')
	{
		//$('#status').html("Information successfully updated.");
		//$('#status').css({color: "green"});
		//$("#myForm").ajaxSubmit(options);
		alert('status ok'); 
		$('#contactForm').html(response.text);
		//$('#results').show();
		$('#results').html("Information successfully updated.");
		//$('#results').hide(1600);
	}
	else
	{
		alert("Error");
		$('#results').html("Enter valid values.");
	
	}
}

function checkInfo() {
	alert('checkinfo');
}
$(document).ajaxStart(function() {
	alert('start ajax');
	$('#contactForm input').attr("disabled", "disabled");
	$('#contactForm textarea').attr("disabled", "disabled");
	$('#results').html("Sending form data...");

});
$(document).ajaxStop(function() {
	alert('stop ajax');
	$('#contactForm input').removeAttr("disabled");
	$('#contacForm textarea').removeAttr("disabled");
});