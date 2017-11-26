function printToModal(title, data) {
   $('.modal-title').text(title);
   $('.modal-body p').text(data);
   $('#myModal').modal('show');
   return true;
}


$(document).ready(function() {
    event.preventDefault();

    $("#populate").click(function(){
        var modal_title = "Populate Database";
        $('.modal-title').text(modal_title);
        $('.modal-body p').text('Populating... it may take 5-10 seconds');
        var saveData = $.ajax({
              type: 'POST',
              url: "/populate/",
              success: function(resultData){
                   printToModal(this.modal_title, resultData);
                   location.href = "/";
              }
        });
        saveData.error(function() {
              printToModal('Error: Something went wrong while populating data')
        });
    });

    $("#teardown").click(function(){
        var modal_title = "Drop table";
        $('.modal-title').text(modal_title);
        $('.modal-body p').text('Tearing down...');
        var saveData = $.ajax({
              type: 'DELETE',
              url: "/teardown/",
              success: function(resultData){
                   printToModal(this.modal_title, resultData);
                   location.href = "/";
              }
        });
        saveData.error(function() {
              printToModal("Error: Something went wrong while dropping table");
        });
    });

});
