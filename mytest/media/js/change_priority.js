var results; 


$(document).ready(function(){
	$("#requests").tablesorter();
	results = $('#results');
	$('#but button').click(function(){
		CheckInfo(this.value);
	});
});


function SendInfo(data){
	GetMsg("Sending data...", "#0025FF");
};


function PostSuccess(response, sts){
	var msg = response['msg'];
	if (response['result']=="OK")
	{
        delete response['result'];
        delete response['msg'];
        var req = $('.priority');
        $.each(response, function(key, value) {
        	var priority = $('#'+key).find(req);
			priority.text(value);
            });
        GetMsg(msg, "blue");
        var check = $('input[type=checkbox]')
        check.attr('checked', false);
        $("#requests").tablesorter();
    }
    else
    {
	GetMsg(msg, "red");
    }
};


function GetMsg(msg, clr){
	results.show();
	results.css({color: clr});
	results.html(msg)
	if (clr == "blue"){results.hide(2000);};
};


function CheckInfo(inc){
	var new_p = $('#p_val').val();
	if (new_p == ''){
		GetMsg("Enter new priority value", "red");
		}
	else {
		var check = $('input[type=checkbox]')
		if (check.is(':checked')) {
            var checked = check.filter(':checked');
  			Change(inc, new_p, checked);
 	        }
        else { GetMsg("Select at least one request", "red");}
	}
};


function Change(inc, new_p, checked){
	var lst = Array();
    checked.each(function() {
    	lst.push($(this).val());
    	});
    $.ajax({
		traditional: true,
		type: "POST",
        url: "/request/",
        data:{'inc': inc, 'new_p': new_p, 'lst': lst},
        dataType: "json",
        beforeSend:  SendInfo,
        success: PostSuccess,
        error: GetMsg,
     	});
};
