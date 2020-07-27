

-- ********************************************************************************** --
-- Global Vars
-- ********************************************************************************** --
direction = { FORWARD=0, RIGHT=1, BACK=2, LEFT=3, UP=4, DOWN=5 }
orientation = { positive_x=0, positive_z=1, negative_x=2, negative_z=3}
local compare_slot = 1
local replace_slot = 2
local fuel_slot = 16
local tries = 11

local position = {x=0, y=0, z=0}
local currOrient = orientation.positive_x

function Down()
    while not turtle.down() do
        if turtle.detectDown() then
            if not turtle.digDown() then
                return false
            end
        elseif turtle.attackDown() then
            while turtle.attackDown() do end
        elseif turtle.getFuelLevel() == 0 then
            add_fuel()
        end
    end
    position.y = position.y - 1
    return true
end

function Up()
    while not turtle.up() do
        if turtle.detectUp() then
            if not turtle.digUp() then
                return false
            end
        elseif turtle.attackUp() then
            while turtle.attackUp() do end
        elseif turtle.getFuelLevel() == 0 then
            add_fuel()
        end
    end
    position.y = position.y + 1
    return true
end

function Forward()
    while not turtle.forward() do
        if turtle.detect() then
            if not turtle.dig() then
                return false
            end
        elseif turtle.attack() then
            while turtle.attack() do end
        elseif turtle.getFuelLevel() == 0 then
            add_fuel()
        end
    end
    calc_position()
    return true
end

function calc_position()
    if currOrient == orientation.positive_x then
        position.x = position.x + 1
    elseif currOrient == orientation.negative_x then
        position.x = position.x - 1
    elseif currOrient == orientation.positive_z then
        position.z = position.z + 1
    elseif currOrient == orientation.negative_z then
        position.z = position.z - 1
    end
end

function Back()
    turn_right(2)
    tfd()
    turn_right(2)
end

function turn_left(times)
    times = times or 1
    for i = 1, times, 1 do
        if not turtle.turnLeft() then
            add_fuel()
            turtle.turnLeft()
        end
        if currOrient == 0 then
            currOrient = 3
        end
        currOrient = currOrient - 1
    end
end

function turn_right(times)
    times = times or 1
    for i = 0, times, 1 do
        if not turtle.turnRight() then
            add_fuel()
            turtle.turnRight()
        end
        if currOrient == 3 then
            currOrient = 0
        end
        currOrient = currOrient + 1
    end
end

function set_orientation(desired_orient)
    orient_diff = currOrient - desired_orient
    if math.abs(orient_diff) == 2 then
        turn_right(2)
    elseif orient_diff == -3 or orient_diff == -1 then
        turn_left()
    elseif orient_diff == -1 or orient_diff == 3 then
        turn_right()
    end
end

function place(side)
    local dig = turtle.dig
    local attack = turtle.attack
    local place_item = turtle.place
    turtle.select(replace_slot)
    if side == direction.UP then
        dig = turtle.digUp
        attack = turtle.attackUp
        place_item = turtle.placeUp
    elseif side == direction.DOWN then
        dig = turtle.digDown
        attack = turtle.attackDown
        place_item = turtle.placeDown
    end
    local attempt = 0
    while place_item() == false do
        dig()
        attack()
        attempt = attempt + 1
        if attempt >= tries then
            return false
        end
    end
    return true
end

function compare_and_replace(side)
    local starting_orient = currOrient
    local ini_slot = turtle.getSelectedSlot()
    turtle.select(compare_slot)
    if side == direction.UP then
        compare_result = turtle.compareUp()
    elseif side == direction.DOWN then
        compare_result = turtle.compareDown()
    elseif side == direction.FORWARD then
        compare_result = turtle.compare()
    elseif side == direction.LEFT then
        turn_left()
        compare_result = turtle.compare()
    elseif side == direction.RIGHT then
        turn_right()
        compare_result = turtle.compare()
    elseif side == direction.BACK then
        turn_right(2)
        compare_result = turtle.compare()
    end
    if compare_result == false then
        place(side)
    end
    set_orientation(starting_orient)
    turtle.select(ini_slot)
end

function add_fuel()
    local ini_slot = turtle.getSelectedSlot()
    turtle.select(fuel_slot)
    fuel_count = turtle.getItemCount()
    if fuel_count > 1 then
        turtle.refuel(fuel_count - 1)
    end
end

function writeMessage(message)
    print(message)
end

function file_write(file_name, value)
    local outputFile = io.open(file_name, 'w')
    outputFile:write(value)
    outputFile:close()
end

function file_read(file_name)
    local outputFile = fs.open(file_name, 'r')
    return outputFile.readLine()
end

function dig_to_bedrock()
    while Down() do

    end
end

function move_up_to_next_level()
    for i = 1, 3 do
        Up()
    end
end

function mine_one_level(width)
    for i = 1, width do
        for i = 1, width do
            Forward()
            compare_and_replace(direction.UP)
            compare_and_replace(direction.DOWN)
        end
        if position.x == 0 then
            turn_left()
            Forward()
            turn_left()
        else
            turn_right()
            Forward()
            turn_right()
        end
    end
end

function back_to_initial_hole()
    if position.x < 0 then
        set_orientation(orientation.positive_x)
    else
        set_orientation(orientation.negative_x)
    end
    if position.z < 0 then
        set_orientation(orientation.positive_z)
    else
        set_orientation(orientation.negative_z)
    end
    for i = 1, math.abs(position.x) do
        Forward()
    end
    for i = 1, math.abs(position.z) do
        Forward()
    end
    set_orientation(orientation.positive_x)
end

function return_to_start()
    back_to_initial_hole()
    while position.y < 0 do
        Up()
    end
end

function quarry(width)
    dig_to_bedrock()
    while position.y <= -4 do
        move_up_to_next_level()
        mine_one_level(width)
        back_to_initial_hole()
    end
    return_to_start()
end

-- ********************************************************************************** --
-- Main Function
-- ********************************************************************************** --
local args = { ... }

quarryWidth = tonumber(args[1])

quarry(quarryWidth)

