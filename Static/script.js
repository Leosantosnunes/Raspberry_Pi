// Event Listener
let RoutineOnbtn = document.getElementById('RoutineOn');

document.getElementById('actions').addEventListener('click', function(event) {
  
  if (event.target.nodeName == "BUTTON") {
    var actionid = event.target.id;
    var timeON = document.getElementById("TurnOnTime").value;
    var timeOFF = document.getElementById("TurnOffTime").value;    
    
    if(actionid == 'RoutineOn'){
      RoutineOnbtn.disabled = true;
    }
    else{
      RoutineOnbtn.disabled = false;
    }
    console.log(actionid, timeON,timeOFF,RoutineOnbtn.disabled);
    
    fetch('/'+actionid+'?id='+actionid+'&timeON='+timeON+'&timeOFF='+timeOFF)
    .then(function(response) {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Network response was not ok.');
    })
    .then(function(data) {
      // handle response data here
      console.log(response.status)
    })
    .catch(function(error) {
      console.log('Fetch error:', error);
    });
    
    return false;
  }
  
});