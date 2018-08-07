
function Create_Bubble_Chart(id_canvas,data,group){
    var data = JSON.parse(data);
    data = data[group];
    console.log(group);
    var ctx = document.getElementById(id_canvas);
    var myChart = new Chart(ctx, {
    type: 'bubble',
    data: {
      datasets: data 
    },
    options: {
      legend: {display:false},
      title: {
        display: true,
        text: 'Center of Gravity of group '+group
      }, scales: {
        yAxes: [{ 
          scaleLabel: {
            display: true,
            labelString: "VCG"
          }
        }],
        xAxes: [{ 
          scaleLabel: {
            display: true,
            labelString: "LCG"
          }
        }]
      },
    tooltips: {
         callbacks: {
            label: function(t, d) {
               var rLabel = d.datasets[t.datasetIndex].data[0].r;
               console.log(rLabel);
               return d.datasets[t.datasetIndex].label + 
                      ': (LCG:' + t.xLabel + ', VCG:' + t.yLabel + ', Mass: ' + rLabel*4+')';

    }}}
}});

}