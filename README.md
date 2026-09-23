Build a Travel Weather Planner<br>
For this lab, you will use conditional statements to determine whether commuting is possible based on the weather, the distance to travel, and the availability of a vehicle.<br>

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.<br>

User Stories:<br>

You should create the following variables:.<br>
distance_mi (a number representing the distance to travel in miles).<br>
is_raining (a boolean representing if the user is currently experiencing rainy weather).<br>
has_bike (a boolean representing if the user has a bicycle).<br>
has_car (a boolean representing if the user has a car).<br>
has_ride_share_app (a boolean representing if the user has an app that allows them to request a ride).<br>
You should use conditional statements to determine whether commuting is possible based on the values of these variables.<br>
You should use if, elif, and else statements to evaluate the distance categories in ascending order.
If distance_mi is a falsy value:.<br>
You should print False..<br>
If the distance is less than or equal to 1 mile:.<br>
You should print True only if it is not raining..<br>
Otherwise, you should print False..<br>
If the distance is greater than 1 mile and less than or equal to 6 miles:.<br>
You should print True only if the person has a bike and it is not raining..<br>
Otherwise, you should print False..<br>
If the distance is greater than 6 miles:.<br>
You should print True if the person has a car or has a ride-share app..<br>
Otherwise, you should print False..<br>
Tests:.<br>
1. You should have a variable named distance_mi.
2. You should assign a number to your distance_mi variable.
3. You should have a variable named is_raining.
4. You should assign a boolean to your is_raining variable.
5. You should have a variable named has_bike.
6. You should assign a boolean to your has_bike variable.
7. You should have a variable named has_car.
8. You should assign a boolean to your has_car variable.
9. You should have a variable named has_ride_share_app.
10. You should assign a boolean to your has_ride_share_app variable.
11. You should use at least one if statement.
12. You should use at least one elif branch in your program.
13. You should use at least one boolean operator (and, or, or not) in your code.
14. You should use the print() function to display the result.
15. When distance_mi is a falsy value, the program should print False.
16. When the distance is 1 mile or less and it is not raining, the program should print True.
17. When the distance is 1 mile or less and it is raining, the program should print False.
18. When the distance is between 1 mile (excluded) and 6 miles (included), and it is raining with no bike, the program should print False.
19. When the distance is between 1 mile (excluded) and 6 miles (included), it is not raining but no bike is available, the program should print False.
20. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is not raining, the program should print True.
21. When the distance is greater than 6 miles and a ride share app is available, the program should print True.
22. When the distance is greater than 6 miles and a car is available, the program should print True.
23. When the distance is greater than 6 miles and no car nor a ride share app is available, the program should print False.
