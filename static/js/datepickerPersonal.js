$(document).ready(function() {
    $('#fechaNacimiento').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().subtract(15, 'year'),
		minDate: moment().subtract(70, 'year'),
		locale: 'es',
		viewMode: 'years',
		useCurrent: false
	});
	$('#fup').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().subtract(1, 'day'),
		minDate: moment().subtract(10, 'year'),
		locale: 'es',
		viewMode: 'months',
		useCurrent: false
	});
	$('#fur').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment(),
		minDate: moment().subtract(20, 'month'),
		locale: 'es',
		useCurrent: false
	});
	$('#fechaPap').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().subtract(1, 'day'),
		minDate: moment().subtract(10, 'year'),
		locale: 'es',
		viewMode: 'months',
		useCurrent: false
	});
	$('#fechaInicioMetodo').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().add(6, 'month'),
		minDate: moment(),
		locale: 'es',
		useCurrent: false
	});
	$('#fechaProximaConsulta').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().add(1, 'year'),
		minDate: moment(),
		locale: 'es',
		viewMode: 'months',
		useCurrent: false
	});
	$('#fechaNacimientoE').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().subtract(18, 'year'),
		minDate: moment().subtract(70, 'year'),
		locale: 'es',
		viewMode: 'years',
		useCurrent: false
	});
	$('#fechaInicio').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().add(1, 'year'),
		minDate: moment(),
		locale: 'es',
		useCurrent: false
	});
	$('#fechaFinal').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().add(1, 'year'),
		minDate: moment(),
		locale: 'es',
		useCurrent: false
	});
	$('#fechaPC').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment(),
		minDate: moment().subtract(2, 'year'),
		locale: 'es',
		useCurrent: false
	});
	$('#fechaProxC').datetimepicker({
		format: 'DD/MM/YYYY',
		maxDate: moment().add(1, 'year'),
		minDate: moment(),
		locale: 'es',
		useCurrent: false
	});
});