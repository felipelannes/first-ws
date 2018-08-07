function Create_Line_Chart(style, id_canvas, title, date, data){

    /*console.log(mass_property);
    console.log(title);
    console.log(date);
    console.log(data);*/
    var y_label = "";
    var x_label = "";

    var ctx = document.getElementById(id_canvas).getContext('2d');
    var myChart = new Chart(ctx, {
    type: style,
    data: {
        labels: date,
        datasets: [{
            label: title,
            lineTension: 0,
            fill: false,
            steppedLine:false, 
            data: data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255,99,132,1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                scaleLabel: {
                        display: true,
                        labelString: y_label
                }
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{ 
                scaleLabel: {
                    display: true,
                    labelString: x_label
              }
            }]
        }
    }
            })
    return myChart

function Create_Bubble_Chart(id_canvas,data){

    var ctx = document.getElementById(id_canvas);
    var myChart = new Chart(ctx, {
    type: 'bubble',
    data: {
      labels: "LANNESNESN",
      datasets: data [
        {
          label: ["China"],
          backgroundColor: "rgba(255,221,50,0.2)",
          borderColor: "rgba(255,221,50,1)",
          data: [{
            x: 21269017,
            y: 5.245,
            r: 15
          }]
        }, {
          label: ["Denmark"],
          backgroundColor: "rgba(60,186,159,0.2)",
          borderColor: "rgba(60,186,159,1)",
          data: [{
            x: 258702,
            y: 7.526,
            r: 10
          }]
        }, {
          label: ["Germany"],
          backgroundColor: "rgba(0,0,0,0.2)",
          borderColor: "#000",
          data: [{
            x: 3979083,
            y: 6.994,
            r: 15
          }]
        }, {
          label: ["Japan"],
          backgroundColor: "rgba(193,46,12,0.2)",
          borderColor: "rgba(193,46,12,1)",
          data: [{
            x: 4931877,
            y: 5.921,
            r: 15
          }]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      }, scales: {
        yAxes: [{ 
          scaleLabel: {
            display: true,
            labelString: "Happiness"
          }
        }],
        xAxes: [{ 
          scaleLabel: {
            display: true,
            labelString: "GDP (PPP)"
          }
        }]
      }
    }
});

}


   /*<canvas id="Weight_Chart" width="800" height="200" ></canvas>

    <script>
        var ctx = document.getElementById("Weight_Chart");
        var Weigt_Chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Structure", "Propulsion", "Eletrical", "Control", "Aux System"],

            datasets: [{
                label: 'Weight (kg)',
                lineTension: 0,
                fill: false,
                steppedLine:false, 
                data: [{{gs_list.0.1}}, {{gs_list.1.1}}, {{gs_list.2.1}}, {{gs_list.3.1}}, {{gs_list.4.1}}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
        });
        </script>

    <canvas id="LCG_Chart" width="800" height="200" ></canvas>

    <script>
        var ctx = document.getElementById("LCG_Chart");
        var LCG_Chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Structure", "Propulsion", "Eletrical", "Control", "Aux System"],

            datasets: [{
                label: 'LCG (m)',
                lineTension: 0,
                fill: false,
                steppedLine:false, 
                data: [{{gs_list.0.1}}, {{gs_list.1.1}}, {{gs_list.2.1}}, {{gs_list.3.1}}, {{gs_list.4.1}}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
        });
        </script>

    <canvas id="VCG_Chart" width="800" height="200" ></canvas>

    <script>
        var ctx = document.getElementById("VCG_Chart");
        var VCG_Chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Structure", "Propulsion", "Eletrical", "Control", "Aux System"],

            datasets: [{
                label: 'VCG (m)',
                lineTension: 0,
                fill: false,
                steppedLine:false, 
                data: [{{gs_list.0.1}}, {{gs_list.1.1}}, {{gs_list.2.1}}, {{gs_list.3.1}}, {{gs_list.4.1}}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
        });
        </script>*/