google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var adr = parseFloat(document.getElementById("adr").value);
  var monthly = parseInt(document.getElementById("monthly").value);
  var cost = parseFloat(document.getElementById("cost").value);
  var direct = parseInt(document.getElementById("direct").value);
  var channels = parseInt(document.getElementById("channels").value);
  var roomCount = parseInt(document.getElementById("roomCount").value);

  var revenue = monthly * adr;
  var occupancy = (monthly / (30 * roomCount)).toFixed(2);
  var expenses = cost + (monthly - direct) * (adr * occupancy) + channels * (adr * occupancy);
  var profit = revenue - expenses;

  var data = google.visualization.arrayToDataTable([
    ['Element', 'Cost', { role: 'style' }],
    ['Revenue', revenue, 'color: #4CAF50'],
    ['Expenses', expenses, 'color: #F44336'],
    ['Profit', profit, 'color: #2196F3']
  ]);

  var options = {
    title: 'ROI Chart',
    width: 600,
    height: 400,
    bar: { groupWidth: '75%' },
    legend: { position: 'none' }
  };

  var chart = new google.visualization.BarChart(document.getElementById('chart'));

  chart.draw(data, options);
}
