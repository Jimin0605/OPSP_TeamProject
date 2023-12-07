// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["액션", "모험", "애니메이션", "코미디", "범죄", "다큐멘터리", "드라마", "가족", "판타지", "역사", "공포", "음악", "미스터리", "로맨스", "SF", "스릴러", "전쟁", "서부"],
    datasets: [{
      data: [12.21, 15.58, 11.25, 8.32, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#123456', '#234567', '#345678', '#456789', '#567890', '#678901', '#789012', '#890123', '#901234', '#012345', '#123456', '#234567', '#345678', '#456789'],
    }],
  },
});
