// Event Listener

document.getElementById('actions').addEventListener('click', function(event) {

  if (event.target.nodeName == "BUTTON") {
    var actionid = event.target.id;
    var timeON = document.getElementById("TurnOnTime").value;
    var timeOFF = document.getElementById("TurnOffTime").value;
  
    console.log(actionid, timeON,timeOFF);
  
    fetch('/'+actionid+'?id='+actionid+'&timeON='+timeON+'&timeOFF='+timeOFF)
      .then(function(response) {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(function(data) {
        // handle response data here
      })
      .catch(function(error) {
        console.log('Fetch error:', error);
      });
  
    return false;
  }
  
    });