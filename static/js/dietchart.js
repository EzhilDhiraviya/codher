// Sample data for categories
var categories = ['Protein', 'Carbs', 'Fats', 'Vitamins', 'Minerals'];
  
// Sample values for each category (in grams)
var values = [80, 200, 50, 30, 20];

// Generate a random color for each category
var colors = values.map(function() {
  return '#' + Math.floor(Math.random()*16777215).toString(16);
});

// Chart configuration
var config = {
  type: 'doughnut',
  data: {
    labels: categories,
    datasets: [{
      label: 'Nutrient Intake (grams)',
      data: values,
      backgroundColor: colors,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
};

// Create the chart
var ctx = document.getElementById('dietChart').getContext('2d');
new Chart(ctx, config);