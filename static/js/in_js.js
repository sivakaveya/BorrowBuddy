$(function(){
    //when u click the police
    $("#citizen_form").hide();
    $("#police_form").hide();
    
    $("#police").click(function(){
        //the form will be visible
        $("#citizen_form").hide();
        $("#police_form").show();
        $("#citizen").css({
            'background-color':'rgba(0,0,0,0.5)'
        });
        $(this).css("background","rgba(246, 246, 217, 0.5)");
    });
    
    $("#citizen").click(function(){
        //the form will be visible
        $("#citizen_form").show();
        $("#police_form").hide();
        $("#police").css('background-color',"rgba(0, 0, 0, 0.5)");
        $(this).css("background","rgba(246, 246, 217, 0.5)");
    });
});