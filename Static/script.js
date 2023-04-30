let lightOn = document.getElementById("LightOn");
let lightOff = document.getElementById("LightOff");

// Event Listener

document.getElementById('actions').addEventListener('click', function(event) {

    if (event.target.nodeName == "BUTTON") {

      var tar = event.target.id;

      console.log(tar);

      $.getJSON('/'+tar,

          function(data) {

        //do nothing

      });

      return false;

    }

  });

  document.getElementById('shutdown').addEventListener('click', function(event) {

    if (event.target.nodeName == "BUTTON") {

      var tar = event.target.id;

      console.log(tar);

      $.getJSON('/'+tar,

          function(data) {

        //do nothing

      });

      return false;

    }

  });