const delay = 5000; // milliseconds

setInterval(function() {
    $.ajax({
        url: '/get_updates',
        type: 'GET',
        success: function(data){
            document.getElementById('length').innerText = data['length'] // displays the line length in the line div
            document.getElementById('date').innerText = ("Uppdaterades: " + data['date']); // displays the date in the date div
        },
        error: function(error) {
            console.log("Error fetching data: ", error);
        }
    });
}, delay);
