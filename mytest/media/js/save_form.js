$(document).ready(function(){
    var options = {
        dataType: 'json',
        //method: 'post',
        //target: '#contactForm',
        //iframeTarget: '#img',
        semantic: true,
        //iframe: true,
        beforeSubmit:  CheckInfo,
        success: Submited,
    };
    //alert('START');
    $('#contactForm').ajaxForm(options);
    //alert('END!!!!!!!!!!!');
});
$(document).ajaxStart(function() {
	alert('start ajax');
	$('#contactForm input').attr("disabled", "disabled");
	$('#contactForm textarea').attr("disabled", "disabled");
	//$('#results').html("Sending form data...");

});
$(document).ajaxStop(function() {
	alert('stop ajax');
	$('#contactForm input').removeAttr("disabled");
	$('#contactForm textarea').removeAttr("disabled");
	//$('#results').html("URA!!!!!!!!!!!!!!!!!!!!!!!!!!");
});
function CheckInfo(formData, jqForm, options){
	var queryString = $.param(formData);
	alert('id\n\n' + formData.('#id_photo'));
    alert('About to submit: \n\n' + queryString); 
    return true; 
};

function Submited(response, statusText, xhr, $form){
            alert('success');
            var queryString1 = $.param(response); 
            alert(queryString1);
            /*alert('status: ' + statusText + '\n\nresponseText: \n' + response + 
        '\n\nThe output div should have already been updated with the responseText.');
        $('#results').html('status: ' + statusText + '\n\nresponseText: \n' + response + 
        '\n\nThe output div should have already been updated with the responseText.');*/
            if (response.status=="Ok")
            {
				alert('status ok');
				$('#contactForm').html(response.text);
				alert('form reload');
				//$('#results').html(response.message);
            }
            else
			{
				alert('status fail');
				$('#contactForm').html(response.text);

			}
            
        };