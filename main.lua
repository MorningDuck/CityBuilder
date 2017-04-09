-- City Builder\main.lua --> the root-level file
state = {}

function clearLoveCallbacks()

	love.draw = nil
	love.load = nil
	love.load = nil
	love.mousereleased = nil
	love.mousepressed = nil
	love.keypressed = nil
end

function loadState(name)

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