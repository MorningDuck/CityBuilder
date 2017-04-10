-- City Builder\main.lua --> the root-level file



Gamestate = require("states/gamestate")

menu = require("states/menu")
play = require("states/play")

local splash = require("states/splash")

function love.load()
	-- load game textures here
	imgMenu = love.graphics.newImage("states/assets/menu.png")
	imgPlane = love.graphics.newImage("states/assets/plane.png")
	imgSplash = love.graphics.newImage("states/assets/splash.png")
	
	-- load game with splash screen as initial game state
	Gamestate.registerEvents()
	Gamestate.switch(menu)
end

-- function menu:draw(dt)
	-- love.graphics.draw(imgMenu)
-- end

-- function love.keypressed(key)

	-- if key == "escape" then
		-- Gamestate.switch(menu)
	-- end
	
-- end