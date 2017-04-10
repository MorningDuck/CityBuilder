-- splash screen

local splash = {}

function splash:enter()

	love.graphics.setBackgroundColor(200,50,50)
end

function splash:update(dt)

end


function splash:draw(dt)
	love.graphics.draw(imgSplash,100,100)
end


-- use escape key to bring up the menu

function splash:keyreleased(key)

	if key == "escape" then
		--print("keypress: esc")
		Gamestate.switch(menu)
		
	end
end

return splash