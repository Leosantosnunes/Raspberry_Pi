// Event Listener
let RoutineOnbtn = document.getElementById('RoutineOn');
let timeON = document.getElementById("TurnOnTime").value;
let timeOFF = document.getElementById("TurnOffTime").value;
const FarmLight = document.querySelectorAll(".circle");
let actions = document.getElementById('actions');
let raspPibtn = document.getElementById('raspPibtn');

actions.addEventListener('click', function(event) {
  
  if (event.target.nodeName == "BUTTON") {
    var actionid = event.target.id;        
    
    Routinebtn(actionid);    
    
    FarmBoard(actionid)
    
    console.log(actionid, timeON,timeOFF,RoutineOnbtn.disabled);    
    var url= '/'+actionid+'?id='+actionid+'&timeON='+timeON+'&timeOFF='+timeOFF;
    SendRequest(actionid,url);    
  }
  
});

async function SendRequest(actionid,url){
  
  const body = {
    actionid_id:actionid,
    timeON:timeON,
    timeOFF:timeOFF
  }
  
  try{
    const response = await fetch(url,{method:"POST",body:JSON.stringify(body)});
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

async function Farm_Response(){
  try{
    const response = await fetch('/farmboard');
    const data = await response.json();
    console.log(data);
    FarmBoardWindow(data);
  }
  catch(error){
    console.error(error);
  }
}

function FarmBoardWindow(actionid){
  for(value in actionid){
    if(actionid[value] == true){
      var FarmId = value + 'GreenLight';
      for(let i = 0;i < FarmLight.length; i++){
        if(FarmId == FarmLight[i].id)
        {
          GreenLight(i,FarmId);
        }
      }
    }    
  }
}

window.addEventListener("load",Farm_Response);  

function FarmBoard(actionid){  
  var FarmIdOn = actionid + 'GreenLight';
  var FarmIdOff = actionid + 'RedLight'; 
  
  for(let i = 0;i < FarmLight.length; i++){
    if(FarmIdOn == FarmLight[i].id)
    {
      GreenLight(i,FarmIdOn);
    }
    else if(FarmIdOff == FarmLight[i].id)
    {
      RedLight(i,FarmIdOff);
    }
  }  
}

function GreenLight(i,action){
  FarmLight[i].classList.add("On");
  FarmIdOff = document.getElementById(action.slice(0,-12) + 'OffRedLight');
  FarmIdOff.classList.remove("Off");
}

function RedLight(i,action){
  FarmLight[i].classList.add("Off");
  FarmIdOff = document.getElementById(action.slice(0,-11) + 'OnGreenLight');
  FarmIdOff.classList.remove("On");
}

raspPibtn.addEventListener('click', function(event) {
  
  if (event.target.nodeName == "BUTTON") {
    var RPiactionid = event.target.id;

    console.log(RPiactionid);    
    
    var url= '/'+RPiactionid;
    SendRequest(RPiactionid,url);    
  }
  
});