const YearListOption = document.getElementById('year-list');
let yearopt;
const YearList = ()=> {
    console.log('Yearly selection changed');
    yearopt = YearListOption.value;
    if (yearopt === 'Singular-Year'){
        document.getElementById('Range1').classList.add('hidden');
        document.getElementById('Range2').classList.add('hidden');
        document.getElementById('Single0').classList.remove('hidden');
    }
    else if (yearopt === 'Range-Selection'){
        document.getElementById('Range1').classList.remove('hidden');
        document.getElementById('Range2').classList.remove('hidden');
        document.getElementById('Single0').classList.add('hidden');
    }
}
