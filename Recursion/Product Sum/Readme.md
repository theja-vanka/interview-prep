Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

For example, the product sum of **[x, y]** is **x + y**; the product sum of **[x, [y, z]]** is **x + 2y + 2z**.

Example:<br>
Input:<br>
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]<br>
Output:<br>
12 // Calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)