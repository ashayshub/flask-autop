function printToModal(data) {
   $('.modal-body p').text(data);
   $('#myModal').modal('show');
   return true;
}
//
//function listCarsInfo(year, car_type){
//    var listData = $.ajax({
//           type: 'GET',
//           url: "/api/cars?year="+year+"&type="+car_type,
//           success: function(resultData){
//                alert(resultData);
//                $('#custom').text(resultData);
//           }
//    });
//    listData.error(function() { printToModal("Error: Something went wrong while listing cars"); });
//}

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

//    var d = new Date();
//    truck_data = listCarsInfo(d.getFullYear(), 'Truck');
//    sport_data = listCarsInfo(d.getFullYear(), 'Sport');
//    template_map('Truck', truck_data);
//    template_map('Sport', sport_data);
});
