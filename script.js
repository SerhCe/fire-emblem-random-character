let globalDataJson = null; // Global variable to store the fetched data
let filterDataJson = null; // Json for filtered data

async function loadHeroes() 
{ 
    const dataJson = await fetch('csvjson.json')
    const response = await dataJson.json();

    console.log(response);
    return response;
}

async function start() {
    globalDataJson = await loadHeroes(); // Load data and store it in the global variable
    console.log("Loaded data."); // Use the data
    randomCharacter();
}

window.onload = start;


function randomCharacter() 
{
    const characterName = document.getElementById("characterName");
    const game = document.getElementById("game");

    filterBehaviour();

    const randomIndex = Math.floor(Math.random() * Object.keys(filterDataJson).length);
    const randomEntry = filterDataJson[randomIndex];

    const jsonId = randomEntry.id;
    const jsonCharId = randomEntry.CharId;
    const jsonGameId = randomEntry.GameId; 
    const jsonGame = randomEntry.Game; 
    const jsonIsMale = randomEntry.IsMale;
    const jsonIsFemale = randomEntry.isFemale;
    
    characterName.innerHTML = jsonCharId;
    game.innerHTML = jsonGame; 
}

function filterBehaviour()
{
    filterDataJson = globalDataJson;
    const gameFilter = parseInt(document.getElementById("gameFilter").value);
    const maleCharactersFilter= document.getElementById("MaleCharactersFilter").checked;
    const femaleCharactersFilter= document.getElementById("FemaleCharactersFilter").checked;

    //game Filter logic:
    if (gameFilter != 0) {
        filterDataJson = filterDataJson.filter(entry => entry.GameId === gameFilter);
    }

    if (!maleCharactersFilter) {
        filterDataJson = filterDataJson.filter(entry => entry.isMale === 0)
    }

    if (!femaleCharactersFilter) {
        filterDataJson = filterDataJson.filter(entry => entry.isFemale === 0)
    }

}