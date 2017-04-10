-- the Menu state for City Builder

local menu = {}

local buttonX 	= 300
local playY 	= 200
local quitY 	= 350

function menu:enter()
	
	love.graphics.setBackgroundColor(20,200,150)

end

-- boolean: is (mx, my) in the parameters?
local function inBox(x,y,width,height,mx,my)

	inbox = false
	
	if mx > x and mx < x + width and my > y and my < y + height then
		inbox = true
	end
	
	return inbox
end

local function drawButtons()

	mx, my = love.mouse.getPosition()
	
	-- Draw the "hover" versions of menu buttons when the mouse is over them
	if inBox(buttonX,playY,imgPlay:getWidth(),imgPlay:getHeight(),mx,my) then
		love.graphics.draw(imgPlayHover,buttonX,playY) -- mouse hover
		love.graphics.draw(imgQuit,buttonX,quitY)		-- default
		
	elseif inBox(buttonX,quitY,imgQuit:getWidth(),imgQuit:getHeight(),mx,my) then
		love.graphics.draw(imgPlay,buttonX,playY) --default
		love.graphics.draw(imgQuitHover,buttonX,quitY) -- mouse hover version
	else
		-- default menu buttons
		love.graphics.draw(imgPlay,buttonX,playY)
		love.graphics.draw(imgQuit,buttonX,quitY)
	end

end

function menu:draw(dt)
	drawButtons()
end

function menu:mousereleased(mx,my)

	if inBox(buttonX,playY,imgPlay:getWidth(),imgPlay:getHeight(),mx,my) then
		Gamestate.switch(play)
	end
	
	if inBox(buttonX,quitY,imgQuit:getWidth(),imgQuit:getHeight(),mx,my) then
		love.event.quit()
	end
end

function menu:keyreleased(key)

	-- this should return from the menu to the previous gamestate
	if key == "escape" then
		Gamestate.switch(play)
	end
end

return menu