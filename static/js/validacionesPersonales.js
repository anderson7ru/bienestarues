$(document).ready(function() {
	
	//funcion para validar presion arterial
	FormValidation.Validator.presion = {
            validate: function(validator, $field, options){
                var value = $field.val();
                var pos = value.search("/");
                var tam = value.length;
                var sistolica = value.slice(0, pos);
                var diastolica = value.slice(pos + 1, tam);
                var aux1 = parseInt(sistolica);
                var aux2 = parseInt(diastolica);
                
                if(aux1 < 40 || aux1 > 300){
                    return {
                        valid: false,
                        message: 'Presion sistolica incorrecta'
                    };
                }
                
                if(aux2 < 40 || aux2 > 200){
                     return {
                        valid: false,
                        message: 'Presion diastolica incorrecta'
                    };
                }
                
                return true;
            }
        };
	
	
	//Formulario de datospersonalesapp<dpa>: Creacion de Paciente permanente
	$('#dpa_pacienteEditarForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            doctor:{
                validators:{
                    notEmpty:{
                        message: 'El doctor asignado es requerido'
                    }
                }
            },
            presionArterial: {
                validators: {
                    notEmpty: {
                        message: 'La presion Arterial es requerida'
                    },
                    regexp: {
                        regexp: /^[1-3]{0,1}[0-9]{2}\/[1-2]{0,1}[0-9]{2}$/,
                        message: 'Debe tener el formato: ej.40/40 o 300/200'
                    },
                    presion: {
                        message: 'Presion Arterial no es valida'
                    }
                }
            },
            frecuenciaRespiratoria: {
                validators: {
                    notEmpty: {
                        message: 'La frecuencia respiratoria es requerida'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 28,
                        message: 'Debe ser menor o igual a 28'
                    },
					greaterThan: {
                        value: 16,
                        message: 'Debe ser mayor o igual a 16'
                    }
                }
            },
            
			frecuenciaCardiaca: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 150,
                        message: 'Debe ser menor o igual a 150'
                    },
					greaterThan: {
                        value: 40,
                        message: 'Debe ser mayor o igual a 40'
                    }
                }
            },
			temperatura: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    lessThan: {
                        value: 40.0,
                        message: 'Debe ser menor o igual a 40.0'
                    },
					greaterThan: {
                        value: 30.0,
                        message: 'Debe ser mayor o igual a 30.0'
                    },
                    regexp: {
                        regexp: /^[0-9]+\.[0-9]{0,1}$/,
                        message: 'Debe ser formato: ##.#'
                    }
                }
            },
			peso: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 450,
                        message: 'Debe ser menor o igual a 450'
                    },
					greaterThan: {
                        value: 80,
                        message: 'Debe ser mayor o igual a 80'
                    }
                }
            },
            talla: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    lessThan: {
                        value: 2.50,
                        message: 'Debe ser menor o igual a 2.50'
                    },
					greaterThan: {
                        value: 1.30,
                        message: 'Debe ser mayor o igual a 1.30'
                    },
                    regexp: {
                        regexp: /^[0-9]+\.[0-9]{0,2}$/,
                        message: 'Debe ser formato: ##.##'
                    }
                }
            },
            apellidoPrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Apellido del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			apellidoSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombrePrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Nombre del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombreSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			fechaNacimiento: {
                validators: {
                    notEmpty: {
                        message: 'La fecha de Nacimiento es requerida'
                    },
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'La fecha de Nacimiento no es valida debe ser: DD/MM/YYYY'
                    }
                }
            },
			facultadE: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione la Facultad de procedencia'
                    }
                }
            },
            facultad: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione la Facultad de procedencia'
                    }
                }
            },
			codDepartamento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione Departamento'
                    }
                }
            },
			codMunicipio: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione Municipio'
                    }
                }
            },
			direccion: {
                validators: {
                    notEmpty: {
                        message: 'La direccion del paciente es requerida'
                    },
					stringLength: {
                        min: 10,
                        message: 'La direccion no puede tener menos de 10 caracteres'
                    }
                }
            },
			nombrePadre: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre del Padre no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombreMadre: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre de la Madre no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombrePareja: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre del Conyuge no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			emergencia: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
					stringLength: {
                        min: 5,
                        message: 'Este campo no puede tener menos de 5 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			telefonoEmergencia: {
                validators: {
                    notEmpty: {
                        message: 'Es necesario el telefono en caso de emergencia'
                    }
                }
            },
            due: {
                validators: {
                    notEmpty: {
                        message:  'Por favor de su numero de DUE'
                    },
                     stringLength: {
                        min: 7,
                        message: 'La longitud de este campo es de 7'
                    }
                }
            },
            nit: {
                enabled: false,
                validators: {
                    notEmpty: {
                        message: 'O su numero de NIT'
                    },
                    stringLength: {
                        min: 17,
                        message: 'La longitud de este campo es de 17'
                    }
                }
            },
            dui: {
                enabled: false,
                validators: {
                    notEmpty: {
                        message: 'sino proporcione su numero de DUI'
                    },
                     stringLength: {
                        min: 10,
                        message: 'La longitud de este campo es de 10'
                    }
                }
            }
        }
        })
        .on('keyup', '[name="due"], [name="nit"],[name="dui"]', function(e) {
                var due = $('#dpa_pacienteEditarForm').find('[name="due"]').val(),
                nit = $('#dpa_pacienteEditarForm').find('[name="nit"]').val(),
                dui = $('#dpa_pacienteEditarForm').find('[name="dui"]').val(),
                fv = $('#dpa_pacienteEditarForm').data('formValidation');
                
                switch($(this).attr('name')){
                    //Si esta enfocando due
                    case 'due':
                        fv.enableFieldValidators('nit',due === '').revalidateField('nit');
                        fv.enableFieldValidators('dui',due === '').revalidateField('dui');
                        
                        if (due && fv.getOptions('due', null, 'enabled') === false) {
                            fv.enableFieldValidators('due', true).revalidateField('due');
                            //alert ('va escribir due');
                        } else if (due === '' &&  (nit !== '' && dui !== '')) {
                            fv.enableFieldValidators('due', false).revalidateField('due');
                            //alert ('escriba nit o dui entonces');
                        }
                        break;
                    
                    //Si esta enfocando nit    
                    case 'nit':
                        if(nit === ''){
                            alert('nit esta en blanco');
                            fv.enableFieldValidators('due', true).revalidateField('due');
                            fv.enableFieldValidators('dui', true).revalidateField('dui');
                        }
                        else if(due === ''){
                            fv.enableFieldValidators('due', false).revalidateField('due');
                            //alert ('desactivando due');
                            //fv.enableFieldValidators('dui', false).revalidateField('dui');
                        }
                        else if(dui === ''){
                            fv.enableFieldValidators('dui', false).revalidateField('dui');
                            //alert ('desactivando dui');
                        }
                        
                        if(nit && (due === '' && dui === '') && fv.getOptions('nit',null,'enabled') === false ){
                            fv.enableFieldValidators('nit', true).revalidateField('nit');
                        }
                        break;    
                    
                    //Si esta enfocando dui
                    case 'dui':
                        if(dui === ''){
                            fv.enableFieldValidators('due', true).revalidateField('due');
                            fv.enableFieldValidators('nit', true).revalidateField('nit');
                        }
                        else if(due === '' ){
                            fv.enableFieldValidators('due', false).revalidateField('due');
                            //fv.enableFieldValidators('nit', false).revalidateField('nit');
                        }
                        else if(nit === ''){
                            fv.enableFieldValidators('nit', false).revalidateField('nit');
                        }
                        
                        if(dui && (due === '' && nit === '') && fv.getOptions('dui',null,'enabled') === false ){
                            fv.enableFieldValidators('dui', true).revalidateField('dui');
                        }
                        break;
                        
                    default:
                        break;
                }
        });
	
	//Formulario de planificacionfamiliarapp<pfa>: inscripcion
	$('#pfa_inscripcionEditarForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            paciente: {
                validators: {
                    notEmpty: {
                        message: 'El Paciente es requerido'
                    }
                }
            },
			aniosEscolaridad: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 20,
                        message: 'Debe ser menor o igual a 20'
                    },
					greaterThan: {
                        value: 1,
                        message: 'Debe ser mayor o igual a 1'
                    }
                }
            },
			embarazos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			partosTermino: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			prematuros: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			abortos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			vivos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			nacidosVivos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			nacidosMuertos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			partoVaginal: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			partoOpereratorio: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 10,
                        message: 'Debe ser menor o igual a 10'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			fup: {
                validators: {
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'El FUP no es valido'
                    }
                }
            },
			menarquia: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 25,
                        message: 'Debe ser menor o igual a 25'
                    },
					greaterThan: {
                        value: 8,
                        message: 'Debe ser mayor o igual a 8'
                    }
                }
            },
			fur: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
					date: {
                        format: 'DD/MM/YYYY',
                        message: 'El FUR no es valido'
                    }
                }
            },
			edadPrimeraVez: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 25,
                        message: 'Debe ser menor o igual a 25'
                    }
					,
					greaterThan: {
                        value: 8,
                        message: 'Debe ser mayor o igual a 8'
                    }
                }
            },
			duracionCiclo: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 100,
                        message: 'Debe ser menor o igual a 100'
                    },
					greaterThan: {
                        value: 10,
                        message: 'Debe ser mayor o igual a 10'
                    }
                }
            },
			duracionSangramiento: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 30,
                        message: 'Debe ser menor o igual a 30'
                    },
					greaterThan: {
                        value: 1,
                        message: 'Debe ser mayor o igual a 1'
                    }
                }
            },
			fechaPap: {
                validators: {
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'La fecha del ultimo PAP no es valido, debe ser: DD/MM/YYYY'
                    }
                }
            },
			resultado: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			agObservaciones: {
                validators: {
                   stringLength: {
                        max: 500,
						message: 'Solo se permiten 500 caracteres'
                    }
                }
            },
			apObservaciones: {
                validators: {
                   stringLength: {
                        max: 500,
						message: 'Solo se permiten 500 caracteres'
                    }
                }
            },
			metUtilizado: {
                validators: {
                   stringLength: {
                        max: 60,
						message: 'Solo se permiten 60 caracteres'
                    }
                }
            },
			metTiempo: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 100,
                        message: 'Debe ser menor o igual a 100'
                    },
					greaterThan: {
                        value: 1,
                        message: 'Debe ser mayor o igual a 1'
                    }
                }
            },
			metJustificar: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			metLugar: {
                validators: {
                   stringLength: {
                        max: 60,
						message: 'Solo se permiten 60 caracteres'
                    }
                }
            },
			temperatura: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    lessThan: {
                        value: 40.0,
                        message: 'Debe ser menor o igual a 40.0'
                    },
					greaterThan: {
                        value: 30.0,
                        message: 'Debe ser mayor o igual a 30.0'
                    },
                    regexp: {
                        regexp: /^[0-9]+\.[0-9]{0,1}$/,
                        message: 'Debe ser formato: ##.#'
                    }
                }
            },
			pulso: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 150,
                        message: 'Debe ser menor o igual a 150'
                    },
					greaterThan: {
                        value: 40,
                        message: 'Debe ser mayor o igual a 40'
                    }
                }
            },
			peso: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 450,
                        message: 'Debe ser menor o igual a 450'
                    },
					greaterThan: {
                        value: 80,
                        message: 'Debe ser mayor o igual a 80'
                    }
                }
            },
			presionArterial: {
                validators: {
                    notEmpty: {
                        message: 'La presion Arterial es requerida'
                    },
                    regexp: {
                        regexp: /^[1-3]{0,1}[0-9]{2}\/[1-2]{0,1}[0-9]{2}$/,
                        message: 'Debe tener el formato: ej.40/40 o 300/200'
                    },
                    presion: {
                        message: 'Presion Arterial no es valida'
                    }
                }
            },
			cabeza: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			cuello: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			mamas: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			torax: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			abdomen: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			miembros: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			gradoCistocele: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 3,
                        message: 'Debe ser menor o igual a 3'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			gradoRectocele: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 3,
                        message: 'Debe ser menor o igual a 3'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			gradoProlapsoUterino: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 3,
                        message: 'Debe ser menor o igual a 3'
                    },
					greaterThan: {
                        value: 0,
                        message: 'Debe ser mayor o igual a 0'
                    }
                }
            },
			secrecionVagina: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			cuObservaciones: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			uTumores: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			aTumores: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			fechaInicioMetodo: {
                validators: {
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'El Fecha no es valida, debe ser: DD/MM/YYYY'
                    }
                }
            },
			miONombre: {
                validators: {
                   stringLength: {
                        max: 15,
						message: 'Solo se permiten 15 caracteres'
                    }
                }
            },
			miOtros: {
                validators: {
                   stringLength: {
                        max: 15,
						message: 'Solo se permiten 15 caracteres'
                    }
                }
            },
			diagnostico: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			indicaciones: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            }
        }
    });
	
	//Formulario de planificacionfamiliarapp<pfa>: consulta subsecuente
	$('#pfa_consultasubEditarForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            peso: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 450,
                        message: 'Debe ser menor o igual a 450'
                    },
					greaterThan: {
                        value: 80,
                        message: 'Debe ser mayor o igual a 80'
                    }
                }
            },
			presionArterial: {
                validators: {
                    notEmpty: {
                        message: 'La presion Arterial es requerida'
                    },
                    regexp: {
                        regexp: /^[1-3]{0,1}[0-9]{2}\/[1-2]{0,1}[0-9]{2}$/,
                        message: 'Debe tener el formato: ej.40/40 o 300/200'
                    },
                    presion: {
                        message: 'Presion Arterial no es valida'
                    }
                }
            },
			metUtilizado: {
                validators: {
                   stringLength: {
                        max: 60,
						message: 'Solo se permiten 60 caracteres'
                    }
                }
            },
			metTiempo: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 100,
                        message: 'Debe ser menor o igual a 100'
                    },
					greaterThan: {
                        value: 1,
                        message: 'Debe ser mayor o igual a 1'
                    }
                }
            },
			histHallazgos: {
                validators: {
                   stringLength: {
                        max: 500,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			nombreCambio: {
                validators: {
                   stringLength: {
                        max: 50,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			motivoCambio: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			diagnostico: {
                validators: {
                   stringLength: {
                        max: 50,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            },
			indicaciones: {
                validators: {
                   stringLength: {
                        max: 100,
						message: 'Solo se permiten 100 caracteres'
                    }
                }
            }
        }
    });
    
    //Formulario de signosvitalesapp<sva>: Agregacion de signos vitales a un paciente
	$('#sva_signosEditarForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            paciente: {
                validators: {
                    notEmpty: {
                        message: 'El paciente es requerido'
                    }
                }
            },
            doctor:{
                validators:{
                    notEmpty:{
                        message: 'El doctor asignado es requerido'
                    }
                }
            },
			presionArterial: {
                validators: {
                    notEmpty: {
                        message: 'La presion Arterial es requerida'
                    },
                    regexp: {
                        regexp: /^[1-3]{0,1}[0-9]{2}\/[1-2]{0,1}[0-9]{2}$/,
                        message: 'Debe tener el formato: ej.40/40 o 300/200'
                    },
                    presion: {
                        message: 'Presion Arterial no es valida'
                    }
                }
            },
			frecuenciaCardiaca: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 150,
                        message: 'Debe ser menor o igual a 150'
                    },
					greaterThan: {
                        value: 40,
                        message: 'Debe ser mayor o igual a 40'
                    }
                }
            },
			temperatura: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    lessThan: {
                        value: 40.0,
                        message: 'Debe ser menor o igual a 40.0'
                    },
					greaterThan: {
                        value: 30.0,
                        message: 'Debe ser mayor o igual a 30.0'
                    },
                    regexp: {
                        regexp: /^[0-9]+\.[0-9]{0,1}$/,
                        message: 'Debe ser formato: ##.#'
                    }
                }
            },
			peso: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 450,
                        message: 'Debe ser menor o igual a 450'
                    },
					greaterThan: {
                        value: 80,
                        message: 'Debe ser mayor o igual a 80'
                    }
                }
            },
			talla: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
                    lessThan: {
                        value: 2.50,
                        message: 'Debe ser menor o igual a 2.50'
                    },
					greaterThan: {
                        value: 1.30,
                        message: 'Debe ser mayor o igual a 1.30'
                    },
                    regexp: {
                        regexp: /^[0-9]+\.[0-9]{0,2}$/,
                        message: 'Debe ser formato: ##.##'
                    }
                }
            },
			frecuenciaRespiratoria: {
                validators: {
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 28,
                        message: 'Debe ser menor o igual a 28'
                    },
					greaterThan: {
                        value: 16,
                        message: 'Debe ser mayor o igual a 16'
                    }
                }
            }
        }
    });
    
    // Formulario de empleadosapp<eea>: Creacion de Empleado
	$('#eea_empleadosEditarForm').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            apellidoPrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Apellido del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			apellidoSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombrePrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Nombre del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombreSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			fechaNacimiento: {
                validators: {
                    notEmpty: {
                        message: 'La fecha de Nacimiento es requerida'
                    },
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'La fecha de Nacimiento no es valida debe ser: DD/MM/YYYY'
                    }
                }
            }
		}
    });
	
	// The pattern of times that accepts moments between 09:00 to 17:00
    var TIME_PATTERN = /^(0[7-9]{1}|1[0-7]{1}):[0]{2}$/;
	// Formulario de empleadosapp<eea>: Creacion de Doctor
	$('#eea_doctorEditarForm').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
			especialidad: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione la Especialidad'
                    }
                }
            },
			dia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione por lo menos 1 dia de atencion'
                    }
                }
            },
			horaInicio: {
                verbose: false,
                validators: {
                    notEmpty: {
                        message: 'La hora que inician las consultas es requerida'
                    },
                    regexp: {
                        regexp: TIME_PATTERN,
                        message: 'La hora de inicio debe ser entre: 07:00 y 17:00'
                    },
                    callback: {
                        message: 'La hora de inicio debe ser antes de la hora final',
                        callback: function(value, validator, $field) {
                            var horaFinal = validator.getFieldElements('horaFinal').val();
                            if (horaFinal === '' || !TIME_PATTERN.test(horaFinal)) {
                                return true;
                            }
                            var startHour    = parseInt(value.split(':')[0], 10),
                                startMinutes = parseInt(value.split(':')[1], 10),
                                endHour      = parseInt(horaFinal.split(':')[0], 10),
                                endMinutes   = parseInt(horaFinal.split(':')[1], 10);

                            if (startHour < endHour || (startHour == endHour && startMinutes < endMinutes)) {
                                // The end time is also valid
                                // So, we need to update its status
                                validator.updateStatus('horaFinal', validator.STATUS_VALID, 'callback');
                                return true;
                            }

                            return false;
                        }
                    }
                }
            },
            horaFinal: {
                verbose: false,
                validators: {
                    notEmpty: {
                        message: 'La hora que finaliza las consultas es requerida'
                    },
                    regexp: {
                        regexp: TIME_PATTERN,
                        message: 'La hora de inicio debe ser entre: 07:00 y 17:00'
                    },
                    callback: {
                        message: 'La hora de fianl debe ser despues de la hora de inicio',
                        callback: function(value, validator, $field) {
                            var horaInicio = validator.getFieldElements('horaInicio').val();
                            if (horaInicio == '' || !TIME_PATTERN.test(horaInicio)) {
                                return true;
                            }
                            var startHour    = parseInt(horaInicio.split(':')[0], 10),
                                startMinutes = parseInt(horaInicio.split(':')[1], 10),
                                endHour      = parseInt(value.split(':')[0], 10),
                                endMinutes   = parseInt(value.split(':')[1], 10);

                            if (endHour > startHour || (endHour == startHour && endMinutes > startMinutes)) {
                                // The start time is also valid
                                // So, we need to update its status
                                validator.updateStatus('horaInicio', validator.STATUS_VALID, 'callback');
                                return true;
                            }

                            return false;
                        }
                    }
                }
            },
			pacienteConsulta:  {
                validators: {
                    notEmpty: {
                        message: 'Debe especificar cuantos pacientes atiende por hora el Doctor'
                    },
                    integer: {
                        message: 'Se aceptan solo numeros'
                    },
					lessThan: {
                        value: 30,
                        message: 'Debe ser menor o igual a 30'
                    },
					greaterThan: {
                        value: 1,
                        message: 'Debe ser mayor o igual a 1'
                    }
                }
            }
		}
	});
	
	// The pattern of times that accepts moments between 09:00 to 17:00
    var TIME_PATTERN = /^(0[7-9]{1}|1[0-7]{1}):[0]{2}$/;
	// Formulario de citasmedicasapp<cma>: Creacion de Cita Medica
	$('#cma_citamedicaEditarForm').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
			paciente: {
                validators: {
                    notEmpty: {
                        message: 'El Paciente es requerido'
                    }
                }
            },
			horaConsulta: {
                validators: {
                    notEmpty: {
                        message: 'La hora de la consultas es requerida'
                    },
                    regexp: {
                        regexp: TIME_PATTERN,
                        message: 'El formato es: HH:MM'
                    }
                }
            },
		}
	});
	
	// The pattern of times that accepts moments between 09:00 to 17:00
    var TIME_PATTERN = /^(0[7-9]{1}|1[0-7]{1}):[0]{2}$/;
	// Formulario de citasmedicasapp<cma>: Creacion de Cancelacion
	$('#cma_cancelacionEditarForm').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
			fechaInicio: {
                validators: {
                    notEmpty: {
                        message: 'Esta fecha es requerida'
                    },
                    date: {
                        format: 'DD/MM/YYYY',
						//max: 'fechaFinal',
                        message: 'La fecha debe ser: DD/MM/YYYY y menor que la fecha de finalizacion'
                    }
                }
            },
			fechaFinal: {
                validators: {
                    date: {
                        format: 'DD/MM/YYYY',
						//min: 'fechaInicio',
                        message: 'La fecha debe ser: DD/MM/YYYY y mayor que la fecha de inicio'
                    }
                }
            },
			horaInicio: {
                verbose: false,
                validators: {
                    notEmpty: {
                        message: 'La hora que inicia la consulta es requerida'
                    },
                    regexp: {
                        regexp: TIME_PATTERN,
                        message: 'La hora de inicio debe ser entre: 07:00 y 17:00'
                    },
                    callback: {
                        message: 'La hora de inicio debe ser antes de la hora final',
                        callback: function(value, validator, $field) {
                            var horaFinal = validator.getFieldElements('horaFinal').val();
                            if (horaFinal === '' || !TIME_PATTERN.test(horaFinal)) {
                                return true;
                            }
                            var startHour    = parseInt(value.split(':')[0], 10),
                                startMinutes = parseInt(value.split(':')[1], 10),
                                endHour      = parseInt(horaFinal.split(':')[0], 10),
                                endMinutes   = parseInt(horaFinal.split(':')[1], 10);

                            if (startHour < endHour || (startHour == endHour && startMinutes < endMinutes)) {
                                // The end time is also valid
                                // So, we need to update its status
                                validator.updateStatus('horaFinal', validator.STATUS_VALID, 'callback');
                                return true;
                            }

                            return false;
                        }
                    }
                }
            },
            horaFinal: {
                verbose: false,
                validators: {
                    notEmpty: {
                        message: 'La hora que finaliza la consulta es requerida'
                    },
                    regexp: {
                        regexp: TIME_PATTERN,
                        message: 'La hora de inicio debe ser entre: 07:00 y 17:00'
                    },
                    callback: {
                        message: 'La hora de final debe ser despues de la hora de inicio',
                        callback: function(value, validator, $field) {
                            var horaInicio = validator.getFieldElements('horaInicio').val();
                            if (horaInicio == '' || !TIME_PATTERN.test(horaInicio)) {
                                return true;
                            }
                            var startHour    = parseInt(horaInicio.split(':')[0], 10),
                                startMinutes = parseInt(horaInicio.split(':')[1], 10),
                                endHour      = parseInt(value.split(':')[0], 10),
                                endMinutes   = parseInt(value.split(':')[1], 10);

                            if (endHour > startHour || (endHour == startHour && endMinutes > startMinutes)) {
                                // The start time is also valid
                                // So, we need to update its status
                                validator.updateStatus('horaInicio', validator.STATUS_VALID, 'callback');
                                return true;
                            }

                            return false;
                        }
                    }
                }
            }
		}
	});
	
	// Formulario de laboraotorioapp<eea>: Creacion de Examen de Hematologia
	$('#hematologiaForm').formValidation({
	    framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
	});
	
	// Formulario para hacer el expediente permanente a partir de un expediente provisionale
	$('#dpa_pacienteProvisionalEditarForm').formValidation({
	    framework: 'bootstrap',
	    icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        
        fields: {
            apellidoPrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Apellido del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			apellidoSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombrePrimero: {
                validators: {
                    notEmpty: {
                        message: 'El Primer Nombre del paciente es requerido'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z\.]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombreSegundo: {
                validators: {
                    regexp: {
                        regexp: /^[a-zA-Z\. ]+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			fechaNacimiento: {
                validators: {
                    notEmpty: {
                        message: 'La fecha de Nacimiento es requerida'
                    },
                    date: {
                        format: 'DD/MM/YYYY',
                        message: 'La fecha de Nacimiento no es valida debe ser: DD/MM/YYYY'
                    }
                }
            },
			facultadE: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione la Facultad de procedencia'
                    }
                }
            },
            facultad: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione la Facultad de procedencia'
                    }
                }
            },
			codDepartamento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione Departamento'
                    }
                }
            },
			codMunicipio: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione Municipio'
                    }
                }
            },
			direccion: {
                validators: {
                    notEmpty: {
                        message: 'La direccion del paciente es requerida'
                    },
					stringLength: {
                        min: 10,
                        message: 'La direccion no puede tener menos de 10 caracteres'
                    }
                }
            },
			nombrePadre: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre del Padre no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombreMadre: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre de la Madre no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			nombrePareja: {
                validators: {
                    stringLength: {
                        min: 3,
                        message: 'El Nombre del Conyuge no puede tener menos de 3 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			emergencia: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    },
					stringLength: {
                        min: 5,
                        message: 'Este campo no puede tener menos de 5 letras'
                    },
                    regexp: {
                        regexp: /^([a-zA-Z\.\s])+$/,
                        message: 'Se aceptan solo letras y el punto'
                    }
                }
            },
			telefonoEmergencia: {
                validators: {
                    notEmpty: {
                        message: 'Es necesario el telefono en caso de emergencia'
                    }
                }
            },
            nit: {
                validators: {
                    notEmpty: {
                        message: 'El NIT es obligatorio'
                    }
                }
            },
            due: {
                validators: {
                     stringLength: {
                        min: 7,
                        message: 'La longitud de este campo es de 7'
                    }
                }
            },
            dui: {
                validators: {
                    stringLength: {
                        min: 10,
                        message: 'La longitud de este campo es de 10'
                    }
                }
            }
        }
        
	});
	
	$('#psicologiaForm').formValidation({
	framework: 'bootstrap',
	icon: {
		valid: 'glyphicon glyphicon-ok',
		invalid: 'glyphicon glyphicon-remove',
		validating: 'glyphicon glyphicon-refresh'
	},                   
		fields: {
			numeroHijos: {
				validators: {
					integer: {
						message: 'Debe ser un numero entero'
					},
					greatherThan: {
						value: -1,
						message: 'Deber igual o mayor que cero'
					},
				}
			},
			profesion: {
				validators: {
					notEmpty: {
						message: 'Este campo es obligatorio'
					}
                }
            },
			direccionResponsable: {
				validators: {
					notEmpty: {
						message: 'La direccion es obligatoria'
					},
					stringLength: {
						min: 5,
						message: 'La direccion no puede tener menos de 5 letras'
					}
				}
			},
			fecha_primeraConsulta: {
				validators: {
					notEmpty: {
						message: 'Esta fecha es obligatoria'
					}					
				}
			},
			referido: {
				validators: {
					notEmpty: {
						message: 'Seleccione el medico que refirio al paciente'
					}
				}
			},
			familia: {
				validators: {
				    notEmpty: {
						message: 'Este campo es obligatorio'
					},
					integer: {
						message: 'Debe ser un numero entero'
					},
					greatherThan: {
						value: 0,
						message: 'Debe ser un numero positivo'
					}
				}
			},
			motivo: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar el motivo de consulta'
					}	
				}
			},
			antecedentes :{
				validators :{
					notEmpty: {
						message: 'Debe ingresar los antecedentes del problema'
					}
				}
			},
			apariencia: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar la apariencia'
					}
				}
			},
			voz: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			patrones: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar los patrones de habla'
					}
				}
			},
			expresionesF: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			ademanes: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			actitudes_tx: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			impresion_dx: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			plan_tx: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			pronostico: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar este campo'
					}
				}
			},
			fecha_proximaCita: {
				validators: {
					notEmpty: {
						message: 'Debe ingresar la fecha de la proxima cita'
					}
				}
			},
			religion: {
			    validators: {
			        notEmpty: {
			            message: 'Debe ingresar la religion que profesa'
			        }
			    }
			}
        } 
    });

	//Validaciones para el proceso terapeutico   
    $('#procesoterapeutico_form').formValidation({
        framework: 'bootstrap',
    	icon: {
    		valid: 'glyphicon glyphicon-ok',
    		invalid: 'glyphicon glyphicon-remove',
    		validating: 'glyphicon glyphicon-refresh'
    	}, 
        	fields: {
        	    objetivo: {
        	        validators: {
        	            notEmpty: {
        	                message: 'Debe ingresar el objetivo terapeutico'
        	            }
        	        }
        	    },
        	    tecnicas: {
        	        validators: {
        	            notEmpty: {
        	                message: 'Debe ingresar la tecnica a usar'
        	            }
        	        }
        	    },
        	    observaciones: {
        	        validators: {
        	            notEmpty: {
        	                message: 'Debe ingresar las observaciones'
        	            }
        	            
        	        }
        	    }
        	}
    });
    
	//Validaciones para el registro de avance
	$('#registroavance_form').formValidation({
        framework: 'bootstrap',
    	icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        }, 
        	fields: {
        	    paciente: {
        	        validators: {
        	            notEmpty: {
                            message: 'Debe ingresar los comentarios del paciente'
                        }
        	        }
        	    },
        	    psicologo: {
        	        validators: {
        	            notEmpty: {
                            message: 'Debe ingresar los comentarios del psicologo'
                        }
        	        }
        	    }
        	}
    });

    //Formulario de nuevoingresoapp<nvi>: Creacion de certificado medico
    $('#nvi_certificadoSaludForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            enfermedadIC: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
            enfermedadEF:{
                validators:{
                    notEmpty:{
                        message: 'Este campo es requerido'
                    }
                }
            },
			enfermedadSN: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoHIV: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoHECES: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoVDRL: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoHemograma: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoOrina: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			resultadoRX: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
			presentaImpedimentos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            },
            aptoAprobado: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es requerido'
                    }
                }
            }
        }
    });
    
    //Validaciones para el cambio de contraseña
    $('#cu_cambiopassForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            pass1: {
                validators: {
                    notEmpty: {
                        message: 'El Password es requerido'
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: 'El password debe tener al menos 6 caracteres'
                    }
                }
            },
            pass2: {
                validators: {
                    notEmpty: {
                        message: 'El Password es requerido'
                    },
                    identical: {
                        field: 'pass1',
                        message: 'Debe escribir el mismo password'
                    }
                }
            }
        }
        
    });
    
    $('#resetPasswordForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            email: {
                validators: {
                    notEmpty: {
                        message: 'El Correo es requerido'
                    },
                    emailAddress: {
                            message: 'No es un direccion de email valida'
                        },
                    regexp: {
                        regexp: '^[^@\\s]+@([^@\\s]+\\.)+[^@\\s]+$',
                        message: 'No es un direccion de email valida'
                    }
                }
            }
        }
    });
    
    $('#eea_usuarioEditarForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            email: {
                validators: {
                    notEmpty: {
                        message: 'El Correo es requerido'
                    },
                    emailAddress: {
                            message: 'No es un direccion de email valida'
                        },
                    regexp: {
                        regexp: '^[^@\\s]+@([^@\\s]+\\.)+[^@\\s]+$',
                        message: 'No es un direccion de email valida'
                    }
                }
            },
            grupos: {
                validators: {
                    choice: {
                        min: 1,
                        max: 3,
                        message: 'Por Favor escoja al menos un tipo de usuario (Maximo 3)'
                    }
                }
            }
        }
    });
    
});



