var states = [];

// Get's all three entries for a state
for( var i = 0; i < states.length;i++){
    var multiLine = states[i];
    for(var x = 0; x <= 2; x++){
        var multiLine = states[i] + x;
        console.log("=Combined!A"+ multiLine);
    }
    console.log("\r")
};

