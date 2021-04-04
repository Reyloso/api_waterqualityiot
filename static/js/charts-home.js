$(document).ready(function () {

    'use strict';

    Chart.defaults.global.defaultFontColor = '#75787c';


    // ------------------------------------------------------- //
    // Line Chart
    // ------------------------------------------------------ //
    var legendState = true;
    if ($(window).outerWidth() < 576) {
        legendState = true;
    }

    var LINECHART = $('#lineCahrt');
    var myLineChart = new Chart(LINECHART, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 60,
                        min: 10
                    },
                    display: true,
                    gridLines: {
                        display: false
                    }
                }]
            },
            legend: {
                display: legendState
            }
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Turbidez Acueducto Monteria",
                    fill: true,
                    lineTension: 0.2,
                    backgroundColor: "transparent",
                    borderColor: '#864DD9',
                    pointBorderColor: '#864DD9',
                    pointHoverBackgroundColor: '#864DD9',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 5,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [20, 27, 20, 35, 30, 40, 33, 25, 39],
                    spanGaps: false
                },
                {
                    label: "Turbidez Acueducto Cereté",
                    fill: true,
                    lineTension: 0.2,
                    backgroundColor: "transparent",
                    borderColor: "#EF8C99",
                    pointBorderColor: '#EF8C99',
                    pointHoverBackgroundColor: "#EF8C99",
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 5,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    data: [25, 17, 28, 25, 33, 27, 30, 33, 27],
                    spanGaps: false
                }
            ]
        }
    });



    // ------------------------------------------------------- //
    // Bar Chart
    // ------------------------------------------------------ //
    // var BARCHARTEXMPLE    = $('#barChartExample1');
    var barChartExample = new Chart(BARCHARTEXMPLE, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        color: '#eee'
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        color: '#eee'
                    }
                }]
            },
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Ph Monteria",
                    backgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    hoverBackgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    borderColor: [
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)"
                    ],
                    borderWidth: 1,
                    data: [65, 59, 80, 81, 56, 55, 40],
                },
                {
                    label: "Ph Cereté",
                    backgroundColor: [
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)"
                    ],
                    hoverBackgroundColor: [
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)"
                    ],
                    borderColor: [
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)"
                    ],
                    borderWidth: 1,
                    data: [35, 40, 60, 47, 88, 27, 30],
                }
            ]
        }
    });


    // ------------------------------------------------------- //
    // Line Chart 1
    // ------------------------------------------------------ //
    var LINECHART1 = $('#lineChart1');
    var myLineChart = new Chart(LINECHART1, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 40,
                        min: 10,
                        stepSize: 0.1
                    },
                    display: false,
                    gridLines: {
                        display: false
                    }
                }]
            },
            legend: {
                display: true
            }
        },
        data: {
            labels:["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Conductividad Cereté",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "transparent",
                    borderColor: '#EF8C99',
                    pointBorderColor: '#EF8C99',
                    pointHoverBackgroundColor: '#EF8C99',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "#EF8C99",
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 0,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [20, 21, 25, 22, 24, 18, 20, 23, 19, 22, 25, 19, 24 ],
                    spanGaps: false
                },
                {
                    label: "Conductividad Monteria",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "transparent",
                    borderColor: 'rgba(134, 77, 217, 0.57)',
                    pointBorderColor: 'rgba(134, 77, 217, 0.57)',
                    pointHoverBackgroundColor: 'rgba(134, 77, 217, 0.57)',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "rgba(134, 77, 217, 0.57)",
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 0,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [24, 20, 23, 19, 22, 20, 25, 21, 23, 19, 21, 23, 19],
                    spanGaps: false
                }
            ]
        }
    });


    // ------------------------------------------------------- //
    // Bar Chart
    // ------------------------------------------------------ //
    var BARCHARTEXMPLE    = $('#barChartExample2');
    var barChartExample = new Chart(BARCHARTEXMPLE, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        color: '#eee'
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        color: '#eee'
                    }
                }]
            },
        },
        data: {
            labels:  ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Temperatura Monteria",
                    backgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    hoverBackgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    borderColor: [
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)"
                    ],
                    borderWidth: 1,
                    data: [65, 59, 80, 81, 56, 55, 40],
                },
                {
                    label: "Temperatura Cereté",
                    backgroundColor: [
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)"
                    ],
                    hoverBackgroundColor: [
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)",
                        "rgba(238, 139, 152, 0.7)"
                    ],
                    borderColor: [
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)",
                        "rgba(238, 139, 152, 1)"
                    ],
                    borderWidth: 1,
                    data: [35, 40, 60, 47, 88, 27, 30],
                }
            ]
        }
    });


    // ------------------------------------------------------- //
    // Pie Chart 1
    // ------------------------------------------------------ //
    var PIECHART = $('#pieChartHome1');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false
            }
        },
        data: {
            labels: [
                "First",
                "Second",
                "Third",
                "Fourth"
            ],
            datasets: [
                {
                    data: [300, 50, 100, 60],
                    borderWidth: [0, 0, 0, 0],
                    backgroundColor: [
                        '#6933b9',
                        "#8553d1",
                        "#a372ec",
                        "#be9df1"
                    ],
                    hoverBackgroundColor: [
                        '#6933b9',
                        "#8553d1",
                        "#a372ec",
                        "#be9df1"
                    ]
                }]
        }
    });

    // ------------------------------------------------------- //
    // Pie Chart 2
    // ------------------------------------------------------ //
    var PIECHART = $('#pieChartHome2');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false
            }
        },
        data: {
            labels: [
                "First",
                "Second",
                "Third",
                "Fourth"
            ],
            datasets: [
                {
                    data: [80, 70, 100, 60],
                    borderWidth: [0, 0, 0, 0],
                    backgroundColor: [
                        '#9528b9',
                        "#b046d4",
                        "#c767e7",
                        "#e394fe"
                    ],
                    hoverBackgroundColor: [
                        '#9528b9',
                        "#b046d4",
                        "#c767e7",
                        "#e394fe"
                    ]
                }]
        }
    });

    // ------------------------------------------------------- //
    // Pie Chart 3
    // ------------------------------------------------------ //
    var PIECHART = $('#pieChartHome3');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false
            }
        },
        data: {
            labels: [
                "First",
                "Second",
                "Third",
                "Fourth"
            ],
            datasets: [
                {
                    data: [120, 90, 77, 95],
                    borderWidth: [0, 0, 0, 0],
                    backgroundColor: [
                        '#da4d60',
                        "#e96577",
                        "#f28695",
                        "#ffb6c1"
                    ],
                    hoverBackgroundColor: [
                        '#da4d60',
                        "#e96577",
                        "#f28695",
                        "#ffb6c1"
                    ]
                }]
        }
    });


    // ------------------------------------------------------- //
    // Sales Bar Chart 1
    // ------------------------------------------------------ //
    var BARCHART1 = $('#salesBarChart1');
    var barChartHome = new Chart(BARCHART1, {
        type: 'bar',
        options:
        {
            scales:
            {
                xAxes: [{
                    display: false,
                    barPercentage: 0.2
                }],
                yAxes: [{
                    display: false
                }],
            },
            legend: {
                display: false
            }
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Data Set 1",
                    backgroundColor: [
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99'
                    ],
                    borderColor: [
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99',
                        '#EF8C99'
                    ],
                    borderWidth: 0.2,
                    data: [35, 55, 65, 85, 40, 30, 18, 35, 20, 70]
                }
            ]
        }
    });

    // ------------------------------------------------------- //
    // Sales Bar Chart 21
    // ------------------------------------------------------ //
    var BARCHART1 = $('#salesBarChart2');
    var barChartHome = new Chart(BARCHART1, {
        type: 'bar',
        options:
        {
            scales:
            {
                xAxes: [{
                    display: false,
                    barPercentage: 0.2
                }],
                yAxes: [{
                    display: false
                }],
            },
            legend: {
                display: false
            }
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Data Set 1",
                    backgroundColor: [
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9'
                    ],
                    borderColor: [
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9',
                        '#CF53F9'
                    ],
                    borderWidth: 0.2,
                    data: [44, 75, 65, 34, 60, 45, 22, 35, 30, 63]
                }
            ]
        }
    });


    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //
    var PIECHARTEXMPLE    = $('#visitPieChart');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: false
            }
        },
        data: {
            labels: [
                "A",
                "B",
                "C",
                "D"
            ],
            datasets: [
                {
                    data: [300, 50, 100, 80],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };

});



// ######################################3 detalle
var LINECHART134 = $('#lineChartmonteria');
    var myLineChart = new Chart(LINECHART134, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 40,
                        min: 10,
                        stepSize: 0.1
                    },
                    display: false,
                    gridLines: {
                        display: false
                    }
                }]
            },
            legend: {
                display: true
            }
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Conductividad Monteria",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "transparent",
                    borderColor: '#EF8C99',
                    pointBorderColor: '#EF8C99',
                    pointHoverBackgroundColor: '#EF8C99',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "#EF8C99",
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 0,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [20, 21, 25, 22, 24, 18, 20, 23, 19, 22, 25, 19, 24],
                    spanGaps: false
                }
            ]
        }
    });


        // ------------------------------------------------------ //
        var BARCHARTEXMPLE    = $('#temperaturamonteria');
        var barChartExample = new Chart(BARCHARTEXMPLE, {
            type: 'line',
            options: {
                scales: {
                    xAxes: [{
                        display: true,
                        gridLines: {
                            color: '#eee'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        gridLines: {
                            color: '#eee'
                        }
                    }]
                },
            },
            data: {
                labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
                datasets: [
                    {
                        label: "Temperatura Monteria",
                        backgroundColor: [
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)"
                        ],
                        hoverBackgroundColor: [
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)",
                            "rgba(134, 77, 217, 0.57)"
                        ],
                        borderColor: [
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)",
                            "rgba(134, 77, 217, 1)"
                        ],
                        borderWidth: 1,
                        data: [28, 30 ,35 , 32 , 31 ,30 ,29,35],
                    }
                ]
            }
        });


var LINECHART12 = $('#phmonteria');
    var myLineChart = new Chart(LINECHART12, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 40,
                        min: 10,
                        stepSize: 0.1
                    },
                    display: false,
                    gridLines: {
                        display: false
                    }
                }]
            },
            legend: {
                display: true
            }
        },
        data: {
            labels: ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Ph Monteria",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "transparent",
                    borderColor: '#EF8C99',
                    pointBorderColor: '#EF8C99',
                    pointHoverBackgroundColor: '#EF8C99',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 2,
                    pointBackgroundColor: "#EF8C99",
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 0,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [30, 25, 32 ,27, 27 ,28 , 29 ,31 , 33],
                    spanGaps: false
                }
            ]
        }
    });


    var BARCHARTEXMPLEwew    = $('#turbidez');
    var barChartExample = new Chart(BARCHARTEXMPLEwew, {
        type: 'line',
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        color: '#eee'
                    }
                }],
                yAxes: [{
                    display: true,
                    gridLines: {
                        color: '#eee'
                    }
                }]
            },
        },
        data: {
            labels:  ["11:00:00", "11:00:20", "11:00:40", "11:01:00", "11:01:20", "11:01:40", "11:02:00"],
            datasets: [
                {
                    label: "Turbidez Monteria",
                    backgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    hoverBackgroundColor: [
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)",
                        "rgba(134, 77, 217, 0.57)"
                    ],
                    borderColor: [
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)",
                        "rgba(134, 77, 217, 1)"
                    ],
                    borderWidth: 1,
                    data: [28, 30 ,35 , 32 , 31 ,30 ,29,35],
                }
            ]
        }
    });
    