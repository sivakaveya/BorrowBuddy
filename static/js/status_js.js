$(function(){
    
   /* $("#online_form").css({
        'opacity' : '1'
    });*/
    
    
    
    var progress = {{ status }};
    var num_pro = 0;
    
    if(progress=="form"){  //if the form is submitted
        view("#online_form");
        num_pro=19;
    }else if(progress=="viewed"){
        view("#online_form");
        view("#view");
        num_pro=39;
    }else if(progress=="verified"){
        view("#online_form");
        view("#view");
        view("#verify");
        num_pro=59;
    }else if(progress=="registered"){
        view("#online_form");
        view("#view");
        view("#verify");
        view("#register");
        num_pro=79;
    }else if(progress=="case_closed"){
        view("#online_form");
        view("#view");
        view("#verify");
        view("#register");
        view("#case_close");
        num_pro=99;
    }
    
    $("#progress").progressbar({
                   value: 0
               });
    var x =0;
    
        $("#label").text("In progress ....");
                    
        setTimeout(function(){
        var progress = setInterval(function(){
            x++;
            $("#label").text(x+ "%");
            $("#progress").progressbar("option","value",x);
            if(x>num_pro){
                clearInterval(progress);
            }
        },100);
        },1000);
    
    
    function view(y){
       $(y).css("opacity","1");
    };
});