-- the Menu state for City Builder

local menu = {}

local playButton = {
					x = 300,
					y = 200,
					img = imgPlay,
					width = imgPlay:getWidth(),
					height = imgPlay:getHeight()}
					
local quitButton = {
					x = 300,
					y = 350,
					img = imgQuit,
					width = imgQuit:getWidth(),
					height = imgQuit:getHeight()}

function menu:enter()

	state = 'menu'
	
	love.graphics.setBackgroundColor(20,200,150)

end

function menu:update(dt)

end

function menu:draw(dt)
	love.graphics.draw(playButton.img,playButton.x,playButton.y)
	love.graphics.draw(quitButton.img,quitButton.x,quitButton.y)
end

-- boolean: is the mouse in the play button?
local function inBox(x,y,width,height,mx,my)

	inbox = false
	
	if mx > x and mx < x + width and my > y and my < y + height then
		inbox = true
	end
	
	return inbox
end

function menu:mousereleased(x,y)

	if inBox(playButton.x, playButton.y,playButton.width,playButton.height,x,y) then
		Gamestate.switch(play)
	end
end

function menu:keyreleased(key)

	-- this should return from the menu to the previous gamestate
	if key == "escape" then
		Gamestate.switch(play)
	end
end

return menu