let heroesData = null; 

async function loadHeroes() 
{ 
    const data = await fetch('Heroes.json')
    const response = await data.json();

    console.log(response)
}

function randomCharacter() 
{
    var characterName = document.getElementById("characterName");
    var game = document.getElementById("game");
    var randnr = Math.random();
    var randjson = getRandomChar();
    characterName.innerHTML = "test"+randnr;
    game.innerHTML = "Game!!"+randjson;
}


function getRandomChar() 
{
    const keys = Object.keys(jsonObject);
    const randomKey = keys[Math.floor(Math.random() * keys.length)];
    const randomValue = jsonObject[randomKey];
    
    return heroesData.find(hero => hero.charid == 1);
}


loadHeroes();