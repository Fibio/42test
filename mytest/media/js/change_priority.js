$(document).ready(function(){
	$('#inc').click(function(){
		Change(1);
	});
	$('#dec').click(function(){
		Change(-1);
	});
});

function CheckInfo(data){
	$('#results').css({color: "blue"});
	$('#results').show()
	$('#results').html("Sending data...")
	
};

function AfterInc(response){
	if (response['result']=="OK")
	{
        $("span").each(function (i) {
        	this.innerHTML = response[this.id];
        });
        $('#results').html("The priority was changing")
		$('#results').hide(1600)
    }
    else
	{
		GetErr(response);
    }
};

function GetErr(data){
	$('#results').css({color: "red"});
	$('#results').html("The priority wasn't changing. Try again")
};

function Change(inc){
	$.ajax({
		type: "POST",
        url: "/request/",
        data:{'inc': inc},
        dataType: "json",
        beforeSend:  CheckInfo,
        success: AfterInc,
        error:GetErr,
        });
};
