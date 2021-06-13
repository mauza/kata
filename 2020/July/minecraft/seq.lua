
-- ********************************************************************************** --
-- Global Vars
-- ********************************************************************************** --
direction = { FORWARD=0, RIGHT=1, BACK=2, LEFT=3, UP=4, DOWN=5 }
orientation = { positive_x=0, positive_z=1, negative_x=2, negative_z=3}
local compare_slot = 1
local replace_slot = 2
local fuel_slot = 3
local last_empty_slot = 16
local tries = 11

local position = {x=0, y=0, z=0}
local currOrient = orientation.positive_x

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
        file_write('y', position.y)
    elseif move_direction == direction.DOWN then
        position.y = position.y - 1
        file_write('y', position.y)
    elseif move_direction == direction.FORWARD then
        if currOrient == orientation.positive_x then
            position.x = position.x + 1
            file_write('x', position.x)
        elseif currOrient == orientation.negative_x then
            position.x = position.x - 1
            file_write('x', position.x)
        elseif currOrient == orientation.positive_z then
            position.z = position.z + 1
            file_write('z', position.z)
        elseif currOrient == orientation.negative_z then
            position.z = position.z - 1
            file_write('z', position.z)
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
        file_write('orientation', currOrient)
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
        file_write('orientation', currOrient)
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
    go_to_position(0, 0, 0, orientation.negative_x, {3,1,2})
    for i = 3, last_empty_slot do
        turtle.select(i)
        turtle.drop()
    end
    turtle.select(last_selected_slot)
    go_to_position(last_x, last_y, last_z, last_orient, {2,1,3})
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
    writeMessage("Reading " .. file_name)
    local outputFile = io.open(file_name, 'r')
    value = outputFile:read()
    outputFile:close()
    return value
end

function dig_to_bedrock()
    while Move(direction.DOWN, 1) do end
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

function go_to_position(x, y, z, desired_orient, order)
    x_diff = position.x - x
    y_diff = position.y - y
    z_diff = position.z - z
    x_y_z = {x_diff, y_diff, z_diff}
    for i, index in ipairs(order) do
        current_diff = x_y_z[index]
        magnitude = math.abs(current_diff)
        if current_diff < 0 then
            if index == 1 then
                set_orientation(orientation.positive_x)
                Move(direction.FORWARD, magnitude)
            elseif index == 3 then
                set_orientation(orientation.positive_z)
                Move(direction.FORWARD, magnitude)
            elseif index == 2 then
                Move(direction.UP, magnitude)
            end
        elseif current_diff > 0 then
            if index == 1 then
                set_orientation(orientation.negative_x)
                Move(direction.FORWARD, magnitude)
            elseif index == 3 then
                set_orientation(orientation.negative_z)
                Move(direction.FORWARD, magnitude)
            elseif index == 2 then
                Move(direction.DOWN, magnitude)
            end
        end
    end
    set_orientation(desired_orient)
end

function reset_files()
    file_write('x', '')
    file_write('y', '')
    file_write('z', '')
    file_write('orientation', '')
    file_write('mined_level', '')
    file_write('width', '')
end

function quarry(width, mined_level)
    if not mined_level then
        dig_to_bedrock()
        file_write('mined_level', position.y)
        go_to_position(0, position.y + 3, 0, orientation.positive_x, {3,1,2})
    else
        go_to_position(0, mined_level + 3, 0, orientation.positive_x, {3,1,2})
    end
    while position.y <= -4 do
        mine_one_level(width)
        file_write('mined_level', position.y)
        go_to_position(0, position.y + 3, 0, orientation.positive_x, {3,1,2})
    end
    go_to_position(0, 0, 0, orientation.positive_x, {3,1,2})
    unload()
    reset_files()
end

-- ********************************************************************************** --
-- Main Function
-- ********************************************************************************** --
local args = { ... }

if #args == 0 then
    position.x = tonumber(file_read('x'))
    position.y = tonumber(file_read('y'))
    position.z = tonumber(file_read('z'))
    currOrient = tonumber(file_read('orientation'))
    quarryWidth = tonumber(file_read('width'))
    mined_level = tonumber(file_read('mined_level'))
    if not position.x or not position.y or not position.z or not currOrient or not quarryWidth then
       writeMessage("There is no saved state or it is corrupt")
    else
        quarry(quarryWidth, mined_level)
    end
elseif #args == 1 then
    quarryWidth = tonumber(args[1])
    file_write('width', quarryWidth)
    quarry(quarryWidth)
else
    writeMessage("something is horribly wrong")
end

