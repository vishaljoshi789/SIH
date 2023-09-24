const ctx = document.getElementById('myChart');

const labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'];
const data = {
  labels: labels,
  datasets: [{
    label: 'Number of Drop Out Students in <City>',
    data: [65, 59, 80, 81, 56, 55, 40,30,55,63,54,40,32],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};

const config = {
    type: 'line',
    data: data,
    options: {
        indexAxis: 'x',
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
  };
new Chart(ctx, config);