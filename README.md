## Purpose of This Repo
I had a data set "State Level Age Cohorts" by `Female`, `Male`, and `Both`. I put them all on separate sheets but wanted them combined on one sheet in a way that was at least somewhat readable.

### nigeria_state_datasets.py
Contains all the states organized together, as zones, and as sharia both as lists and as dictionaries.

### State_Names_Three_Ways.py
Has an array of all state names with FCT-Abuja last. It loops through and prints out the state name followed by Female, Male, or Both with a newline after each.


### ReferToStates.js
Takes an array with the line numbers of the states' first lines. Loops through to give you the reference for all three lines for that state, then skips a line.

### State_Arrays.py
An index of our common state arrangements (Sharia, Zones, Etc.). Abuja-FCT is last.

### AdjustToSheet.js
Depending on the sheet you're using, Abia probably won't start on Row 1. Use this script to adjust them. It transforms the array to the new scheme.