var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const myObj = JSON.parse(this.responseText);
    
    //World
    document.getElementById("world_cases").innerHTML = (myObj.COVID19.World.COVID19Cases);
    document.getElementById("world_deads").innerHTML = (myObj.COVID19.World.Deaths + ' (' + myObj.COVID19.World.DeathRate + '%)');
    document.getElementById("world_recovered").innerHTML = (myObj.COVID19.World.Recoveries + ' (' + myObj.COVID19.World.RecoveredRate + '%)' );
    document.getElementById("world_active").innerHTML = (myObj.COVID19.World.ActiveCases);
    document.getElementById("world_condition").innerHTML = (myObj.COVID19.World.MildCondition) + ' (' + myObj.COVID19.World.ConditionRate + '%)';
    document.getElementById("world_critical").innerHTML = (myObj.COVID19.World.SeriousOrCritical + ' (' + myObj.COVID19.World.CriticalRate + '%)');

    
    //Brazil
    document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Brazil.COVID19Cases);
    document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Brazil.Deaths + ' (' + myObj.COVID19.Brazil.DeathRate + '%)');
    document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Brazil.Recoveries + ' (' + myObj.COVID19.Brazil.RecoveredRate + '%)' );
    document.getElementById("brazil_active").innerHTML = (myObj.COVID19.Brazil.ActiveCases);
    document.getElementById("brazil_condition").innerHTML = (myObj.COVID19.Brazil.MildCondition) + ' (' + myObj.COVID19.Brazil.ConditionRate + '%)';
    document.getElementById("brazil_critical").innerHTML = (myObj.COVID19.Brazil.SeriousOrCritical + ' (' + myObj.COVID19.Brazil.CriticalRate + '%)');

    var dating = myObj.COVID19.Update.LastUpdate;
    console.log(dating)
    //document.getElementById("last_updatexd").innerHTML = dating;

    document.getElementById("lup").innerHTML = dating;
    //console.log(myObj.COVID19.Update.LastUpdate);
    
      
    
 }
};
xmlhttp.open("GET", "https://covid19search.herokuapp.com/", true);
xmlhttp.send();


