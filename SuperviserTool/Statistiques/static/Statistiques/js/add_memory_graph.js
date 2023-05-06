$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrf-token');

    $.ajaxSetup({
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Csrf-Token', csrftoken);
        },
        cache: false
    });

    $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        url: 'api/get_memory_data',
        type: "GET",
        content_type: "application/json",
        success: function (response) {
            $.each(response, function (k, v) {
                console.log(k);
                $('#'+k+' #Memory_graph').append('<canvas id="'+k+'_memory_chart"></canvas>');
                var ctx = $('#'+k+'_memory_chart');
                    dataset = {
                        labels: v.labels,
                        datasets:[
                            {
                                label: "Memoire libre",
                                data: v.mem_free_data,
                                borderColor: '#1fc12c',
                                backgroundColor:'#1fc12c',
                                pointRadius: 2,
                                yAxisID:'y',
                            },
                            {
                                label: "Memoire Utilisée",
                                data: v.mem_used_data,
                                borderColor: '#ff3333',
                                backgroundColor:'#ff3333',
                                pointRadius: 2,
                                yAxisID:'y1',
                            }
                        ]
                    };
                new Chart(ctx,{
                    type: 'line',
                    data: dataset,
                    options:{
                        responsive: true,
                        interaction:{
                            mode: 'index',
                            intersect: false,
                        },
                        stacked:false,
                        plugins:{
                            title:{
                                display:true,
                                text: 'Utilisation mémoire'
                            },
                        },
                        scales:{
                            y:{
                                type:'linear',
                                display:true,
                                position: 'left',
                                max: v.mem_total,
                            },
                            y1:{
                                type:'linear',
                                display:true,
                                position: 'right',
                                grid:{
                                    drawOnChartArea:false,
                                },
                                max: v.mem_total,
                            }
                        }
                    }
                })
            });
        }
    });
    //Graph pour le swap
    $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        url: 'api/get_swap_data',
        type: "GET",
        content_type: "application/json",
        success: function (response) {
            $.each(response, function (k, v) {
                console.log(k),
                $('#'+k+' #Memory_graph').append('<canvas id="'+k+'_swap_chart"></canvas>');
                var ctx = $('#'+k+'_swap_chart');
                    dataset = {
                        labels: v.labels,
                        datasets:[
                            {
                                label: "Swap libre",
                                data: v.swap_free_data,
                                borderColor: '#1fc12c',
                                backgroundColor:'#1fc12c',
                                pointRadius: 2,
                                yAxisID:'y',
                            },
                            {
                                label: "Swap Utilisée",
                                data: v.swap_used_data,
                                borderColor: '#ff3333',
                                backgroundColor:'#ff3333',
                                pointRadius: 2,
                                yAxisID:'y1',
                            }
                        ]
                    };
                new Chart(ctx,{
                    type: 'line',
                    data: dataset,
                    options:{
                        responsive: true,
                        interaction:{
                            mode: 'index',
                            intersect: false,
                        },
                        stacked:false,
                        plugins:{
                            title:{
                                display:true,
                                text: 'Utilisation Swap'
                            },
                            zoom:{
                                mode: 'x',
                                drag: {
                                    enabled: true,
                                },
                                pinch:{
                                    enabled: true,
                                }
                            }
                        },
                        scales:{
                            y:{
                                type:'linear',
                                display:true,
                                position: 'left',
                                max: v.swap_total,
                            },
                            y1:{
                                type:'linear',
                                display:true,
                                position: 'right',
                                grid:{
                                    drawOnChartArea:false,
                                },
                                max: v.swap_total,
                            }
                        }
                    }
                })
            });
        }
    });
});
