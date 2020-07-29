

function dig_forward()
    turtle.dig()
    turtle.forward()
end

for i = 1, 10000000 do
    dig_forward()
end