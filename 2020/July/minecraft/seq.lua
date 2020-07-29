
-- ********************************************************************************** --
-- Global Vars
-- ********************************************************************************** --
direction = { FORWARD=0, RIGHT=1, BACK=2, LEFT=3, UP=4, DOWN=5 }
orientation = { positive_x=0, positive_z=1, negative_x=2, negative_z=3}
local compare_slot = 1
local replace_slot = 2
local fuel_slot = 16
local tries = 11
local last_empty_slot = 15

local position = {x=0, y=0, z=0}
local currOrient = orientation.positive_x

function Move(move_direction, times)
    writeMessage("moving " .. move_direction)
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
            elseif turtle.getFuelLevel() == 0 then
                add_fuel()
            end
        end
        calc_position(move_direction)
    end
    return true
end

function calc_position(move_direction)
    if move_direction == direction.UP then
        position.y = position.y + 1
    elseif move_direction == direction.DOWN then
        position.y = position.y - 1
    elseif move_direction == direction.FORWARD then
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
    writeMessage(position.x .. ' - ' .. position.y .. ' - ' .. position.z)
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
        else
            currOrient = currOrient - 1
        end
    end
end

function turn_right(times)
    times = times or 1
    for i = 1, times, 1 do
        if not turtle.turnRight() then
            add_fuel()
            turtle.turnRight()
        end
        if currOrient == 3 then
            currOrient = 0
        else
            currOrient = currOrient + 1
        end
    end
end

function set_orientation(desired_orient)
    orient_diff = currOrient - desired_orient
    if math.abs(orient_diff) == 2 then
        turn_right(2)
    elseif orient_diff == -3 or orient_diff == 1 then
        turn_left()
    elseif orient_diff == -1 or orient_diff == 3 then
        turn_right()
    end
end

function ensure_inventory_space()
    writeMessage("ensuring inventory has room")
    if turtle.getItemCount(last_empty_slot) > 0 then
        unload()
    end
end

function unload()
    writeMessage("unloading inventory")
    local last_x = position.x
    local last_y = position.y
    local last_z = position.z
    local last_orient = currOrient
    local last_selected_slot = turtle.getSelectedSlot()
    go_to_position(0, 0, 0, orientation.negative_x)
    for i = 3, last_empty_slot do
        turtle.select(i)
        turtle.drop()
    end
    turtle.select(last_selected_slot)
    go_to_position(last_x, last_y, last_z, last_orient)
end

function Dig(side)
    writeMessage("digging")
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

function Attack(side)
    writeMessage("attacking")
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

function Place(side)
    writeMessage("placing")
    local result = false
    if side == direction.UP then
        result = turtle.placeUp()
    elseif side == direction.DOWN then
        result = turtle.placeDown()
    elseif side == direction.FORWARD then
        result = turtle.place()
    end
    return result
end

function ensure_place(side)
    turtle.select(replace_slot)
    local attempt = 0
    while not Place(side) do
        Dig(side)
        Attack(side)
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
        ensure_place(side)
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
    turtle.select(ini_slot)
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
    while Move(direction.DOWN, 1) do end
end

function move_up_to_next_level()
    for i = 1, 3 do
        Move(direction.UP, 1)
    end
end

function mine_one_level(width)
    for i = 1, width + 1 do
        if i ~= 1 then
            if position.x == 0 then
                turn_left()
                Move(direction.FORWARD, 1)
                compare_and_replace(direction.UP)
                compare_and_replace(direction.DOWN)
                turn_left()
            else
                turn_right()
                Move(direction.FORWARD, 1)
                compare_and_replace(direction.UP)
                compare_and_replace(direction.DOWN)
                turn_right()
            end
        end
        for i = 1, width do
            Move(direction.FORWARD, 1)
            compare_and_replace(direction.UP)
            compare_and_replace(direction.DOWN)
        end
    end
end

function go_to_position(x, y, z, desired_orient)
    x_diff = position.x - x
    y_diff = position.y - y
    z_diff = position.z - z
    writeMessage("differences: " .. x_diff .. " " .. y_diff .. " " .. z_diff)
    if x_diff < 0 then
        set_orientation(orientation.positive_x)
        Move(direction.FORWARD, math.abs(x_diff))
    elseif x_diff > 0 then
        set_orientation(orientation.negative_x)
        Move(direction.FORWARD, math.abs(x_diff))
    end
    if z_diff < 0 then
        set_orientation(orientation.positive_z)
        Move(direction.FORWARD, math.abs(z_diff))
    elseif z_diff > 0 then
        set_orientation(orientation.negative_z)
        Move(direction.FORWARD, math.abs(z_diff))
    end
    if y_diff < 0 then
        Move(direction.UP, math.abs(y_diff))
    elseif y_diff > 0 then
        Move(direction.DOWN, math.abs(y_diff))
    end
    set_orientation(desired_orient)
end

function quarry(width)
    writeMessage("Starting to mine")
    dig_to_bedrock()
    while position.y <= -4 do
        move_up_to_next_level()
        mine_one_level(width)
        go_to_position(0, position.y, 0, orientation.positive_x)
    end
    go_to_position(0, 0, 0, orientation.positive_x)
end

-- ********************************************************************************** --
-- Main Function
-- ********************************************************************************** --
local args = { ... }

quarryWidth = tonumber(args[1])

quarry(quarryWidth)
