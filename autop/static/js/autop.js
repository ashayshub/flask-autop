function printToModal(data) {
   $('.modal-body p').text(data);
   $('#myModal').modal('show');
   return true;
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
                   location.href = "/";
              }
        });
        saveData.error(function() {
              printToModal('Error: Something went wrong while populating data')
        });
    });

    $("#teardown").click(function(){
        $('.modal-body p').text('Tearing down...');
        var saveData = $.ajax({
              type: 'DELETE',
              url: "/teardown/",
              success: function(resultData){
                   printToModal(resultData);
                   location.href = "/";
              }
        });
        saveData.error(function() {
              printToModal("Error: Something went wrong while dropping table");
        });
    });

});
