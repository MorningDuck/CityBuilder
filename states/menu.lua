-- the Menu state for City Builder (gamesStates branch)

function load()
	
	love.graphics.setBackgroundColor(20,200,150)
	
	--imgMenu = love.graphics.newImage("City Builder/assets/menu.png")

end

function love.update(dt)

end
	

local function drawButtons(x, y, width, height)
	
	love.graphics.draw(imgMenu, 150, 150)
end

function love.draw(dt)
	drawButtons()

-- use for loop with ipairs to iterate through multiple buttons
end

function love.keypressed(key)

	if key == "escape" then
		
		loadState("gameplay")
	end
end