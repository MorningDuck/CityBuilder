-- City Builder\main.lua --> the root-level file



Gamestate = require("states/gamestate")

menu = require("states/menu")
play = require("states/play")
pause = require("states/pause")

state = ''

local splash = require("states/splash")


function love.load()
	-- load game textures here
	imgPlay = love.graphics.newImage("assets/playButton.png")
	imgQuit = love.graphics.newImage("assets/exitButton.png")
	imgPlane = love.graphics.newImage("assets/plane.png")
	imgSplash = love.graphics.newImage("assets/splash.png")
	
	-- load game with splash screen as initial game state
	Gamestate.registerEvents()
	Gamestate.switch(splash)
end