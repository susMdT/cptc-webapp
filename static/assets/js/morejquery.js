/*
$(document).ready(function() {
    $('#userRegButton').click(function() {
      $.when($.postJSON($SCRIPT_ROOT + '/register', {
        username: $('#username').val(),
        password: $('#password').val(),
        email: $('#email').val()
      }))
      $.get("/balls"), function(data, status){
        alert("Data: " + data);
      }
      return false;
    });
  });
  */
  $(document).ready(function() {
    $('#registration').submit(function(e) {
      e.preventDefault();
      var form = $(this);
      $.ajax({
        type:'POST',
        url: 'http://192.168.1.105:5000/api/register',
        cache: false,
        data:{
          'username': $('#username').val(),
          'password': $('#password').val(),
          'email': $('#email').val()
        },
        success: function(){
          alert("Success!");
        },
        error: function(){
          alert("Something went wrong!");
        }
      });
    });
    
  });

  function bruh(){
    let uid = prompt("Please enter a user id number to look up");
      $.ajax({
        type:'POST',
        url: 'http://192.168.1.105:5000/api/lookup',
        cache: false,
        data:{
          'UID': uid
        },
        success: function(){
          alert("We have a Wrlder number " + uid + "!");
        },
        error: function(data){
          alert(data.responseText);
        }
      });
  }