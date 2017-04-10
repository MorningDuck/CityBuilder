-- the main gameplay state for City Builder

local play = {}

local plane = {}
function play:enter()

	love.graphics.setBackgroundColor(70,130,230)
	plane = {
		img = imgPlane,
		X = 200,
		Y = 200}
end

function play:update(dt)

	plane.X = plane.X + (150 * dt)
	plane.Y = plane.Y + (150 * dt)

end


function play:draw(dt)
	love.graphics.draw(plane.img, plane.X,plane.Y)
end


-- use escape key to bring up the menu

function play:keyreleased(key)

	if key == "escape" then
		--print("keypress: esc")
		Gamestate.switch(menu)
		
	elseif key == "space" then
		Gamestate.switch(pause)
		
	end
end

return play