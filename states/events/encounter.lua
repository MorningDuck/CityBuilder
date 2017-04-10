-- an event in which a villager speaks to the player

local encounter = {}

function encounter:enter()
end
	
function encounter:draw(dt)
	love.graphics.print("Hello there!",200,200,.5,2,2)
end

return encounter