function printToModal(data) {
   $('.modal-body p').text(data);
   $('#myModal').modal('show');
   location.href = "/";
   return true;
}

function template_map(type, data){
   $("#catTemplate").tmpl(data).appendTo("#table-"+type);
}

$(document).ready(function() {
    event.preventDefault();

    $("#populate").click(function(){
        $('.modal-body p').text('Populating... it may take 5-10 seconds');
        var saveData = $.ajax({
              type: 'POST',
              url: "/populate/",
              success: function(resultData){
                   printToModal(resultData);
              }
        });
        saveData.error(function() { printToModal('Error: Something went wrong while populating data') });
    });

    $("#teardown").click(function(){
        $('.modal-body p').text('Tearing down...');
        var saveData = $.ajax({
              type: 'DELETE',
              url: "/teardown/",
              success: function(resultData){
                   printToModal(resultData);
              }
        });
        saveData.error(function() { printToModal("Error: Something went wrong while dropping table"); });
    });

});
