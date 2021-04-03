$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json"
        },        
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "username"},
            {"data": "opc"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    
                    var buttons = '<a href="/users/update/'  + row.id + '/" class="btn btn-secondary btn-xs btn-flat">Editar</a> ';
                    buttons += '<a href="/users/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat">Eliminar</i></a>';
                    return buttons;
                }
            }
                   
        ],
        initComplete: function (settings, json) {

        }
    });
});