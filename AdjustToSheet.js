// This adjusts the state index to fit into our specific Excel sheet
// You'll need to figure out the formula for adjustment. Use your maths
states = [];

for(i = 0; i < states.length; i++){
	states[i] = states[i] * 4 - 1;
};
