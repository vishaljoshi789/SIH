let chart_data = [];
let City, Year, Subject, Filter;
const City_dom = document.getElementById('City');
const Year_dom = document.getElementById('Year');
const Subject_dom = document.getElementById('Subject');
graph_data = HALDWANI.map((i) => {
    return i;
})
const getData = () => {
    let num = 0;
    graph_data = HALDWANI.map((i) => {
        if (i[Subject_dom] in graph_data) { 
            chart_data[0].append(i[Subject_dom]);
        }
        return i;
    })
    
}
getData();