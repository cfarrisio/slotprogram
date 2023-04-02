google.charts.load('current', {packages: ['corechart']});

document.getElementById("reservation-form").addEventListener("submit", function(event) {
  event.preventDefault();

  var adr = parseFloat(document.getElementById("adr").value);
  var monthly = parseFloat(document.getElementById("monthly").value);
  var cost = parseFloat(document.getElementById("cost").value);
  var direct = parseFloat(document.getElementById("direct").value);
  var channels = parseFloat(document.getElementById("channels").value);
  var occupancy = parseFloat(document.getElementById("occupancy").value);

  if (isNaN(adr) || isNaN(monthly) || isNaN(cost) || isNaN(direct) || isNaN(channels) || isNaN(occupancy)) {
    document.getElementById("results").innerHTML = "Please enter valid input for all fields.";
    document.getElementById("chart").innerHTML = "";
    document.getElementById("chart2").innerHTML = "";
  } else {
    document.getElementById("results").innerHTML = "";

    var data = google.visualization.arrayToDataTable([
      ['Category', 'Value', { role: 'style' }],
      ['ADR', adr, '#21827c'],
      ['Monthly Reservations', monthly, '#21827c'],
      ['Cost of Current System', cost, '#21827c'],
      ['Number of Direct Reservations', direct, '#21827c'],
      ['Number of Booking Channels', channels, '#21827c'],
      ['Occupancy Rate', occupancy, '#21827c']
    ]);

    var options = {
      chartArea: { width: '50%' },
      hAxis: {
        title: 'Value',
        minValue: 0
      },
      vAxis: {
        title: 'Category'
      },
      legend: { position: 'none' }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart'));
    chart.draw(data, options);

    var data2 = google.visualization.arrayToDataTable([
      ['Opportunity Areas', 'Impact'],
      ['Marketing and Distribution', 2],
      ['Pricing', 1],
      ['Revenue Management', 1],
      ['Operations', 3],
      ['Technology', 3]
    ]);

    var options2 = {
      chartArea: { width: '50%' },
      legend: { position: 'none' }
    };

    var chart2 = new google.visualization.PieChart(document.getElementById('chart2'));
    chart2.draw(data2, options2);

    document.getElementById("charts").style.display = "block";
  }
});
