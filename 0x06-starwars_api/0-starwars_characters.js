#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/';
const FILM_ID = argv[2];
async function printStarWarsCharacters() {
  request(BASE_URL + FILM_ID, async function (error, response, body) {
    if (error) {
      console.log(error);
    }
    body = JSON.parse(body);
    const characters = body.characters;
    for (const i of characters) {
      request(i, function (error, response, body) {
        if (error) {
          console.log(error);
        }
        body = JSON.parse(body);
        console.log(body.name);
      });
    }
  });
}

printStarWarsCharacters();
