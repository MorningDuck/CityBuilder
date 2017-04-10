-- paused state

local pause = {}

function pause:enter()
	state = 'pause'

end

function pause:update(dt)


end


function pause:draw(dt)
	--love.graphics.draw(plane.img, plane.X,plane.Y)
end

function pause:keyreleased(key)

	if key == "escape" then
		--print("keypress: esc")
		Gamestate.switch(menu)
		
	elseif key == "space" then
		Gamestate.switch(play)
		
	end
end


return pause