# List-Comphrension-Example

Description
In a school, there are total 20 students numbered from 1 to 20. You’re given three lists named ‘C’, ‘F’, and ‘H’, representing students who play cricket, football, and hockey, respectively. Based on this information, find out and print the following: 
Students who play all the three sports
Students who play both cricket and football but don’t play hockey
Students who play exactly two of the sports
Students who don’t play any of the three sports
Format:
Input:
3 lists containing numbers (ranging from 1 to 20) representing students who play cricket, football and hockey respectively.
Output:
4 different lists containing the students according to the constraints provided in the questions.

Note: Make sure you sort the final lists (in an ascending order) that you get before printing them; otherwise your answer might not match the test-cases.

Examples:
Input 1:
[2, 5, 9, 12, 13, 15, 16, 17, 18, 19]\n
[2, 4, 5, 6, 7, 9, 13, 16]\n
[1, 2, 5, 9, 10, 11, 12, 13, 15]\n
Output 1:
[2, 5, 9, 13]
[16]
[12, 15, 16]
[3, 8, 14, 20]

Explanation:
1.Given the three sets, you can see that the students numbered '2', '5', '9', and '13' play all the three sports. 
2. The student numbered '16' plays cricket and football but doesn't play hockey. 
3. The student numbered '12' and '15' plays cricket and hockey and the student numbered '16' plays cricket and football. There are no students who play only football and hockey. Hence, the students who play exactly two sports are 12, 15, and 16.
4. As you can see, the students who play none of the sports are 3, 8, 14, and 20.
