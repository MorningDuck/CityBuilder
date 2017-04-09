-- the main gameplay state for City Builder
plane = {}

function load()

	love.graphics.setBackgroundColor(70,130,230)
	plane = {
		img = imgPlane,
		X = 200,
		Y = 200}
end

function love.update(dt)

	plane.X = plane.X + (50 * dt)
	plane.Y = plane.Y + (50 * dt)

end


function love.draw(dt)
	love.graphics.draw(plane.img, plane.X,plane.Y)
end


-- use escape key to bring up the menu

function love.keypressed(key)

	if key == "escape" then
		--print("keypress: esc")
		loadState("menu")
		
	end
end