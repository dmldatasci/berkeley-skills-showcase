# VBA Grade Book

In this activity, you will create a macro that checks a student’s numerical grade, assigns them a letter grade, and applies formatting changes to a cell that depend on the value of the grade.

## Instructions

With `grader.xlsm` as your starting point, create a grade calculator that uses conditionals. This calculator will convert a student's numerical grade into a letter grade and then style the resulting cell accordingly.

Your grade calculator script should do the following:

* If the score is greater than or equal to 85:
  * Add an "A" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the colour green.
  * Add the text "Pass" to the Pass/Warning/Fail cell.

* If the score is between 70 and 84 (inclusive):
  * Add a "B" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the colour green.
  * Add the text "Pass" to the Pass/Warning/Fail cell.
  **Note:** The inclusive number range means that a score up to 84.9 stays in the "B" grade range and doesn't get rounded up.

* If the score is between 50 and 69 (inclusive):
  * Add a "C" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the colour yellow.
  * Add the text "Warning" to the Pass/Warning/Fail cell.

* If the score is less than 50:
  * Add an "F" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the colour red.
  * Add the text "Fail" to the Pass/Warning/Fail cell.

## Bonus

Create a second button that resets the grades to their original state and then establishes the previous grade in a row that's labelled "Last Grade".

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
