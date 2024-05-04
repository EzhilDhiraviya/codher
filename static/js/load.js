document.addEventListener("DOMContentLoaded", function() {
    // Show loader
    var loader = document.querySelector('.loader');
    loader.style.display = 'block';
  
    // Hide loader and show content after 2 seconds
    setTimeout(function() {
      loader.style.display = 'none';
      document.getElementById('content').style.display = 'block';
    }, 2000);
  });
  