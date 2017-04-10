-- paused state

local pause = {}

function pause:enter()
end


function pause:draw(dt)
	love.graphics.print("Paused",300,300,0,1.5,1.5)
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