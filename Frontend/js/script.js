var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const myObj = JSON.parse(this.responseText);
    
    //World
    document.getElementById("world_cases").innerHTML = (myObj.COVID19.World.COVID19Cases);
    document.getElementById("world_deads").innerHTML = (myObj.COVID19.World.Deaths);
    document.getElementById("world_dead_rate").innerHTML = (myObj.COVID19.World.DeathRate + '%');
    document.getElementById("world_recovered").innerHTML = (myObj.COVID19.World.Recoveries);
    document.getElementById("world_recovered_rate").innerHTML = (myObj.COVID19.World.RecoveredRate + '%');
    
    //Brazil
    document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Brazil.COVID19Cases);
    document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Brazil.Deaths);
    document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Brazil.DeathRate) + '%';
    document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Brazil.Recoveries);
    document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Brazil.RecoveredRate) + '%';
    
    function getSelectValue() {
      var selectedValue = document.getElementById("estado").value;
      console.log(selectedValue)
      return selectedValue;
    }
      document.getElementById("sdados").addEventListener("click", function() {
        selectedValue = getSelectValue();
        console.log('clicando')

      if (selectedValue == 'brazil')
      {
        console.log('kkk');
        document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Brazil.COVID19Cases);
        document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Brazil.Deaths);
        document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Brazil.DeathRate) + '%';
        document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Brazil.Recoveries);
        document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Brazil.RecoveredRate) + '%';
      }
      if (selectedValue == 'bahia_brazil')
      {
        console.log('kkk2')
        document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Bahia.COVID19Cases);
        document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Bahia.Deaths);
        
        if (myObj.COVID19.Bahia.DeathRate == '-'){
          document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Bahia.DeathRate);
        }
        else {
          document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Bahia.DeathRate) + '%';
        }
       
        document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Bahia.Recoveries);
        
        if (myObj.COVID19.Bahia.RecoveredRate == '-'){
          document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Bahia.RecoveredRate);
        }
        else {
          document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Bahia.RecoveredRate) + '%';
     
        }
        
    }
          if (selectedValue == 'pernambuco_brazil')
          {
            console.log('kkk2')
            document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Pernambuco.COVID19Cases);
            document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Pernambuco.Deaths);
    
            if (myObj.COVID19.Pernambuco.DeathRate == '-') {
              document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Pernambuco.DeathRate);
            }
            else {
              document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Pernambuco.DeathRate) + '%';
            }
    
            document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Pernambuco.Recoveries);
    
            if (myObj.COVID19.Pernambuco.RecoveredRate == '-') {
              document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Pernambuco.RecoveredRate);
            }
            else {
              document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Pernambuco.RecoveredRate) + '%';
        }
    }
          
      if (selectedValue == 'sopaulo_brazil')
      {
        console.log('kkk2')
        document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.SaoPaulo.COVID19Cases);
        document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.SaoPaulo.Deaths);
      
        if (myObj.COVID19.SaoPaulo.DeathRate == '-') {
          document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Pernambuco.DeathRate);
        }
        else {
          document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.SaoPaulo.DeathRate) + '%';
        }
      
        document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.SaoPaulo.Recoveries);
      
        if (myObj.COVID19.SaoPaulo.RecoveredRate == '-') {
          document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.SaoPaulo.RecoveredRate);
        }
        else {
          document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.SaoPaulo.RecoveredRate) + '%';
        }
        
      }
    if (selectedValue == 'riodejaneiro_brazil')
    {
      console.log('kkk2')
      document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.RiodeJaneiro.COVID19Cases);
      document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.RiodeJaneiro.Deaths);
    
      if (myObj.COVID19.RiodeJaneiro.DeathRate == '-') {
        document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.RiodeJaneiro.DeathRate);
      }
      else {
        document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.RiodeJaneiro.DeathRate) + '%';
      }
    
      document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.RiodeJaneiro.Recoveries);
    
      if (myObj.COVID19.RiodeJaneiro.RecoveredRate == '-') {
        document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.RiodeJaneiro.RecoveredRate);
      }
      else {
        document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.RiodeJaneiro.RecoveredRate) + '%';
    
     }
    }
    /*
    document.getElementById("idhora").innerHTML = (myObj.COVID19.World.LastUpdated);
    console.log(myObj.COVID19.World.LastUpdated)
     */ 
     horario = (myObj.COVID19.World.LastUpdated);
     var d = new Date(horario)
     console.log(d);
     var d = new Date(2018, 11, 24, 10, 33, 30);
     
 });
    
 }
};
xmlhttp.open("GET", "https://covid19search.herokuapp.com/", true);
xmlhttp.send();


