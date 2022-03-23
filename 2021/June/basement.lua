
direction = { FORWARD=0, RIGHT=1, BACK=2, LEFT=3, UP=4, DOWN=5 }
local last_empty_slot = 16

function ensure_inventory_space()
    if turtle.getItemCount(last_empty_slot) > 0 then
        for i = 1, last_empty_slot do
            turtle.select(i)
            turtle.drop()
        end
    end
    turtle.select(1)
end

function Attack(side)
    local result = false
    if side == direction.UP then
        result = turtle.attackUp()
    elseif side == direction.DOWN then
        result = turtle.attackDown()
    elseif side == direction.FORWARD then
        result = turtle.attack()
    end
    return result
end

function Move(move_direction, times)
    local move = turtle.forward
    local detect = turtle.detect
    if move_direction == direction.UP then
        move = turtle.up
        detect = turtle.detectUp
    elseif move_direction == direction.DOWN then
        move = turtle.down
        detect = turtle.detectDown
    end
    times = times or 1
    for i = 1, times, 1 do
        while not move() do
            if detect() then
                if not Dig(move_direction) then
                    return false
                end
            elseif Attack(move_direction) then
                while Attack(move_direction) do end
            end
        end
    end
    return true
end

function Dig(side)
    local result = false
    ensure_inventory_space()
    if side == direction.UP then
        result = turtle.digUp()
    elseif side == direction.DOWN then
        result = turtle.digDown()
    elseif side == direction.FORWARD then
        result = turtle.dig()
    end
    return result
end


local args = { ... }

l = tonumber(args[1])
w = tonumber(args[2])
h = tonumber(args[3])

turtle.select(1)
current_x = 0

while current_x <= w do
    for x = 1, l, 1 do
        Move(direction.DOWN, h)
        Move(direction.UP, h)
        Move(direction.FORWARD, 1)
    end
    if current_x % 2 == 0 then
        turtle.turnLeft()
        Move(direction.FORWARD, 1)
        turtle.turnLeft()
    else
        turtle.turnRight()
        Move(direction.FORWARD, 1)
        turtle.turnRight()
    end
    current_x = current_x + 1
end