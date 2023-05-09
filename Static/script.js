// Event Listener
let RoutineOnbtn = document.getElementById('RoutineOn');
let timeON = document.getElementById("TurnOnTime").value;
let timeOFF = document.getElementById("TurnOffTime").value;

document.getElementById('actions').addEventListener('click', function(event) {
  
  if (event.target.nodeName == "BUTTON") {
    var actionid = event.target.id;        
    
    Routinebtn(actionid);

    FarmBoard(actionid);

    console.log(actionid, timeON,timeOFF,RoutineOnbtn.disabled);    

    SendRequest(actionid,timeON,timeOFF);

    // fetch('/'+actionid+'?id='+actionid+'&timeON='+timeON+'&timeOFF='+timeOFF)
    // .then(function(response) {
    //   if (response.ok) {
    //     return response.json();
    //   }
    //   throw new Error('Network response was not ok.');
    // })
    // .then(function(data) {
    // })
    // .catch(function(error) {
    //   console.log('Fetch error:', error);
    // });
    
    // return false;
  }
    
});

async function SendRequest(actionid,timeON,timeOFF){

  const body = {
    actionid_id:actionid,
    timeON:timeON,
    timeOFF:timeOFF
  }
  
  try{
    const response = await fetch('/'+actionid+'?id='+actionid+'&timeON='+timeON+'&timeOFF='+timeOFF,{method:"POST",body:JSON.stringify(body)});
    console.log(response);
  }
  catch(error){
    console.error(error);
  }
}

function Routinebtn(actionid){
  if(actionid == 'RoutineOn'){
    RoutineOnbtn.disabled = true;
  }
  else{
    RoutineOnbtn.disabled = false;
  }
}

function FarmBoard(actionid){
  const FarmLight = document.querySelectorAll(".circle");
  var FarmIdOn = actionid + 'GreenLight';
  var FarmIdOff = actionid + 'RedLight'; 
  for(let i = 0;i < FarmLight.length; i++){
    if(FarmIdOn == FarmLight[i].id)
    {
      FarmLight[i].classList.add("On");
      FarmIdOff = document.getElementById(FarmIdOn.slice(0,-12) + 'OffRedLight');
      FarmIdOff.classList.remove("Off");
    }
    else if(FarmIdOff == FarmLight[i].id)
    {
      FarmLight[i].classList.add("Off");
      FarmIdOff = document.getElementById(FarmIdOff.slice(0,-11) + 'OnGreenLight');
      FarmIdOff.classList.remove("On");
    };
  }
}