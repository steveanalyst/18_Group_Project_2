function simpleChart(entry) {
    d3.json(`/data/${entry}`).then((data) => {
        console.log(entry);

        var basic = d3.select('#state-data')

        basic.html("");

        Object.entries(data).forEach(([key, value]) => {
            basic.append("h6").text(`${key}: ${value}`);
        });
    });
};

function init() {
    var selector = d3.select("#selState");

    d3.json('/states').then((stateNames) => {
        stateNames.forEach((state) => {
            selector
                .append("option")
                .text(state)
                .property("value", state);
        });

        const firstState = stateNames[0];
        simpleChart(firstState);

    });
};

function optionChanged(newState) {
    simpleChart(newState);
};

init();