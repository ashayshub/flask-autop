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
        $('.modal-body p').text('Populating... it may take 10-15 seconds');
        var saveData = $.ajax({
              type: 'POST',
              url: "/populate/",
              success: function(resultData){
                   printToModal(modal_title, resultData);
                   location.href = "/";
              }
        });
        saveData.error(function() {
              printToModal(modal_title, 'Error: Something went wrong while populating data');
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
                   printToModal(modal_title, resultData);
              }
        });
        saveData.error(function() {
              printToModal(modal_title, "Error: Something went wrong while dropping table");
        });
     });

    $("[id^=price-info-]").click(function(){
        var modal_title = "Vehicle Price";
        var price_query = $(this).data("price-query");
        $('.modal-title').text(modal_title);
        $('.modal-body p').text('Fetching price for vehicle...');
        var saveData = $.ajax({
              type: 'GET',
              url: "/price?price_query=" + encodeURIComponent(price_query),
              success: function(resultData){
                   body_text = "Base price of the vehicle is $" + resultData.baseMSRP;
                   printToModal(modal_title, body_text);
              }
        });
        saveData.error(function() {
              printToModal(modal_title, 'Error: Work in progresss');
        });
     });
});

