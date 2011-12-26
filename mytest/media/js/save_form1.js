$(document).ready(function(){
  $('#send').click(function(){
    $.ajax({
      url: '/get_post/',
      data: {'email':'test@gmail.com'},      
      dataType: "json",
                        type:"POST",
      success: function(data, textStatus){
        alert('есть ответ');  
        alert(data["email"]);
      }
    });
  });
});


$(document).ready(function(){
    var options = {
        dataType: 'json',
        beforeSubmit: function(){
            $.blockUI({ fadeIn: 200, message: "Please wait, loading data"});
        },
        success: function(response){
            $.unblockUI();
            if (response.status=="ok")
            {
$('#form').html(response.text);
$('#form_save').show(response.message);
$('#form_save').html(response.message);
$('#form_save').hide(1600);
            }
            else
{
$('#form').html(response.text);

}
            $("#id_date_of_birth").datepicker({dateFormat: 'yy-mm-dd'});
        }
    };
    $.datepicker.setDefaults(
        $.extend($.datepicker.regional["ru"])
    );
    $("#id_date_of_birth").datepicker({
        dateFormat: 'yy-mm-dd'
    });
    $('#myForm').ajaxForm(options);
});