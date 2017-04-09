-- splash screen

function load()

	love.graphics.setBackgroundColor(200,50,50)
end

function love.update(dt)

end


function love.draw(dt)
	love.graphics.draw(imgChicken,10,10)
end


-- use escape key to bring up the menu

function love.keypressed(key)

	if key == "escape" then
		--print("keypress: esc")
		loadState("menu")
		
	end
end