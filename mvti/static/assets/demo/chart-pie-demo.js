// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["액션", "모험", "애니메이션", "코미디", "범죄", "판타지", "역사", "공포", "음악", "미스터리", "로맨스", "SF", "스릴러", "전쟁"],
    datasets: [{
      data: [12.21, 15.58, 11.25, 8.32, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1],
      backgroundColor: ['#6096B4', '#93BFCF', '#BDCDD6', '#EEE9DA', '#164863', '#427D9D', '#9BBEC8', '#DDF2FD', '#B7C4CF', '#EEE3CB', '#D7C0AE', '#967E76', '#FFB3B3', '#C9BBCF'],
    }],
  },
});
