-- the Menu state for City Builder (gamesStates branch)

local menu = {}

function menu:enter()
	
	love.graphics.setBackgroundColor(20,200,150)

end

function menu:update(dt)

end
	

local function drawButtons(x, y, width, height)
	
	love.graphics.draw(imgMenu, 150, 150)
end

function menu:draw(dt)
	drawButtons()

-- use for loop with ipairs to iterate through multiple buttons
end

function love.keyreleased(key)

	if key == "space" then
		Gamestate.switch(play)
	end
end

return menu