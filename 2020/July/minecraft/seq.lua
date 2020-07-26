

-- ********************************************************************************** --
-- Global Vars
-- ********************************************************************************** --
direction = { FORWARD=0, RIGHT=1, BACK=2, LEFT=3, UP=4, DOWN=5 }



function Down()
    check_and_add_fuel()
    local attempts = 0
    while turtle.down() == false do
        turtle.digDown()
        turtle.attackDown()
        attempt = attempt + 1
        if attempt >= 10 then
            stuck()
        end
    end
end

function Up()
    check_and_add_fuel()
    local attempts = 0
    while turtle.up() == false do
        turtle.digUp()
        turtle.attackUp()
        attempt = attempt + 1
        if attempt >= 10 then
            stuck()
        end
    end
end

function Forward()
    check_and_add_fuel()
    local attempts = 0
    while turtle.forward() == false do
        turtle.dig()
        turtle.attack()
        attempt = attempt + 1
        if attempt >= 10 then
            stuck()
        end
    end
end

function Back()
    check_and_add_fuel()
    if turtle.back() == false then
        turtle.turnRight()
        turtle.turnRight()
        tfd()
        turtle.turnRight()
        turtle.turnRight()
    end
end

function compare(side)

end

function check_and_add_fuel()
    local fuel_level = turtle.getFuelLevel()
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

function dig_to_bedrock(position)

end

function quarry(width, position)
    currOrient = direction.FORWARD
    position = dig_to_bedrock(position)
    while position.y <= -4 do
        position = move_up_to_next_level()
        position = mine_one_level(width, position)
    end
    return_to_start()
end

-- ********************************************************************************** --
-- Main Function
-- ********************************************************************************** --
local args = { ... }

quarryWidth = tonumber(args[1])

position = {x=0, y=0, z=0}
quarry(quarryWidth, position, bottomLayer)
