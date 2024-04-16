#!/usr/bin/node
const util = require('node:util');
const request = util.promisify(require('request'));
const argv = process.argv;
const FILM_ID = argv[2];
async function printStarWarsCharacters (filmId) {
  const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/';
  try {
    let response = await (await request(BASE_URL + filmId)).body;
    response = JSON.parse(response);
    const characters = response.characters;

    for (const i of characters) {
      const characterUrl = i;
      let character = await (await request(characterUrl)).body;
      character = JSON.parse(character);
      console.log(character.name);
    }
  } catch (error) {}
}

printStarWarsCharacters(FILM_ID);
