
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

local args = { ... }

l = args[1]
w = args[2]
h = args[3]

for z = 1, h, 1 do
    turtle.up()
    for x = 1, l, 1 do
        turtle.forward()
        place()
    end
    turtle.turnLeft()
    for y = 1, w, 1 do
        turtle.forward()
        place()
    end
    turtle.turnLeft()
    for x = 1, l, 1 do
        turtle.forward()
        place()
    end
    turtle.turnLeft()
    for y = 1, w, 1 do
        turtle.forward()
        place()
    end
    turtle.turnLeft()
end