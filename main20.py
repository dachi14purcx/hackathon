# შექმენით calculator ფუნქცია რომელსაც ექნება ყველა მათემატიკური მოქმედება მაგალითად:+,-,*,/. ფუნქციას გადაეცით 3 არგუმენტი. პირველი იქნება პირველი რიცხვი, მეორე მეორე რიცხვი და მესამე მათემატიკური ოპერაციის ოპერატორი (+,-...).

def calculator(num1, num2, sign):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "//":
        return num1 // num2
    
print(calculator(int(input("Enter a num1: ")), int(input("Enter a num2: ")), input("Enter a sign: ")))