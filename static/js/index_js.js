$(function(){
    //when u click the police
    $("#citizen_form").hide();
    $("#police_form").hide();
    
    $("#police").click(function(){
        //the form will be visible
        $("#citizen_form").hide();
        $("#police_form").show(); 
        $("#police_form input").jqBootstrapValidation({
    preventSubmit: true,
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var username = $("input#username").val();
      var password = $("input#password").val();

      $this = $("#police_btn");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "././index.php",
        type: "POST",
        data: {
          username: username,
          password: password,
        },
            complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });
    });
    
    //the login button is clicked
    
   

        
               
    
    //when u click on citzen
    $("#citizen").click(function(){
        //form will be visible
        $("#police_form").hide();
        $("#citizen_form").show();
       $("#citizen_form input").jqBootstrapValidation({
    preventSubmit: true,
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var Aadharcardno = $("input#Aadharcardno").val();

      $this = $("#citizen_btn");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "././index.php",
        type: "POST",
        data: {
            Aadharcardno = Aadharcardno,
        },
            complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });
    
    
    $("#citizen_form input").jqBootstrapValidation({
    preventSubmit: true,
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var otpp = $("input#otpp").val();

      $this = $("#otp_btn");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "././index.php",
        type: "POST",
        data: {
            otpp=otpp,
        },
            complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });
    
    
    });
    
    
        
            //the send otp button clicked
                //the flask will get that aadhar card no...usse the phoneno is extracted and the otp will be sent to the phone no. 
            
            //the login button is clicked 
                //the flask will confirm the otp and accordingly sen to next pg orelse send an alert message that the otp entered is wrong
    
});