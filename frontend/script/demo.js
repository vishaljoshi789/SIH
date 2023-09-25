let chart_data = [];
let City, Year, Subject, Filter;
const InputList = {
    "City": ['Haldwani','Nainital','Bhimtal','Mukteshwar','Bhowali'],
    "Subject": ['Age', 'Gender', 'School', 'Grade'],
    "Gender": ['Male','Female', 'Others'],
    "School": ['Inspiration senior secondary school','Cynthia senior secondary school','KVM public school','Doon public school','Beersheba senior secondary school','Gurukul international school'],
    
}
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