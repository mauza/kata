

function place()
    slot = turtle.getSelectedSlot()
    slot_count = turtle.getItemCount()
    if slot_count == 0 then
        slot = slot + 1
        if slot == 17 then
            print("You are out of building material")
            os.exit()
        end
        turtle.select(slot)
    end
    turtle.placeDown()
end

continuing = true
turning_integer = 0
while continuing do
	while turtle.forward() do
		place()
	end
	if turning_integer % 2 == 0 then
		turn = turtle.turnLeft
	else
		turn = turtle.turnRight
	end
	turn()
	continuing = turtle.forward()
	place()
	turn()
	turning_integer = turning_integer + 1
end
