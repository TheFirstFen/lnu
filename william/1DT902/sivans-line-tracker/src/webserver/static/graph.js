function fetchAndDrawGraph() {
    let dropdownMenu = document.getElementById('dropdown');
    let selectedOption = dropdownMenu.options[dropdownMenu.selectedIndex];
    let toDate = selectedOption.value;

    $.ajax({
      url: '/data-history',
      type: 'GET',
      data: { toDate: toDate },
      success: function(data) {
        // Assuming data is an array of values for the graph
        drawGraph(data);
      },
      error: function(error) {
        console.log("Error fetching historical data: ", error);
      }
    });
  }

function drawGraph(data) {
// Assuming data is an array of values, modify as needed
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
    labels: Array.from({ length: data.length }, (_, i) => i + 1),
    datasets: [{
        label: 'Historical Data',
        data: data,
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        fill: false
    }]
    },
    options: {
    scales: {
        x: {
        type: 'linear',
        position: 'bottom'
        },
        y: {
        type: 'linear',
        position: 'left'
        }
    }
    }
});
}