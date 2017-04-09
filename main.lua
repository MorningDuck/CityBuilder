-- City Builder\main.lua --> the root-level file
state = {}


function loadState(name)

	local path = "states/"..name
	m = require(path)
	load()

end

function love.load()
	-- load game textures here
	imgMenu = love.graphics.newImage("states/assets/menu.png")
	imgPlane = love.graphics.newImage("states/assets/plane.png")
	imgChicken = love.graphics.newImage("states/assets/birbdog.png")
	
	-- load game with splash screen as initial game state
	loadState("splash")
end


function love.keypressed(key)
	--if key == "d" then
	--	debug.debug()
	--end

end