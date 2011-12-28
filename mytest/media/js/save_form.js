$(document).ready(function(){
    var options = {
        dataType: 'json',
        beforeSubmit:  CheckInfo,
        success: Submited
    };
    $('#contactForm').ajaxForm(options);

});
$(document).ajaxStart(function() {
	$('#contactForm input').attr("disabled", "disabled");
	$('#contactForm textarea').attr("disabled", "disabled");
});
$(document).ajaxStop(function() {
	$('#contactForm input').removeAttr("disabled");
	$('#contactForm textarea').removeAttr("disabled");
});
function CheckInfo(formData, jqForm, options){
	$('.errorlist').remove();
	$('#results').css({color: "red"});
};

function Submited(response, statusText, xhr, $form){
            if (response.status=="Ok")
            {
				if (response.response_text != "Empty")
				{
					$('#contactForm .img').html(response.response_text);
				}
				$('#results').css({color: "blue"});
				$('#results').html('Information updated');
            }
            else
			{
                for (var i=0, count=response.errors.length; i<count; i++) {
                    var error = response.errors[i];
                    var err = '<div class=errorlist>' + error[1] + '</div>';
                    $('input[name='+error[0]+']').after(err);
                }
				$('#results').html('Fix errors and submit again');
			}
            
        };