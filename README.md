## Purpose of This Repo
I had a data set "State Level Age Cohorts" by `Female`, `Male`, and `Both`. I put them all on separate sheets but wanted them combined on one sheet in a way that was at least somewhat readable.

### State Name's Three Ways.js
Has an array of all state names with FCT-Abuja last. It loops through and prints out the state name followed by Female, Male, or Both with a newline after each.


### ReferToStates.js
Takes an array with the line numbers of the states' first lines. Loops through to give you the reference for all three lines for that state, then skips a line.

### StateArrays.js
An index of our common state arrangements (Sharia, Zones, Etc.). Abuja-FCT is last.

### AdjustToSheet.js
Depending on the sheet you're using, Abia probably won't start on Row 1. Use this script to adjust them. It transforms the array to the new scheme.