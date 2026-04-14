# Dungeons & Cards

## Repository
[<Link to your project's public GitHub respository>](https://github.com/dillionx13/PFDA-Final-Project)

## Description
This is going to be a card game where you use cards against creatures, inspired by DnD. This relates to media and digital arts as it will be an interactive game.

## Features
- Turn-based combat
	- The player and the enemy take turns playing cards or taking actions. This will most likely use a loop to continuously swap whose turn it is.
- Card Zones
	- The card zones will most likely be the deck of cards and the hand where the player can use the cards after drawing them. This will most likely use a list to contain and move each card.
- Energy System
	- A simple energy system that allows cards to be played if the player has enough energy (probably being related to spell-slots or charges). This will most likely use a variable and if statements.
- Health
   	- This would keep track how much damage a player can take/deal before losing/winning. This will most likely use a variable.
- Cards
  	- Cards will contain information and visuals to be played. This may use class objects or dictionaries.
 
## Challenges
- I need to research more into pygame module for multiple features such as images, music, inputs, and displays.
- I need to look more into graphic design for the gameplay.
- I need to look into code logic and flow more in order to make the game flow properly without much confusion.

## Outcomes
Ideal Outcome:
- The ideal outcome would be a playable game where the player is able to fight against creatures in multiple stages. Within each stage, the player and the enemy will take turns using cards from a deck to deal damage to each other untill their hp is 0. After each stage, the player would gain points depending on their hp and regain hp a little, winning at the end of the last stage and displaying their points.

Minimal Viable Outcome:
- Minimally, the game should have at least a single playable fight, where the player has a drawable deck and the enemy attacks with set moves. The cards just need to be clear on what they do without any type of visual images. The player just needs to be able to win if the enemy reaches 0 hp and lose when they reach 0 hp.

## Milestones

- Week 1
  1. Create a menu display
  2. Basic game structure

- Week 2
  1. Create game loop logic
  2. Implement controls for interactions
  3. Implement visual for players to recognize hand, enemy, and energy.

- Week 3 (Final)
  1. Implement stages with winning and losing
  2. Implement sounds and card images
  3. Finalize visual interactions in the game (such as menu, playing cards, etc.)
