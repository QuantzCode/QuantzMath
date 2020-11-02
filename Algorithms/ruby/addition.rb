puts "Enter the numbers you are going to add:"
a = gets.chomp()
b = 0
while a > 0
    puts "Please enter a number:"
    c = gets.chomp()
    b += c
end
puts("The answer is " + b)