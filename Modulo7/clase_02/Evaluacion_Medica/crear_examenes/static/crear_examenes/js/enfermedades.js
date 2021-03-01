
function myOnLoad() {
    cargar_enfermedades()
    cargar_medicos()
    contarFilas()
    //cargarTabla()
}

// Rutina para cargar datos de enfermedades al <select>
function cargar_enfermedades() {
    var array = ['Hepatitis C', 'Artritis idiopática juvenil', 'Fibrosis quística', 'Cáncer gástrico', 'Esquizofrenia', 'Diabetes Mellitus tipo I', 'Hemofilia', 'Gran quemado', 'Lupus eritematoso sistémico', 'Retinopatía del prematuro'];
    array.sort();
    addOptions("enfermedad", array);
}

// Rutina para cargar datos de medicos al <select>
function cargar_medicos() {
    var array = ['MARCELO GONZALEZ', 'MARIA ACEVEDO', 'CHRISTINA HAFERMALZ ADANIEL', 'DANIEL AGUIRRE', 'XIMENA AHUMADA', 'IGNACIA ALLENDE', 'RODRIGO PEREZ'];
    array.sort();
    addOptions("medico", array);
}

// Rutina para agregar opciones a un <select>
function addOptions(domElement, array) {
    var select = document.getElementsByName(domElement)[0];
    for (value in array) {
        var option = document.createElement("option");
        option.text = array[value];
        select.add(option);
    }
}


/* function cargarTabla() {
    var myTableDiv = document.getElementById("metric_results")
    var table = document.createElement('TABLE')
    var tableBody = document.createElement('TBODY')

    table.border = '0'
    table.appendChild(tableBody);

    var heading = new Array();
    heading[0] = "Código"
    heading[1] = "Diagnostico"
    heading[2] = "Médico tratante"
    heading[3] = "Fecha"
    heading[4] = "Hora"
    heading[5] = ""

    var stock = new Array()
    stock[0] = new Array("COD-01-01-01", "Trastorno Bipolar en personas de 15 años y más", "MARIA VALERIA ACEVEDO ARANGUA", "01-01-2000", "16:30")
    stock[1] = new Array("COD-01-01-01", "Trastorno Bipolar en personas de 15 años y más", "MARIA VALERIA ACEVEDO ARANGUA", "01-01-2000", "16:30")
    stock[2] = new Array("COD-01-01-01", "Trastorno Bipolar en personas de 15 años y más", "MARIA VALERIA ACEVEDO ARANGUA", "01-01-2000", "16:30")
    stock[3] = new Array("COD-01-01-01", "Trastorno Bipolar en personas de 15 años y más", "MARIA VALERIA ACEVEDO ARANGUA", "01-01-2000", "16:30")
    stock[4] = new Array("COD-01-01-01", "Trastorno Bipolar en personas de 15 años y más", "MARIA VALERIA ACEVEDO ARANGUA", "01-01-2000", "16:30")

    //COLUMNAS DE LA TABLA
    var tr = document.createElement('TR');
    tableBody.appendChild(tr);
    for (i = 0; i < heading.length; i++) {
        var th = document.createElement('TH')
        th.width = '220';
        th.appendChild(document.createTextNode(heading[i]));
        tr.appendChild(th);
    }

    //FILAS DE LA TABLA
    for (i = 0; i < stock.length; i++) {
        var tr = document.createElement('TR');
        for (j = 0; j < stock[i].length; j++) {
            var td = document.createElement('TD')
            td.appendChild(document.createTextNode(stock[i][j]))
            tr.appendChild(td)
        }
        tableBody.appendChild(tr);
    }
    myTableDiv.appendChild(table)
} */

/*
function anadirRegistro() {
    var codigo = "COD-" + Math.floor(Math.random() * 999999);
    var diagnostico = $('select[name="enfermedad"]').val();
    var medico = $('select[name="medico"]').val();
    var anamnesis = $('#anamnesis').val();
    var tratamiento = $('#tratamiento').val();
    var hora = $('#hora').val();
    var fecha = $('#fecha').val();

    console.log(codigo + " " + diagnostico + " " + medico + " " + anamnesis + " " + tratamiento +
        " " + hora + " " + fecha + "EDIT" + "DEL");

    //var tipo = $('input[name="optradio"]:checked').val();
    //var accion = $('#comentarios').val();
    //var fechafin = $('#fecha_final').val();

    $('table tbody').append('<tr><td>' + codigo + '</td><td>' + diagnostico + '</td><td>' + medico +
        '</td><td>' + anamnesis + '</td><td>' + tratamiento + '</td><td>' + hora + '</td><td>' +
         fecha + '<td class="text-right py-0 align-middle"></td> ' +
            '<div class="btn-group btn-group-sm"> <a href="#" class="btn btn-info"><i class="fas fa-eye"></i></a> <a href="#" class="btn btn-danger"><i class="fas fa-trash"></i></a>' +
            ' </div>'
       + '</td></tr>');
    $("#modalNuevaData").modal('hide');


}

*/
function eliminarRegistro() {
    var tbody = $('#tablaEnfermedades tbody');
    var fila_contenido = tbody.find('tr').first().html();
    //Agregar fila nueva.
    //Eliminar fila.
    $('#tablaEnfermedades').on('click', '.boton_eliminar', function () {
        $(this).parents('tr').eq(0).remove();
    });
}

function contarFilas() {
    var $num = document.getElementById('tablaEnfermedades').getElementsByTagName('tr').length - 1;
    if ($num == 0){
        lblCantidadRegistro.innerHTML = "No posee registros asociados. " + $num + " enfermedades";
    }else{
        lblCantidadRegistro.innerHTML = "Usted tiene " + $num + " enfermedades asociadas.";
    }
    
}
